#!/usr/bin/env python3
"""Validate and aggregate declared CEPB evidence. No models or network are used.

This program checks structure, declared coverage, arithmetic and clocks. It
cannot establish the truth of evidence, interpret behavioral anchors, identify
real humans or issue an independent certification.
"""
from __future__ import annotations

import argparse
import calendar
import json
import math
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

FRAMEWORK = "CEPB-1.0.0"
SUITE_VERSION = "CEPB-SUITE-1.0.0"
O_RUBRIC = "CEPB-O-0.1"
RULE_PUBLICATION_FLOOR = "2026-10-09T15:00:00Z"
ROOT = Path(__file__).resolve().parent
STATUSES = {"scored", "unsupported", "unobserved", "log_missing", "system_failed",
            "disputed", "not_applicable", "plan_error", "protocol_error"}
CONDITIONS = {"ordinary", "stress", "heldout"}
QUICK_IDS = ["CEPB_" + i for i in "A1 A2 B2 B3 B4 C1 C2 C3 D1 D3 D5 E1 E3 F4 G1 G3 M1 N5".split()]
BASE_GATES = ["identity_evidence", "persistence", "scope", "procedure"]


def required_gate_ids(track):
    gates = list(BASE_GATES)
    if track in {"World", "Integrated"}:
        gates.append("world_connection")
    if track == "Integrated":
        gates.append("longitudinal")
    return gates


def short_id(item):
    return item.removeprefix("CEPB_")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _no_constant(value):
    raise ValueError(f"non-finite JSON number: {value}")


def load_json(path):
    value = json.loads(Path(path).read_text(encoding="utf-8-sig"),
                       object_pairs_hook=_unique_object, parse_constant=_no_constant)
    def finite(entry):
        if type(entry) is float and not math.isfinite(entry):
            raise ValueError("non-finite JSON number")
        if isinstance(entry, dict):
            for child in entry.values():
                finite(child)
        elif isinstance(entry, list):
            for child in entry:
                finite(child)
    finite(value)
    return value


def is_number(value):
    return type(value) is int or (type(value) is float and math.isfinite(value))


def is_score(value, integer=False):
    return (type(value) is int if integer else is_number(value)) and 0 <= value <= 5


def utc_time(value):
    """Require an explicit UTC offset; never interpret a simulated/naive clock."""
    if not isinstance(value, str) or "T" not in value:
        raise ValueError("expected ISO UTC timestamp")
    if not (value.endswith("Z") or value.endswith("+00:00")):
        raise ValueError("timestamp must use Z or +00:00")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.utcoffset() != timezone.utc.utcoffset(result):
        raise ValueError("timestamp must be UTC")
    return result.astimezone(timezone.utc)


def iso_time(value):
    return value.isoformat().replace("+00:00", "Z") if value is not None else None


def add_calendar_months(value, months=36):
    """Calendar months, preserving time and clipping to the target month's end."""
    total = value.year * 12 + value.month - 1 + months
    year, month_zero = divmod(total, 12)
    month = month_zero + 1
    day = min(value.day, calendar.monthrange(year, month)[1])
    return value.replace(year=year, month=month, day=day)


def load_catalog(path=None):
    catalog = load_json(path or ROOT / "data" / "items.json")
    if catalog.get("framework") != FRAMEWORK:
        raise ValueError("catalog framework mismatch")
    domains = catalog.get("domains", [])
    weights = {entry["id"]: entry["weight"] for entry in domains}
    if len(weights) != len(domains) or any(not is_number(w) or w <= 0 for w in weights.values()):
        raise ValueError("invalid catalog domain weights")
    items = catalog.get("items", [])
    by_id = {entry["id"]: entry for entry in items}
    if len(by_id) != len(items) or any(entry.get("domain") not in weights for entry in items):
        raise ValueError("invalid catalog item IDs/domains")
    tracks = catalog.get("tracks", {})
    for name, track in tracks.items():
        ids = track.get("items", [])
        if not ids or len(ids) != len(set(ids)) or any(i not in by_id for i in ids):
            raise ValueError(f"invalid catalog track: {name}")
        selected = {by_id[i]["domain"] for i in ids}
        if name != "Quick":
            if any(sum(by_id[i]["domain"] == d for i in ids) != 6 for d in selected):
                raise ValueError(f"formal track must include six items per domain: {name}")
            if not math.isclose(sum(weights[d] for d in selected), track.get("max_points", -1)):
                raise ValueError(f"catalog track total mismatch: {name}")
    if tracks.get("Quick", {}).get("items") != QUICK_IDS:
        raise ValueError("Quick must use its declared 18-item diagnostic set")
    return catalog


class Audit:
    def __init__(self, run, catalog, base, now=None):
        self.run, self.catalog, self.base = run, catalog, Path(base)
        self.issues = []
        self.as_of = None
        self.temporal = {"lineage_t0": None, "lineage_matures_at": None,
                         "scopes": [], "full_attainment_not_before": None}
        self.bundle_values = {}
        self.presence_stats = {}
        self.now = now or datetime.now(timezone.utc)

    def issue(self, code, message, *, item=None, severity="error", bundle=None):
        self.issues.append({"code": code, "message": message, "item_id": item,
                            "bundle_id": bundle, "severity": severity})

    def text(self, value, label, *, item=None):
        if not isinstance(value, str) or not value.strip():
            self.issue("required_text", f"{label}: non-empty text required", item=item)
            return False
        return True

    def timestamp(self, value, label, *, item=None, nullable=False, allow_future=False):
        if value is None and nullable:
            return None
        try:
            result = utc_time(value)
        except (ValueError, TypeError, OverflowError):
            self.issue("invalid_clock", f"{label}: explicit ISO UTC timestamp required", item=item)
            return None
        if not allow_future and self.as_of is not None and result > self.as_of:
            self.issue("future_clock", f"{label}: later than as_of", item=item)
        return result

    def ref(self, value, label, *, item=None):
        if not self.text(value, label, item=item):
            return
        if value.startswith("https://"):
            parts = urlsplit(value)
            if not parts.hostname or parts.username or parts.password:
                self.issue("invalid_ref", f"{label}: invalid HTTPS reference", item=item)
            return  # Syntactic check only; no network request or truth verification.
        if "://" in value:
            self.issue("invalid_ref", f"{label}: use a local file or HTTPS URL", item=item)
            return
        path = Path(value.split("#", 1)[0])
        if not path.is_absolute():
            path = self.base / path
        try:
            exists = path.is_file()
        except (OSError, ValueError):
            exists = False
        if not exists:
            self.issue("missing_ref", f"{label}: local file missing: {value}", item=item, severity="missing")

    def reference_available(self, value):
        """Check optional stage evidence without making a lower stage invalid."""
        if not isinstance(value, str) or not value.strip():
            return False
        if value.startswith("https://"):
            try:
                parts = urlsplit(value)
                return bool(parts.hostname) and not parts.username and not parts.password
            except ValueError:
                return False
        if "://" in value:
            return False
        path = Path(value.split("#", 1)[0])
        try:
            return (path if path.is_absolute() else self.base / path).is_file()
        except (OSError, ValueError):
            return False

    def refs(self, values, label, *, item=None, required=True):
        if not isinstance(values, list):
            self.issue("invalid_refs", f"{label}: list required", item=item)
            return
        if required and not values:
            self.issue("evidence_missing", f"{label}: evidence required", item=item, severity="missing")
        for ref in values:
            self.ref(ref, label, item=item)

    def ids(self, values, label, *, item=None, minimum=1):
        if not isinstance(values, list) or any(not isinstance(i, str) or not i.strip() for i in values):
            self.issue("invalid_ids", f"{label}: non-empty string IDs required", item=item)
            return []
        if len(values) != len(set(values)):
            self.issue("duplicate_id", f"{label}: duplicate IDs", item=item)
        if len(values) < minimum:
            self.issue("coverage_missing", f"{label}: at least {minimum} IDs required", item=item, severity="missing")
        return values

    def raters(self, bundle, item):
        entries = bundle.get("rater_scores")
        if not isinstance(entries, list) or not entries:
            self.issue("rater_missing", "bundle rater_scores required", item=item, severity="missing")
            return []
        ids = []
        for entry in entries:
            if not isinstance(entry, dict):
                self.issue("invalid_rater", "rater score must be an object", item=item)
                continue
            if self.text(entry.get("rater_id"), "rater_id", item=item):
                ids.append(entry["rater_id"])
            if not is_score(entry.get("score"), integer=True):
                self.issue("invalid_score", "rater score must be an integer 0..5", item=item)
        if len(ids) != len(set(ids)):
            self.issue("duplicate_rater", "rater IDs must be distinct", item=item)
        scores = [r.get("score") for r in entries if isinstance(r, dict) and is_score(r.get("score"), integer=True)]
        if scores and any(s != bundle.get("score") for s in scores) and not bundle.get("adjudication_ref"):
            self.issue("rater_disagreement", "rater/final disagreement requires adjudication_ref; preserve raw scores",
                       item=item, severity="missing")
        return ids

    def highest_level(self, bundle, item, raters):
        if bundle.get("score") != 5:
            return
        if len(set(raters)) < 2:
            self.issue("score5_raters", "score 5 requires two distinct raters", item=item)
        self.ref(bundle.get("independent_check_ref"), "score 5 independent_check_ref", item=item)
        if short_id(item).startswith("P"):
            return  # A cumulative window does not use behavioral heldout cases.
        secrecy = bundle.get("heldout_secrecy")
        if not isinstance(secrecy, dict) or secrecy.get("declared") is not True:
            self.issue("score5_heldout", "score 5 requires heldout secrecy declaration", item=item)
        else:
            self.ref(secrecy.get("evidence_ref"), "heldout secrecy evidence_ref", item=item)

    def manifest(self):
        run = self.run
        if not isinstance(run, dict):
            self.issue("invalid_run", "run must be a JSON object")
            return
        for field in ("campaign_id", "suite_version"):
            self.text(run.get(field), field)
        if run.get("framework") != FRAMEWORK:
            self.issue("framework_mismatch", f"framework must be {FRAMEWORK}")
        if run.get("suite_version") != SUITE_VERSION:
            self.issue("suite_mismatch", f"this CLI supports {SUITE_VERSION}")
        if run.get("track") not in self.catalog["tracks"]:
            self.issue("invalid_track", "unknown track; tracks are not interchangeable")
        self.as_of = self.timestamp(run.get("as_of"), "as_of")
        if self.as_of is not None and self.as_of > self.now:
            self.issue("future_as_of", "as_of is later than current actual UTC time")
        for name, fields in (("character", ("mode", "id", "definition_ref")),
                             ("system", ("version", "manifest_ref"))):
            value = run.get(name)
            if not isinstance(value, dict):
                self.issue("required_object", f"{name} object required")
                continue
            for field in fields:
                if field.endswith("_ref"):
                    self.ref(value.get(field), f"{name}.{field}")
                else:
                    self.text(value.get(field), f"{name}.{field}")
        protocol = run.get("protocol")
        if not isinstance(protocol, dict):
            self.issue("required_object", "protocol object required")
        else:
            self.timestamp(protocol.get("registered_at"), "protocol.registered_at")
            if protocol.get("frozen_before_execution") is not True:
                self.issue("protocol_not_frozen", "protocol must be frozen before execution")
        verification = run.get("verification")
        if not isinstance(verification, dict):
            self.issue("required_object", "verification object required")
        else:
            if verification.get("level") not in {"self_reported", "independently_reviewed"}:
                self.issue("invalid_verification", "invalid verification level")
            ids = self.ids(verification.get("reviewer_ids"), "verification.reviewer_ids", minimum=0)
            self.ref(verification.get("disclosure_ref"), "verification.disclosure_ref")
            if verification.get("report_ref") is not None:
                self.ref(verification["report_ref"], "verification.report_ref")
            if verification.get("level") == "independently_reviewed":
                if len(set(ids)) < 2:
                    self.issue("reviewer_missing", "independent review needs two distinct reviewer IDs")
                if verification.get("report_ref") is None:
                    self.issue("review_missing", "independent review needs report_ref")
        gates = run.get("gates")
        if not isinstance(gates, list):
            self.issue("invalid_gates", "gates list required")
        else:
            ids = []
            for gate in gates:
                if not isinstance(gate, dict):
                    self.issue("invalid_gate", "gate must be an object")
                    continue
                if self.text(gate.get("id"), "gate.id"):
                    ids.append(gate["id"])
                if gate.get("status") not in {"clear", "unresolved", "not_assessed"}:
                    self.issue("invalid_gate", "invalid gate status")
                self.refs(gate.get("evidence_refs"), "gate.evidence_refs", required=gate.get("status") != "not_assessed")
            if len(ids) != len(set(ids)):
                self.issue("duplicate_gate", "gate IDs must be distinct")
        self.lineage()

    def lineage(self):
        value = self.run.get("lineage")
        if not isinstance(value, dict):
            self.issue("required_object", "lineage object required")
            return
        if value.get("kind") not in {"FIXED_RELEASE", "MAINTAINED_LINEAGE"}:
            self.issue("invalid_lineage", "lineage kind must be FIXED_RELEASE or MAINTAINED_LINEAGE")
        times = [self.timestamp(value.get(k), f"lineage.{k}", nullable=True)
                 for k in ("rule_publication_at", "registered_at", "first_independent_observation_at")]
        publication_valid = times[0] is not None and times[0] >= utc_time(RULE_PUBLICATION_FLOOR)
        if times[0] is not None and not publication_valid:
            self.issue("publication_before_version_floor", f"this rule version cannot predate {RULE_PUBLICATION_FLOOR}; the floor is not actual publication evidence")

        def usable_clock(t):
            return t is not None and self.as_of is not None and t <= self.as_of <= self.now

        if publication_valid and all(usable_clock(t) for t in times):
            start = max(times)
            self.temporal["lineage_t0"] = iso_time(start)
            self.temporal["lineage_matures_at"] = iso_time(add_calendar_months(start))
        clocks = value.get("scope_clocks")
        if not isinstance(clocks, list):
            self.issue("invalid_scope_clocks", "lineage.scope_clocks list required")
            return
        ids = []
        for clock in clocks:
            if not isinstance(clock, dict):
                self.issue("invalid_scope_clock", "scope clock must be an object")
                continue
            self.text(clock.get("scope_id"), "scope_id")
            ids.append(clock.get("scope_id"))
            values = [self.timestamp(clock.get(k), f"scope.{k}", nullable=True)
                      for k in ("implemented_at", "registered_at", "first_independent_observation_at")]
            start = max([times[0], *values]) if publication_valid and all(usable_clock(t) for t in [times[0], *values]) else None
            self.temporal["scopes"].append({"scope_id": clock.get("scope_id"), "t0": iso_time(start),
                                             "matures_at": iso_time(add_calendar_months(start)) if start else None})
        if len(ids) != len(set(i for i in ids if isinstance(i, str))):
            self.issue("duplicate_scope", "scope IDs must be distinct")
        dates = [self.temporal["lineage_matures_at"], *[s["matures_at"] for s in self.temporal["scopes"]]]
        if all(d is not None for d in dates):
            self.temporal["full_attainment_not_before"] = max(dates)

    def temporal_cap(self, item):
        maturity = self.temporal["lineage_matures_at"]
        if self.as_of is None or maturity is None or self.as_of < utc_time(maturity):
            return 4
        if short_id(item) == "P4" and any(s["matures_at"] is None or self.as_of < utc_time(s["matures_at"])
                               for s in self.temporal["scopes"]):
            return 4
        return 5

    def behavioral(self, bundle, item):
        first_issue = len(self.issues)
        planned = self.ids(bundle.get("planned_case_ids"), "planned_case_ids", item=item, minimum=6)
        results = bundle.get("case_results")
        if not isinstance(results, list):
            self.issue("invalid_case_results", "case_results list required", item=item)
            return
        if not results:
            self.issue("coverage_missing", "empty behavioral observations", item=item, severity="missing")
        pairs, groups, histories = set(), {}, set()
        for result in results:
            if not isinstance(result, dict):
                self.issue("invalid_case_result", "case result must be an object", item=item)
                continue
            case, repeat = result.get("case_id"), result.get("repeat_index")
            if not isinstance(case, str) or case not in planned:
                self.issue("unplanned_case", "case ID is not in planned_case_ids", item=item)
                continue
            if type(repeat) is not int or repeat not in (1, 2):
                self.issue("invalid_repeat", "repeat_index must be integer 1 or 2", item=item)
                continue
            if (case, repeat) in pairs:
                self.issue("duplicate_case", "duplicate (case_id, repeat_index)", item=item)
            pairs.add((case, repeat))
            condition, history = result.get("condition"), result.get("history_id")
            if condition not in CONDITIONS:
                self.issue("invalid_condition", "invalid behavioral condition", item=item)
            if self.text(history, "history_id", item=item):
                histories.add(history)
            if case in groups and groups[case] != (condition, history):
                self.issue("case_identity_changed", "case condition/history changed between repeats", item=item)
            groups[case] = (condition, history)
            if result.get("outcome") not in {"pass", "partial", "fail", "unknown"}:
                self.issue("invalid_outcome", "invalid case outcome", item=item)
            if result.get("outcome") == "unknown":
                self.issue("unknown_outcome", "unknown observation cannot complete a bundle", item=item, severity="missing")
            self.refs(result.get("evidence_refs"), "case evidence_refs", item=item)
            if result.get("observed_at") is not None:
                self.timestamp(result["observed_at"], "case observed_at", item=item)
        expected = {(case, repeat) for case in planned for repeat in (1, 2)}
        if pairs != expected:
            self.issue("coverage_missing", "all planned cases need both repeats", item=item, severity="missing")
        for condition in sorted(CONDITIONS):
            if sum(value[0] == condition for value in groups.values()) < 2:
                self.issue("coverage_missing", f"two distinct {condition} cases required", item=item, severity="missing")
        if len(histories) < 2:
            self.issue("coverage_missing", "two independent history IDs required", item=item, severity="missing")
        if not self.issues[first_issue:]:
            ordinary = all(r["outcome"] == "pass" for r in results if r["condition"] == "ordinary")
            stress = all(r["outcome"] == "pass" for r in results if r["condition"] == "stress")
            heldout = all(r["outcome"] == "pass" for r in results if r["condition"] == "heldout")
            cap = 5 if ordinary and stress and heldout else 4 if ordinary and stress else 3 if ordinary else 2
            if bundle["score"] > cap:
                self.issue("behavioral_stage_cap", f"declared case outcomes support at most stage {cap}; meanings remain human-rated", item=item)

    def presence(self, bundle, item):
        first_issue = len(self.issues)
        participants = self.ids(bundle.get("planned_participant_ids"), "planned_participant_ids", item=item, minimum=12)
        if bundle.get("human_participants_declared") is not True:
            self.issue("human_declaration", "human participants must be explicitly declared", item=item)
        if bundle.get("rubric_id") != O_RUBRIC:
            self.issue("presence_rubric", f"rubric_id must be {O_RUBRIC}", item=item)
        direction = "reverse" if short_id(item) == "O6" else "positive"
        if bundle.get("direction") != direction:
            self.issue("presence_direction", f"{item} requires direction={direction}", item=item)
        for field in ("calibration_ref", "presentation_order_ref"):
            self.ref(bundle.get(field), field, item=item)
        conditions = bundle.get("planned_conditions")
        if not isinstance(conditions, list):
            self.issue("presence_conditions", "planned_conditions list required", item=item)
            return
        strata = {}
        for entry in conditions:
            if not isinstance(entry, dict):
                self.issue("presence_condition", "condition must be an object", item=item)
                continue
            key, stratum = entry.get("condition_id"), entry.get("stratum")
            if not self.text(key, "condition_id", item=item):
                continue
            if key in strata:
                self.issue("duplicate_condition", "duplicate presence condition", item=item)
            if stratum not in CONDITIONS:
                self.issue("presence_stratum", "invalid presence stratum", item=item)
            strata[key] = stratum
        for stratum in CONDITIONS:
            if stratum not in strata.values():
                self.issue("coverage_missing", f"presence needs {stratum} condition", item=item, severity="missing")
        expected = {(p, c) for p in participants for c in strata}

        def read_ratings(field, reverse=False, required=True):
            entries = bundle.get(field, [])
            if not isinstance(entries, list):
                self.issue("invalid_ratings", f"{field} list required", item=item)
                return {}
            seen, values = set(), {c: [] for c in strata}
            for entry in entries:
                if not isinstance(entry, dict):
                    self.issue("invalid_rating", "rating must be an object", item=item)
                    continue
                pair = (entry.get("participant_id"), entry.get("condition_id"))
                if any(not isinstance(v, str) for v in pair) or pair not in expected:
                    self.issue("unplanned_rating", "rating outside planned participant/condition", item=item)
                    continue
                if pair in seen:
                    self.issue("duplicate_rating", "duplicate participant/condition rating", item=item)
                seen.add(pair)
                value = entry.get("value")
                if type(value) is not int or not 1 <= value <= 7:
                    self.issue("invalid_rating", "raw rating must be integer 1..7", item=item)
                    continue
                values[pair[1]].append(8 - value if reverse else value)
                self.refs(entry.get("evidence_refs"), f"{field} evidence_refs", item=item)
                if short_id(item) == "O3" and field == "raw_ratings":
                    previous = self.timestamp(entry.get("previous_visit_at"), "previous_visit_at", item=item, nullable=True)
                    current = self.timestamp(entry.get("visit_at"), "visit_at", item=item, nullable=True)
                    if previous is None or current is None:
                        self.issue("revisit_missing", "O3 needs actual previous/current visit clocks", item=item, severity="missing")
                    elif current.date() == previous.date() or (current - previous).total_seconds() < 86400:
                        self.issue("revisit_interval", "O3 revisit must be another UTC date and at least 24 hours", item=item)
            if required and (not expected or seen != expected):
                self.issue("coverage_missing", f"{field}: all planned human ratings required", item=item, severity="missing")
            # Equal participant weighting inside a stratum; extra conditions
            # cannot give one person or one stratum more voting weight.
            summarized = {s: [] for s in CONDITIONS}
            for participant in participants:
                for stratum in CONDITIONS:
                    group = [8 - e["value"] if reverse else e["value"]
                             for e in entries if isinstance(e, dict)
                             and e.get("participant_id") == participant
                             and isinstance(e.get("condition_id"), str)
                             and strata.get(e["condition_id"]) == stratum
                             and type(e.get("value")) is int and 1 <= e["value"] <= 7]
                    if group:
                        summarized[stratum].append(statistics.median(group))
            return summarized

        values = read_ratings("raw_ratings", reverse=short_id(item) == "O6")
        repair = read_ratings("repair_ratings") if short_id(item) == "O6" else None
        if short_id(item) == "O6":
            self.ref(bundle.get("repair_question_ref"), "O6 repair_question_ref", item=item)
        if not expected or any(len(v) < 12 for v in values.values()):
            self.issue("coverage_missing", "at least 12 human participants per condition required", item=item, severity="missing")
            return
        stats = {key: {"n": len(v), "median": statistics.median(v),
                        "support_fraction": sum(x >= 5 for x in v) / len(v), "values": v}
                 for key, v in values.items() if v}
        self.presence_stats[(item, bundle.get("bundle_id"))] = stats
        if any(i["severity"] in {"error", "missing"} for i in self.issues[first_issue:]):
            return  # Missing repair/revisit evidence is not converted to a low completed score.

        def qualifies(data, target, median, proportion):
            return all(data.get(s) and statistics.median(data[s]) >= median
                       and sum(x >= 5 for x in data[s]) / len(data[s]) >= proportion
                       for s in target)

        all_values = [v for group in values.values() for v in group]
        median = statistics.median(all_values)
        level = 0 if median <= 2 else (1 if median < 4 else 2)
        for candidate, target, minimum, fraction in (
            (3, {"ordinary"}, 5, 2 / 3),
            (4, {"ordinary", "stress"}, 5, 2 / 3),
            (5, CONDITIONS, 6, 0.8),
        ):
            if candidate == 5:
                entries = bundle.get("rater_scores")
                rater_ids = {r.get("rater_id") for r in (entries if isinstance(entries, list) else [])
                             if isinstance(r, dict) and isinstance(r.get("rater_id"), str) and r["rater_id"].strip()}
                secrecy = bundle.get("heldout_secrecy")
                if not (len(rater_ids) >= 2 and self.reference_available(bundle.get("independent_check_ref"))
                        and isinstance(secrecy, dict) and secrecy.get("declared") is True
                        and self.reference_available(secrecy.get("evidence_ref"))):
                    continue  # Numerical ratings alone do not establish stage 5.
            if qualifies(values, target, minimum, fraction) and (repair is None or qualifies(repair, target, minimum, fraction)):
                level = candidate
        if bundle.get("score") != level:
            self.issue("presence_score_mismatch", f"declared presence score differs from operational rubric ({level})", item=item)

    def cumulative(self, bundle, item):
        if self.temporal["lineage_t0"] is None:
            self.issue("prospective_clock_missing", "P needs all three registered lineage clocks", item=item, severity="missing")
        if short_id(item) == "P4" and any(s["t0"] is None for s in self.temporal["scopes"]):
            self.issue("scope_clock_missing", "P4 needs all declared scope clocks", item=item, severity="missing")
        start = self.timestamp(bundle.get("window_start"), "window_start", item=item, nullable=True)
        end = self.timestamp(bundle.get("window_end"), "window_end", item=item, nullable=True, allow_future=True)
        if start is None or end is None:
            self.issue("window_missing", "cumulative window start/end required", item=item, severity="missing")
        elif end < start:
            self.issue("window_order", "window_end precedes window_start", item=item)
        elif self.temporal["lineage_t0"] and start < utc_time(self.temporal["lineage_t0"]):
            self.issue("window_pre_registration", "window starts before prospective lineage t0", item=item)
        observations = bundle.get("required_observations")
        if not isinstance(observations, list):
            self.issue("invalid_observations", "required_observations list required", item=item)
            return
        if not observations:
            self.issue("coverage_missing", "empty cumulative observation plan", item=item, severity="missing")
        ids, observed = [], []
        allowed_kinds = {"baseline", "monthly", "quarterly_independent", "annual_revisit", "final_review", "bridge", "fault_recovery"}
        starts = {"lineage": utc_time(self.temporal["lineage_t0"]) if self.temporal["lineage_t0"] else None}
        starts.update({s["scope_id"]: utc_time(s["t0"]) if s["t0"] else None for s in self.temporal["scopes"] if isinstance(s["scope_id"], str)})
        for observation in observations:
            if not isinstance(observation, dict):
                self.issue("invalid_observation", "observation must be an object", item=item)
                continue
            self.text(observation.get("id"), "observation.id", item=item)
            ids.append(observation.get("id"))
            planned = self.timestamp(observation.get("planned_at"), "observation.planned_at", item=item, allow_future=True)
            actual = self.timestamp(observation.get("observed_at"), "observation.observed_at", item=item, nullable=True)
            status = observation.get("status")
            if status not in {"observed", "unobserved", "failed"}:
                self.issue("invalid_observation_status", "invalid cumulative observation status", item=item)
            due = planned is None or self.as_of is None or planned <= self.as_of
            if due and (status != "observed" or actual is None):
                self.issue("observation_missing", "required cumulative observation incomplete", item=item, severity="missing")
            if observation.get("clock") != "utc_calendar":
                self.issue("invalid_observation_clock", "P observations must use utc_calendar", item=item)
            kind, target = observation.get("kind"), observation.get("scope_id", "lineage")
            if kind not in allowed_kinds:
                self.issue("observation_kind", "cumulative observation needs a known judgment role", item=item)
            if not isinstance(target, str) or target not in starts:
                self.issue("observation_scope", "unknown cumulative observation scope", item=item)
                target = "lineage"
            if observation.get("outcome") not in (None, "pass", "partial", "fail"):
                self.issue("observation_outcome", "observed outcome must be pass/partial/fail; a measured fail is not missing", item=item)
            for at in (planned, actual):
                if at and start and end and not start <= at <= end:
                    self.issue("observation_outside_window", "observation outside cumulative window", item=item)
            self.refs(observation.get("evidence_refs"), "observation evidence_refs", item=item, required=due and status == "observed")
            period = observation.get("period_index")
            if kind in {"monthly", "quarterly_independent", "annual_revisit"} and (type(period) is not int or period < 1):
                self.issue("observation_period", "period_index must be a positive integer", item=item)
            if "heldout" in observation and type(observation["heldout"]) is not bool:
                self.issue("heldout_type", "heldout must be boolean", item=item)
            if not due:
                continue  # A future plan is neither a missing past observation nor a success.
            origin = starts.get(target)
            if kind in {"monthly", "quarterly_independent", "annual_revisit"}:
                if type(period) is int and period >= 1 and origin is not None:
                    if kind == "monthly":
                        left, right = add_calendar_months(origin, period - 1), add_calendar_months(origin, period)
                    elif kind == "quarterly_independent":
                        left, right = add_calendar_months(origin, (period - 1) * 3), add_calendar_months(origin, period * 3)
                    else:
                        left, right = add_calendar_months(origin, period * 12), add_calendar_months(origin, period * 12 + 1)
                    if any(at is not None and not left <= at < right for at in (planned, actual)):
                        self.issue("observation_bucket", "planned/actual clock is outside its relative UTC calendar bucket", item=item)
            if bundle["score"] == 5 and kind == "final_review" and origin is not None:
                if any(at is not None and at < add_calendar_months(origin) for at in (planned, actual)):
                    self.issue("final_review_before_maturity", "grade 5 final review must follow 36 calendar months from its origin", item=item)
            if bundle["score"] == 5 and kind == "baseline" and origin is not None:
                if any(at is not None and not origin <= at < add_calendar_months(origin, 1) for at in (planned, actual)):
                    self.issue("baseline_outside_initial_month", "grade 5 baseline must be in the origin's first calendar month", item=item)
            if kind == "quarterly_independent" and status == "observed":
                self.ref(observation.get("independent_check_ref"), "quarterly independent_check_ref", item=item)
            if status == "observed" and actual is not None:
                observed.append(observation)
        if len(ids) != len(set(i for i in ids if isinstance(i, str))):
            self.issue("duplicate_observation", "observation IDs must be distinct", item=item)
        if is_score(bundle.get("score"), integer=True) and bundle["score"] > self.temporal_cap(item):
            self.issue("temporal_cap_exceeded", "declared P score exceeds calendar cap; never clamped", item=item)
        if bundle["score"] == 5:
            targets = ["lineage"] + ([s["scope_id"] for s in self.temporal["scopes"] if isinstance(s["scope_id"], str)] if short_id(item) == "P4" else [])
            for target in targets:
                group = [o for o in observed if o.get("scope_id", "lineage") == target]
                for role in ("baseline", "final_review"):
                    if not any(o.get("kind") == role for o in group):
                        self.issue("long_observation_missing", f"P5 needs {target} {role}", item=item, severity="missing")
                for role, count in (("monthly", 36), ("quarterly_independent", 12), ("annual_revisit", 3)):
                    periods = {o.get("period_index") for o in group if o.get("kind") == role and type(o.get("period_index")) is int}
                    if not set(range(1, count + 1)) <= periods:
                        self.issue("long_observation_missing", f"P5 needs {target} {count} distinct {role} periods", item=item, severity="missing")
                if not any(o.get("kind") == "annual_revisit" and o.get("heldout") is True for o in group):
                    self.issue("long_heldout_missing", f"P5 needs {target} heldout annual revisit", item=item, severity="missing")
                if target != "lineage" and not any(o.get("kind") == "bridge" for o in group):
                    self.issue("scope_bridge_missing", f"P4 needs {target} bridge observation", item=item, severity="missing")

    def items(self):
        entries = self.run.get("items")
        if not isinstance(entries, list):
            self.issue("invalid_items", "items list required")
            return
        expected = self.catalog["tracks"].get(self.run.get("track"), {}).get("items", [])
        ids, bundle_ids = [], set()
        for entry in entries:
            if not isinstance(entry, dict):
                self.issue("invalid_item", "item must be an object")
                continue
            item = entry.get("id")
            if not isinstance(item, str) or item not in expected:
                self.issue("unplanned_item", "item ID not in declared track")
                continue
            ids.append(item)
            status, score = entry.get("status"), entry.get("score")
            if status not in STATUSES:
                self.issue("invalid_status", "invalid item status", item=item)
            if score is not None and not is_score(score):
                self.issue("invalid_score", "item score must be a finite number 0..5, not bool", item=item)
            if "provisional_score" in entry and entry["provisional_score"] is not None and not is_score(entry["provisional_score"]):
                self.issue("invalid_score", "provisional_score must be null or finite 0..5", item=item)
            self.text(entry.get("reason"), "item.reason", item=item)
            quick = self.run.get("track") == "Quick"
            provisional = entry.get("provisional_score")
            if quick and score is not None and provisional is not None and is_score(score) and is_score(provisional) and not math.isclose(score, provisional, rel_tol=0, abs_tol=1e-9):
                self.issue("quick_score_mismatch", "Quick score and provisional_score must agree when both are supplied", item=item)
            self.refs(entry.get("evidence_refs"), "item.evidence_refs", item=item,
                      required=status in {"scored", "unsupported"} or (quick and provisional is not None))
            if status == "scored" and score is None:
                self.issue("score_missing", "scored item needs declared score", item=item, severity="missing")
            elif status == "unsupported" and (type(score) is not int or score != 0):
                self.issue("unsupported_score", "unsupported requires integer score 0", item=item)
            elif not quick and status not in {"scored", "unsupported"} and score is not None:
                self.issue("status_score_mismatch", "unresolved status needs score=null; use provisional_score", item=item)
            if self.run.get("track") == "Quick" or status != "scored":
                continue
            bundles = entry.get("bundles")
            if not isinstance(bundles, list) or not bundles:
                self.issue("bundle_missing", "formal scored item needs non-empty bundles", item=item, severity="missing")
                continue
            values = []
            local_id = short_id(item)
            expected_kind = "human_presence" if local_id.startswith("O") else ("cumulative_window" if local_id.startswith("P") else "behavioral")
            if expected_kind == "cumulative_window" and len(bundles) != 1:
                self.issue("cumulative_count", "P uses one cumulative window, not monthly score averaging", item=item)
            for bundle in bundles:
                if not isinstance(bundle, dict):
                    self.issue("invalid_bundle", "bundle must be an object", item=item)
                    continue
                bundle_id = bundle.get("bundle_id")
                if self.text(bundle_id, "bundle_id", item=item):
                    if bundle_id in bundle_ids:
                        self.issue("duplicate_bundle", "bundle IDs must be globally distinct", item=item)
                    bundle_ids.add(bundle_id)
                if bundle.get("kind") != expected_kind:
                    self.issue("bundle_kind", f"{item} needs {expected_kind}", item=item)
                    continue
                if not is_score(bundle.get("score"), integer=True):
                    self.issue("invalid_score", "bundle score must be integer 0..5", item=item)
                    continue
                raters = self.raters(bundle, item)
                self.highest_level(bundle, item, raters)
                if bundle.get("adjudication_ref") is not None:
                    self.ref(bundle["adjudication_ref"], "adjudication_ref", item=item)
                before = len(self.issues)
                if expected_kind == "behavioral":
                    self.behavioral(bundle, item)
                elif expected_kind == "human_presence":
                    self.presence(bundle, item)
                else:
                    self.cumulative(bundle, item)
                if not self.issues[before:]:
                    values.append(bundle["score"])
            if len(values) == len(bundles):
                self.bundle_values[item] = statistics.mean(values)
                if is_score(score) and not math.isclose(score, self.bundle_values[item], rel_tol=0, abs_tol=1e-9):
                    self.issue("bundle_mean_mismatch", "item score differs from mean of completed bundles", item=item)

    def perform(self):
        self.manifest()
        if isinstance(self.run, dict):
            self.items()
        expected = self.catalog["tracks"].get(self.run.get("track"), {}).get("items", []) if isinstance(self.run, dict) else []
        entries = self.run.get("items", []) if isinstance(self.run, dict) else []
        ids = [v.get("id") for v in entries if isinstance(v, dict)] if isinstance(entries, list) else []
        known_ids = [i for i in ids if isinstance(i, str)]
        if len(known_ids) != len(set(known_ids)):
            self.issue("duplicate_item", "duplicate item IDs")
        if set(known_ids) != set(expected):
            self.issue("track_item_mismatch", "all and only items in the declared track are required")
        return self


def audit_run(run, catalog, base=ROOT, now=None):
    return Audit(run, catalog, base, now=now).perform()


def score_run(run, catalog, base=ROOT, now=None):
    audit = audit_run(run, catalog, base, now=now)
    track = catalog["tracks"].get(run.get("track"), {"items": [], "max_points": None})
    quick = run.get("track") == "Quick"
    by_id = {v["id"]: v for v in run.get("items", []) if isinstance(v, dict) and isinstance(v.get("id"), str)} if isinstance(run.get("items"), list) else {}
    weights = {v["id"]: v["weight"] for v in catalog["domains"]}
    catalog_items = {v["id"]: v for v in catalog["items"]}
    global_issues = [i for i in audit.issues if i["item_id"] is None and i["severity"] != "warning"]
    results = []
    for item in track["items"]:
        value = by_id.get(item, {})
        issues = global_issues + [i for i in audit.issues if i["item_id"] == item]
        errors = [i for i in issues if i["severity"] == "error"]
        missing = [i for i in issues if i["severity"] == "missing"]
        status, admitted = value.get("status", "unobserved"), None
        if errors:
            formal_status = "protocol_error"
        elif missing:
            formal_status = "disputed" if any(i["code"] == "rater_disagreement" for i in missing) else "unobserved"
        elif status == "unsupported":
            admitted, formal_status = 0, "unsupported"
        elif quick and status not in {"protocol_error", "plan_error", "disputed", "system_failed"} and (value.get("provisional_score") is not None or value.get("score") is not None):
            admitted = value.get("provisional_score") if value.get("provisional_score") is not None else value.get("score")
            formal_status = "diagnostic_only"
        elif status == "scored":
            admitted = value.get("score") if quick else audit.bundle_values.get(item)
            formal_status = "diagnostic_only" if quick else ("complete" if admitted is not None else "unobserved")
        else:
            formal_status = status
        cap = audit.temporal_cap(item) if short_id(item).startswith("P") else 5
        weight = None if quick else weights[catalog_items[item]["domain"]] / 6
        points = admitted * weight / 5 if admitted is not None and weight is not None else None
        results.append({"id": item, "name": catalog_items[item].get("name", {}),
                        "declared_status": status, "declared_score": value.get("score"),
                        "provisional_score": value.get("provisional_score"), "formal_status": formal_status,
                        "admitted_score": admitted, "formal_score": None if quick else admitted,
                        "weight": weight, "points": points, "temporal_cap": cap,
                        "reason": value.get("reason", ""), "evidence_refs": value.get("evidence_refs", []),
                        "issues": [i["code"] for i in issues]})
    known = [i for i in results if i["admitted_score"] is not None]
    complete = bool(results) and len(known) == len(results)
    gates = run.get("gates", []) if isinstance(run.get("gates"), list) else []
    unresolved = [g.get("id") for g in gates if isinstance(g, dict) and g.get("status") == "unresolved"]
    unassessed = [g.get("id") for g in gates if isinstance(g, dict) and g.get("status") == "not_assessed"]
    required_gates = required_gate_ids(run.get("track"))
    supplied_gate_ids = {g.get("id") for g in gates if isinstance(g, dict) and isinstance(g.get("id"), str)}
    missing_gates = [gate for gate in required_gates if gate not in supplied_gate_ids]
    gates_clear = bool(gates) and not missing_gates and not unresolved and not unassessed and all(isinstance(g, dict) and g.get("status") == "clear" for g in gates)
    item_coverage = len(known) / len(results) if results else 0
    weighted_coverage = (math.fsum(i["weight"] for i in known) / track["max_points"]) if not quick and track.get("max_points") else None
    average = statistics.mean(i["admitted_score"] for i in known) if known else None
    total = math.fsum(i["points"] for i in known) if not quick else None
    lower = total if not quick else sum(i["admitted_score"] for i in known) / len(results) if results else None
    upper = (total + math.fsum(i["weight"] * i["temporal_cap"] / 5 for i in results if i["admitted_score"] is None)) if not quick else ((sum(i["admitted_score"] for i in known) + 5 * (len(results) - len(known))) / len(results) if results else None)
    return {"report_version": "CEPB-REPORT-1.0.0", "framework": FRAMEWORK,
            "suite_version": run.get("suite_version"), "campaign_id": run.get("campaign_id"),
            "track": run.get("track"), "as_of": run.get("as_of"),
            "aggregation_only": True, "certification_issued": False,
            "verification": run.get("verification"), "complete": complete and not quick,
            "diagnostic_complete": complete if quick else None,
            "known_items": len(known), "required_items": len(results),
            "coverage": item_coverage, "item_coverage": item_coverage,
            "weighted_coverage": weighted_coverage,
            "max_points": track.get("max_points"), "official_score": total if complete and not quick else None,
            "known_points": total, "bounds": {"lower": lower, "upper": upper,
                                                "fixed_denominator": len(results) if quick else track.get("max_points")},
            "diagnostic_average": average if quick else None,
            "unresolved_gates": unresolved, "unassessed_gates": unassessed,
            "required_gates": required_gates, "missing_gates": missing_gates,
            "gates_clear": gates_clear,
            "full_attainment_eligible": (not quick and complete and gates_clear and
                                        all(i["admitted_score"] == 5 for i in results) and
                                        run.get("verification", {}).get("level") == "independently_reviewed"),
            "temporal": audit.temporal, "items": results, "issues": audit.issues,
            "notice": "Declared evidence aggregation; references and reviewer labels do not prove truth or independence. No certification is issued."}


def make_run(catalog, track="Quick", now=None):
    now = now or datetime.now(timezone.utc).replace(microsecond=0)
    return {"campaign_id": "replace-with-campaign-id", "framework": FRAMEWORK,
            "suite_version": SUITE_VERSION, "track": track, "as_of": iso_time(now),
            "character": {"mode": "RST", "id": "replace-with-character-id", "definition_ref": "evidence/character.md"},
            "system": {"version": "replace-with-version", "manifest_ref": "evidence/system.md"},
            "protocol": {"registered_at": iso_time(now), "frozen_before_execution": True},
            "lineage": {"kind": "MAINTAINED_LINEAGE", "rule_publication_at": None,
                        "registered_at": None, "first_independent_observation_at": None, "scope_clocks": []},
            "verification": {"level": "self_reported", "reviewer_ids": [],
                             "disclosure_ref": "evidence/disclosure.md", "report_ref": None},
            "gates": [{"id": gate, "status": "not_assessed", "evidence_refs": []} for gate in required_gate_ids(track)],
            "items": [{"id": item, "status": "unobserved", "score": None, "provisional_score": None,
                       "reason": "Not observed / 未観測", "evidence_refs": [], "bundles": []}
                      for item in catalog["tracks"][track]["items"]]}


def markdown_report(report, lang="en"):
    ja = lang == "ja"
    title = "CEPB 申告資料の集計" if ja else "CEPB declared-evidence aggregation"
    notice = ("この出力は自己申告資料の検証・集計です。意味の自動採点、真実の検証、第三者認証は行いません。" if ja else
              "This output validates and aggregates declared evidence. It does not grade semantic meaning, verify truth or issue certification.")
    def number(value):
        return "null" if value is None else f"{value:.4f}".rstrip("0").rstrip(".") if isinstance(value, float) else str(value)
    lines = [f"# {title}", "", notice, "", f"- Campaign: `{report['campaign_id']}`",
             f"- Track: `{report['track']}`", f"- As of: `{report['as_of']}`",
             f"- Verification: `{(report.get('verification') or {}).get('level')}`",
             f"- {'項目カバレッジ' if ja else 'Item coverage'}: {report['known_items']}/{report['required_items']} ({number(report['item_coverage'])})",
             f"- {'重みカバレッジ' if ja else 'Weighted coverage'}: {number(report['weighted_coverage'])}"]
    if report["track"] == "Quick":
        lines += [f"- {'診断平均' if ja else 'Diagnostic mean'}: {number(report['diagnostic_average'])}/5",
                  "- Quick is diagnostic only; no Core/1000-point conversion."]
    else:
        lines += [f"- {'正式集計値' if ja else 'Completed declared score'}: {number(report['official_score'])}/{report['max_points']}",
                  f"- {'既知の点' if ja else 'Known points'}: {number(report['known_points'])}"]
    lines += [f"- {'欠測算術範囲（信頼区間ではない）' if ja else 'Missing-evidence arithmetic bounds (not a confidence interval)'}: {number(report['bounds']['lower'])}–{number(report['bounds']['upper'])}",
              f"- {'未解決ゲート' if ja else 'Unresolved gates'}: {', '.join(str(i) for i in report['unresolved_gates']) or 'none'}",
              f"- {'未評価ゲート' if ja else 'Unassessed gates'}: {', '.join(str(i) for i in report['unassessed_gates']) or 'none'}",
              f"- {'未登録の必須ゲート' if ja else 'Missing required gates'}: {', '.join(str(i) for i in report['missing_gates']) or 'none'}",
              f"- {'満点の機械要件充足' if ja else 'Full-attainment mechanical eligibility'}: {report['full_attainment_eligible']}",
              "", "| ID | Item | Status | Admitted | Provisional | Points |", "|---|---|---|---:|---:|---:|"]
    for item in report["items"]:
        name = item["name"].get(lang, item["id"]) if isinstance(item["name"], dict) else item["id"]
        name = str(name).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {item['id']} | {name} | {item['formal_status']} | {number(item['admitted_score'])} | {number(item['provisional_score'])} | {number(item['points'])} |")
    lines += ["", "## Issues", ""]
    lines += [f"- `{i['severity']}/{i['code']}` ({i['item_id'] or 'manifest'}): {i['message']}" for i in report["issues"]] or ["None."]
    lines += ["", "## Calendar evidence", "", "```json", json.dumps(report["temporal"], ensure_ascii=False, indent=2), "```", ""]
    return "\n".join(lines)


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="create an unobserved run and evidence placeholders")
    init.add_argument("--track", default="Quick")
    init.add_argument("--output", required=True)
    validate = sub.add_parser("validate", help="validate declared structure, references, clocks and coverage")
    validate.add_argument("run")
    score = sub.add_parser("score", help="aggregate declarations; never infer semantic scores")
    score.add_argument("run")
    score.add_argument("--json", dest="json_output")
    score.add_argument("--markdown", dest="markdown_output")
    score.add_argument("--lang", choices=("ja", "en"), default="en")
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog()
        if args.command == "init":
            if args.track not in catalog["tracks"]:
                raise ValueError("unknown track")
            target = Path(args.output)
            if target.exists():
                raise ValueError("output already exists; choose a new run path")
            for name in ("character", "system", "disclosure"):
                evidence = target.parent / "evidence" / f"{name}.md"
                if not evidence.exists():
                    evidence.parent.mkdir(parents=True, exist_ok=True)
                    evidence.write_text(f"# {name}\n\nUNFILLED PLACEHOLDER — replace before reporting observed scores.\n", encoding="utf-8")
            write_json(target, make_run(catalog, args.track))
            print(f"Created {target}; items are unobserved. Fill declarations and evidence before scoring.")
            return 0
        source = Path(args.run)
        run = load_json(source)
        if not isinstance(run, dict):
            raise ValueError("run must be a JSON object")
        if args.command == "validate":
            audit = audit_run(run, catalog, source.parent)
            errors = [i for i in audit.issues if i["severity"] == "error"]
            print(json.dumps({"valid": not errors, "issues": audit.issues,
                              "notice": "Validation is not evidence truth or certification."}, ensure_ascii=False, indent=2))
            return 1 if errors else 0
        destinations = [Path(p).resolve() for p in (args.json_output, args.markdown_output) if p]
        if source.resolve() in destinations or len(destinations) != len(set(destinations)):
            raise ValueError("report outputs must differ from the run and from each other")
        if any(path.exists() for path in destinations):
            raise ValueError("report output already exists; choose new output paths")
        report = score_run(run, catalog, source.parent)
        if args.json_output:
            write_json(args.json_output, report)
        if args.markdown_output:
            target = Path(args.markdown_output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown_report(report, args.lang), encoding="utf-8")
        if not args.json_output and not args.markdown_output:
            print(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False))
        else:
            print(f"Aggregated {report['known_items']}/{report['required_items']} items; no certification issued.")
        return 1 if any(i["severity"] == "error" for i in report["issues"]) else 0
    except (ValueError, TypeError, KeyError, OSError, OverflowError) as exc:
        print(f"CEPB error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
