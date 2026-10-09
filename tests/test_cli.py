"""Pure local unittest coverage. Fixtures are explicitly fictional, never Yui data."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE))
import cepb

AS_OF = cepb.utc_time("2029-10-10T12:00:00Z")  # Injected test clock, never real elapsed evidence.
START = cepb.utc_time(cepb.RULE_PUBLICATION_FLOOR)
REFERENCE = "evidence/synthetic.md"


def behavioral_bundle(item, score=5):
    planned, results = [], []
    for condition in ("ordinary", "stress", "heldout"):
        for index in (1, 2):
            case = f"{item}_{condition}_{index}"
            planned.append(case)
            for repeat in (1, 2):
                results.append({"case_id": case, "condition": condition, "repeat_index": repeat,
                                "history_id": f"fictional_history_{index}", "outcome": "pass",
                                "evidence_refs": [REFERENCE]})
    return {"kind": "behavioral", "bundle_id": f"fictional_{item}_bundle", "score": score,
            "planned_case_ids": planned, "case_results": results,
            "rater_scores": [{"rater_id": "fictional_rater_1", "score": score},
                             {"rater_id": "fictional_rater_2", "score": score}],
            "independent_check_ref": REFERENCE,
            "heldout_secrecy": {"declared": True, "evidence_ref": REFERENCE}}


def presence_bundle(item, score=5):
    local_id = cepb.short_id(item)
    people = [f"fictional_person_{i:02}" for i in range(1, 13)]
    conditions = [{"condition_id": s, "stratum": s} for s in ("ordinary", "stress", "heldout")]
    ratings = []
    for participant in people:
        for condition in conditions:
            row = {"participant_id": participant, "condition_id": condition["condition_id"],
                   "value": 2 if local_id == "O6" else 6, "evidence_refs": [REFERENCE]}
            if local_id == "O3":
                row.update(previous_visit_at="2029-10-08T10:00:00Z", visit_at="2029-10-10T10:00:00Z")
            ratings.append(row)
    bundle = {"kind": "human_presence", "bundle_id": f"fictional_{item}_bundle", "score": score,
              "rubric_id": cepb.O_RUBRIC, "direction": "reverse" if local_id == "O6" else "positive",
              "human_participants_declared": True, "planned_participant_ids": people,
              "planned_conditions": conditions, "raw_ratings": ratings,
              "calibration_ref": REFERENCE, "presentation_order_ref": REFERENCE,
              "rater_scores": [{"rater_id": "fictional_rater_1", "score": score},
                               {"rater_id": "fictional_rater_2", "score": score}],
              "independent_check_ref": REFERENCE,
              "heldout_secrecy": {"declared": True, "evidence_ref": REFERENCE}}
    if local_id == "O6":
        bundle["repair_ratings"] = [{**row, "value": 6} for row in ratings]
        bundle["repair_question_ref"] = REFERENCE
    return bundle


def cumulative_bundle(item, score=5):
    observations = []
    def add(role, at, index=None, heldout=False):
        row = {"id": f"fictional_{role}_{index or 0}", "kind": role, "planned_at": cepb.iso_time(at),
               "observed_at": cepb.iso_time(at), "status": "observed", "clock": "utc_calendar", "evidence_refs": [REFERENCE]}
        if index is not None:
            row["period_index"] = index
        if role == "quarterly_independent":
            row["independent_check_ref"] = REFERENCE
        if heldout:
            row["heldout"] = True
        observations.append(row)
    add("baseline", START)
    for index in range(1, 37):
        add("monthly", cepb.add_calendar_months(START, index - 1) + timedelta(days=1), index)
    for index in range(1, 13):
        add("quarterly_independent", cepb.add_calendar_months(START, (index - 1) * 3) + timedelta(days=1), index)
    for index in range(1, 4):
        add("annual_revisit", cepb.add_calendar_months(START, index * 12), index, heldout=index == 3)
    add("final_review", AS_OF)
    return {"kind": "cumulative_window", "bundle_id": f"fictional_{item}_window", "score": score,
            "window_start": cepb.iso_time(START), "window_end": cepb.iso_time(AS_OF),
            "required_observations": observations,
            "rater_scores": [{"rater_id": "fictional_rater_1", "score": score},
                             {"rater_id": "fictional_rater_2", "score": score}],
            "independent_check_ref": REFERENCE}


def fictional_run(catalog, track="Core", complete=True):
    run = cepb.make_run(catalog, track, AS_OF)
    run.update(campaign_id=f"fictional_{track.lower()}_fixture", synthetic_example=True,
               description="FICTIONAL SYNTHETIC FIXTURE. No actual character, human participants, independent review or 36-month study. Tests arithmetic only.")
    run["character"].update(id="fictional_character", definition_ref=REFERENCE)
    run["system"].update(version="fictional_system_v1", manifest_ref=REFERENCE)
    run["verification"]["disclosure_ref"] = REFERENCE
    run["protocol"]["registered_at"] = cepb.iso_time(START)
    run["gates"] = [{"id": gate, "status": "clear", "evidence_refs": [REFERENCE]} for gate in cepb.required_gate_ids(track)]
    run["lineage"].update(rule_publication_at=cepb.iso_time(START),
                         registered_at=cepb.iso_time(START),
                         first_independent_observation_at=cepb.iso_time(START))
    if complete:
        for item in run["items"]:
            item.update(status="scored", score=5, reason="Fictional complete fixture, not measured evidence.", evidence_refs=[REFERENCE])
            if track == "Quick":
                item["provisional_score"] = 5
            elif cepb.short_id(item["id"]).startswith("O"):
                item["bundles"] = [presence_bundle(item["id"])]
            elif cepb.short_id(item["id"]).startswith("P"):
                item["bundles"] = [cumulative_bundle(item["id"])]
            else:
                item["bundles"] = [behavioral_bundle(item["id"])]
    return run


class TestCEPB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = cepb.load_catalog()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        (self.base / "evidence").mkdir()
        (self.base / REFERENCE).write_text("FICTIONAL test evidence; no real observations.\n", encoding="utf-8")

    def score(self, run):
        return cepb.score_run(run, self.catalog, self.base, now=AS_OF)

    def item(self, run, item="A1"):
        return next(i for i in run["items"] if cepb.short_id(i["id"]) == cepb.short_id(item))

    def result(self, report, item="A1"):
        return next(i for i in report["items"] if cepb.short_id(i["id"]) == cepb.short_id(item))

    def codes(self, report):
        return {i["code"] for i in report["issues"]}

    def test_core_maximum_590_is_declared_not_certified(self):
        report = self.score(fictional_run(self.catalog))
        self.assertEqual(report["issues"], [])
        self.assertEqual(report["official_score"], 590)
        self.assertEqual(report["required_items"], 54)
        self.assertTrue(report["complete"])
        self.assertFalse(report["certification_issued"])
        self.assertFalse(report["full_attainment_eligible"])

    def test_integrated_maximum_1000_and_independent_label_not_certification(self):
        run = fictional_run(self.catalog, "Integrated")
        run["verification"].update(level="independently_reviewed", reviewer_ids=["fictional_reviewer_1", "fictional_reviewer_2"], report_ref=REFERENCE)
        report = self.score(run)
        self.assertEqual(report["issues"], [])
        self.assertEqual(report["official_score"], 1000)
        self.assertEqual(report["required_items"], 96)
        self.assertTrue(report["full_attainment_eligible"])
        self.assertFalse(report["certification_issued"])

    def test_catalog_track_totals(self):
        expected = {"Core": 590, "Voice": 660, "Avatar": 660, "Multimodal": 790, "World": 720, "Integrated": 1000}
        self.assertEqual({k: self.catalog["tracks"][k]["max_points"] for k in expected}, expected)

    def test_unknown_item_keeps_fixed_denominator_bounds(self):
        run = fictional_run(self.catalog)
        self.item(run).update(status="unobserved", score=None, provisional_score=4, evidence_refs=[], bundles=[])
        report = self.score(run)
        self.assertIsNone(report["official_score"])
        self.assertFalse(report["complete"])
        self.assertEqual(report["known_items"], 53)
        self.assertAlmostEqual(report["bounds"]["lower"], 590 - 80 / 6)
        self.assertEqual(report["bounds"]["upper"], 590)
        self.assertEqual(report["bounds"]["fixed_denominator"], 590)
        self.assertEqual(self.result(report)["provisional_score"], 4)

    def test_unsupported_is_known_zero_not_missing(self):
        run = fictional_run(self.catalog)
        self.item(run).update(status="unsupported", score=0, bundles=[])
        report = self.score(run)
        self.assertTrue(report["complete"])
        self.assertEqual(self.result(report)["formal_score"], 0)
        self.assertAlmostEqual(report["official_score"], 590 - 80 / 6)

    def test_unsupported_needs_zero_and_evidence(self):
        run = fictional_run(self.catalog)
        self.item(run).update(status="unsupported", score=3, evidence_refs=[])
        report = self.score(run)
        self.assertIn("unsupported_score", self.codes(report))
        self.assertIsNone(self.result(report)["formal_score"])

    def test_empty_and_partial_behavioral_bundles_are_missing(self):
        for alteration in ("empty", "partial", "unknown"):
            with self.subTest(alteration=alteration):
                run = fictional_run(self.catalog)
                item = self.item(run)
                if alteration == "empty":
                    item["bundles"] = []
                elif alteration == "partial":
                    item["bundles"][0]["case_results"].pop()
                else:
                    item["bundles"][0]["case_results"][0]["outcome"] = "unknown"
                report = self.score(run)
                self.assertIsNone(self.result(report)["formal_score"])
                self.assertEqual(self.result(report)["formal_status"], "unobserved")

    def test_behavioral_duplicate_case_pair_rejected(self):
        run = fictional_run(self.catalog)
        bundle = self.item(run)["bundles"][0]
        bundle["case_results"].append(copy.deepcopy(bundle["case_results"][0]))
        report = self.score(run)
        self.assertIn("duplicate_case", self.codes(report))
        self.assertEqual(self.result(report)["formal_status"], "protocol_error")

    def test_behavioral_history_and_condition_cannot_change_on_repeat(self):
        run = fictional_run(self.catalog)
        self.item(run)["bundles"][0]["case_results"][1]["history_id"] = "changed"
        self.assertIn("case_identity_changed", self.codes(self.score(run)))

    def test_score5_rejects_partial_fail_missing_independent_and_same_rater(self):
        for alteration in ("partial", "fail", "independent", "rater", "heldout"):
            with self.subTest(alteration=alteration):
                run = fictional_run(self.catalog)
                bundle = self.item(run)["bundles"][0]
                if alteration in {"partial", "fail"}:
                    bundle["case_results"][-1]["outcome"] = alteration
                elif alteration == "independent":
                    bundle.pop("independent_check_ref")
                elif alteration == "rater":
                    bundle["rater_scores"][1]["rater_id"] = bundle["rater_scores"][0]["rater_id"]
                else:
                    bundle["heldout_secrecy"]["declared"] = False
                report = self.score(run)
                self.assertEqual(self.result(report)["formal_status"], "protocol_error")

    def test_stage3_and_4_caps_use_declared_pass_conditions(self):
        for condition, score in (("ordinary", 3), ("stress", 4)):
            run = fictional_run(self.catalog)
            item = self.item(run)
            item.update(score=score, bundles=[behavioral_bundle("A1", score)])
            next(r for r in item["bundles"][0]["case_results"] if r["condition"] == condition)["outcome"] = "fail"
            self.assertIn("behavioral_stage_cap", self.codes(self.score(run)))

    def test_rater_disagreement_needs_adjudication_and_preserves_scores(self):
        run = fictional_run(self.catalog)
        bundle = self.item(run)["bundles"][0]
        bundle["rater_scores"][1]["score"] = 4
        report = self.score(run)
        self.assertEqual(self.result(report)["formal_status"], "disputed")
        self.assertIsNone(self.result(report)["formal_score"])
        bundle["adjudication_ref"] = REFERENCE
        self.assertEqual(self.result(self.score(run))["formal_score"], 5)
        self.assertEqual(bundle["rater_scores"][1]["score"], 4)

    def test_completed_bundle_means_are_not_rounded_to_ordinal_scores(self):
        run = fictional_run(self.catalog)
        item = self.item(run)
        a, b = behavioral_bundle("A1", 3), behavioral_bundle("A1", 4)
        b["bundle_id"] += "_second"
        item.update(score=3.5, bundles=[a, b])
        self.assertEqual(self.result(self.score(run))["formal_score"], 3.5)
        item["score"] = 4
        self.assertIn("bundle_mean_mismatch", self.codes(self.score(run)))

    def test_bool_nan_out_of_range_scores_are_rejected(self):
        for value in (True, False, float("nan"), float("inf"), -1, 6, "5"):
            with self.subTest(value=str(value)):
                run = fictional_run(self.catalog)
                self.item(run)["score"] = value
                report = self.score(run)
                self.assertIn("invalid_score", self.codes(report))
                self.assertIsNone(self.result(report)["formal_score"])

    def test_duplicate_item_and_bundle_ids_are_rejected(self):
        run = fictional_run(self.catalog)
        run["items"].append(copy.deepcopy(run["items"][0]))
        self.assertIn("duplicate_item", self.codes(self.score(run)))
        run = fictional_run(self.catalog)
        run["items"][1]["bundles"][0]["bundle_id"] = run["items"][0]["bundles"][0]["bundle_id"]
        self.assertIn("duplicate_bundle", self.codes(self.score(run)))

    def test_quick_uses_provisional_without_formal_points_or_conversion(self):
        run = fictional_run(self.catalog, "Quick", complete=False)
        self.item(run).update(provisional_score=3, evidence_refs=[REFERENCE])
        report = self.score(run)
        self.assertEqual(report["diagnostic_average"], 3)
        self.assertEqual(report["known_items"], 1)
        self.assertAlmostEqual(report["coverage"], 1 / 18)
        self.assertIsNone(report["max_points"])
        self.assertIsNone(report["official_score"])
        self.assertIsNone(self.result(report)["formal_score"])
        self.assertAlmostEqual(report["bounds"]["lower"], 3 / 18)

    def test_quick_both_values_must_agree(self):
        run = fictional_run(self.catalog, "Quick")
        self.item(run)["provisional_score"] = 4
        self.assertIn("quick_score_mismatch", self.codes(self.score(run)))

    def test_quick_cannot_be_relabelled_as_core(self):
        run = fictional_run(self.catalog, "Quick")
        run["track"] = "Core"
        report = self.score(run)
        self.assertIn("track_item_mismatch", self.codes(report))
        self.assertIsNone(report["official_score"])

    def test_gates_flag_unresolved_and_not_assessed_without_erasing_numeric_declarations(self):
        for status in ("unresolved", "not_assessed"):
            run = fictional_run(self.catalog)
            run["gates"][0]["status"] = status
            report = self.score(run)
            self.assertEqual(report["official_score"], 590)
            self.assertFalse(report["gates_clear"])
            self.assertFalse(report["full_attainment_eligible"])

    def test_future_as_of_and_lineage_clock_rejected(self):
        run = fictional_run(self.catalog)
        run["as_of"] = "2030-01-01T00:00:00Z"
        self.assertIn("future_as_of", self.codes(self.score(run)))
        run = fictional_run(self.catalog)
        run["lineage"]["registered_at"] = "2030-01-01T00:00:00Z"
        self.assertIn("future_clock", self.codes(self.score(run)))

    def test_publication_floor_is_version_bound_not_publication_evidence(self):
        run = fictional_run(self.catalog)
        run["lineage"]["rule_publication_at"] = "2020-01-01T00:00:00Z"
        self.assertIn("publication_before_version_floor", self.codes(self.score(run)))
        run["lineage"]["rule_publication_at"] = None
        run["lineage"]["scope_clocks"] = [{"scope_id": "voice", "implemented_at": "2020-01-01T00:00:00Z",
                                           "registered_at": "2020-01-01T00:00:00Z", "first_independent_observation_at": "2020-01-01T00:00:00Z"}]
        self.assertIsNone(self.score(run)["temporal"]["scopes"][0]["t0"])

    def test_36_calendar_month_cap_is_not_clamped(self):
        run = fictional_run(self.catalog, "Integrated")
        run["lineage"].update(rule_publication_at="2028-01-01T00:00:00Z", registered_at="2028-01-01T00:00:00Z",
                             first_independent_observation_at="2028-01-01T00:00:00Z")
        report = self.score(run)
        self.assertIn("temporal_cap_exceeded", self.codes(report))
        self.assertIsNone(self.result(report, "P1")["formal_score"])
        self.assertEqual(self.result(report, "P1")["declared_score"], 5)

    def test_missing_prospective_clock_and_empty_p_observations_are_null(self):
        for alteration in ("clock", "empty"):
            run = fictional_run(self.catalog, "Integrated")
            item = self.item(run, "P1")
            item.update(score=4, provisional_score=4, bundles=[cumulative_bundle("P1", 4)])
            if alteration == "clock":
                run["lineage"]["registered_at"] = None
            else:
                item["bundles"][0]["required_observations"] = []
            report = self.score(run)
            self.assertIsNone(self.result(report, "P1")["formal_score"])
            self.assertEqual(self.result(report, "P1")["provisional_score"], 4)

    def test_new_scope_p4_cap_and_publication_floor(self):
        run = fictional_run(self.catalog, "Integrated")
        run["lineage"]["scope_clocks"] = [{"scope_id": "new_voice", "implemented_at": "2029-01-01T00:00:00Z",
                                           "registered_at": "2029-02-01T00:00:00Z", "first_independent_observation_at": "2029-03-01T00:00:00Z"}]
        item = self.item(run, "P4")
        item.update(score=4, bundles=[cumulative_bundle("P4", 4)])
        report = self.score(run)
        self.assertAlmostEqual(report["official_score"], 1000 - (50 / 6) / 5)
        self.assertFalse(report["full_attainment_eligible"])
        self.assertEqual(report["temporal"]["full_attainment_not_before"], "2032-03-01T00:00:00Z")
        run["lineage"]["scope_clocks"][0].update(implemented_at="2020-01-01T00:00:00Z", registered_at="2020-01-01T00:00:00Z",
                                               first_independent_observation_at="2020-01-01T00:00:00Z")
        self.assertEqual(self.score(run)["temporal"]["scopes"][0]["t0"], cepb.RULE_PUBLICATION_FLOOR)

    def test_calendar_leap_and_end_month_rules(self):
        for source, months, expected in (("2024-02-29T12:00:00Z", 36, "2027-02-28T12:00:00Z"),
                                         ("2024-02-29T12:00:00Z", 48, "2028-02-29T12:00:00Z"),
                                         ("2023-01-31T12:00:00Z", 36, "2026-01-31T12:00:00Z"),
                                         ("2023-10-31T12:00:00Z", 1, "2023-11-30T12:00:00Z")):
            self.assertEqual(cepb.iso_time(cepb.add_calendar_months(cepb.utc_time(source), months)), expected)

    def test_p_observed_clock_future_and_simulation_are_rejected(self):
        run = fictional_run(self.catalog, "Integrated")
        observation = self.item(run, "P1")["bundles"][0]["required_observations"][0]
        observation["observed_at"] = "2030-01-01T00:00:00Z"
        self.assertIn("future_clock", self.codes(self.score(run)))
        observation.update(observed_at=cepb.RULE_PUBLICATION_FLOOR, clock="simulation")
        self.assertIn("invalid_observation_clock", self.codes(self.score(run)))

    def test_single_record_cannot_complete_p5_and_same_month_cannot_replace_36_months(self):
        run = fictional_run(self.catalog, "Integrated")
        bundle = self.item(run, "P1")["bundles"][0]
        bundle["required_observations"] = bundle["required_observations"][:1]
        self.assertIn("long_observation_missing", self.codes(self.score(run)))
        run = fictional_run(self.catalog, "Integrated")
        bundle = self.item(run, "P1")["bundles"][0]
        for observation in bundle["required_observations"]:
            if observation["kind"] == "monthly":
                observation["observed_at"] = cepb.iso_time(START + timedelta(days=1))
        self.assertIn("observation_bucket", self.codes(self.score(run)))

    def test_future_plan_is_not_missing_and_observed_failure_is_not_hidden(self):
        run = fictional_run(self.catalog, "Integrated")
        item = self.item(run, "P1")
        bundle = cumulative_bundle("P1", 1)
        item.update(score=1, bundles=[bundle])
        bundle["required_observations"] = bundle["required_observations"][:1]
        bundle["required_observations"][0]["outcome"] = "fail"
        bundle["window_end"] = "2031-01-01T00:00:00Z"
        bundle["required_observations"].append({"id": "future_plan", "kind": "monthly", "period_index": 50,
            "planned_at": "2030-12-10T15:00:00Z", "observed_at": None, "status": "unobserved", "clock": "utc_calendar", "evidence_refs": []})
        report = self.score(run)
        self.assertEqual(self.result(report, "P1")["formal_score"], 1)
        self.assertNotIn("observation_missing", self.result(report, "P1")["issues"])

    def test_presence_requires_humans_raw_ratings_and_correct_operational_stage(self):
        run = fictional_run(self.catalog, "Integrated")
        self.item(run, "O1")["bundles"][0]["raw_ratings"].pop()
        self.assertIsNone(self.result(self.score(run), "O1")["formal_score"])
        run = fictional_run(self.catalog, "Integrated")
        for row in self.item(run, "O1")["bundles"][0]["raw_ratings"]:
            row["value"] = 5
        self.assertIn("presence_score_mismatch", self.codes(self.score(run)))

    def test_o6_reverse_without_separate_repair_is_missing(self):
        run = fictional_run(self.catalog, "Integrated")
        self.item(run, "O6")["bundles"][0].pop("repair_ratings")
        report = self.score(run)
        self.assertEqual(self.result(report, "O6")["formal_status"], "unobserved")
        self.assertIsNone(self.result(report, "O6")["formal_score"])

    def test_o3_requires_actual_revisit_of_24_hours(self):
        run = fictional_run(self.catalog, "Integrated")
        row = self.item(run, "O3")["bundles"][0]["raw_ratings"][0]
        row["previous_visit_at"] = "2029-10-10T09:00:00Z"
        self.assertIn("revisit_interval", self.codes(self.score(run)))

    def test_presence_extra_conditions_do_not_overweight_a_stratum(self):
        run = fictional_run(self.catalog, "Integrated")
        item = self.item(run, "O1")
        item.update(score=4)
        bundle = item["bundles"][0]
        bundle.update(score=4)
        for rater in bundle["rater_scores"]:
            rater["score"] = 4
        for row in bundle["raw_ratings"]:
            if row["condition_id"] == "heldout":
                row["value"] = 4
        for number in range(5):
            condition = f"ordinary_extra_{number}"
            bundle["planned_conditions"].append({"condition_id": condition, "stratum": "ordinary"})
            for person in bundle["planned_participant_ids"]:
                bundle["raw_ratings"].append({"participant_id": person, "condition_id": condition, "value": 7, "evidence_refs": [REFERENCE]})
        self.assertEqual(self.result(self.score(run), "O1")["formal_score"], 4)

    def test_presence_high_ratings_without_stage5_evidence_support_stage4(self):
        run = fictional_run(self.catalog, "Integrated")
        item = self.item(run, "O1")
        item["score"] = 4
        bundle = item["bundles"][0]
        bundle.update(score=4, rater_scores=[{"rater_id": "fictional_rater_1", "score": 4}])
        bundle.pop("independent_check_ref")
        bundle.pop("heldout_secrecy")
        for row in bundle["raw_ratings"]:
            row["value"] = 7
        report = self.score(run)
        self.assertEqual(self.result(report, "O1")["formal_score"], 4)
        self.assertNotIn("presence_score_mismatch", self.result(report, "O1")["issues"])
        item["score"] = bundle["score"] = 5
        bundle["rater_scores"][0]["score"] = 5
        report = self.score(run)
        self.assertEqual(self.result(report, "O1")["formal_status"], "protocol_error")
        self.assertIsNone(self.result(report, "O1")["formal_score"])

    def test_final_review_cannot_substitute_a_baseline_date(self):
        run = fictional_run(self.catalog, "Integrated")
        final = next(o for o in self.item(run, "P1")["bundles"][0]["required_observations"] if o["kind"] == "final_review")
        final["planned_at"] = final["observed_at"] = cepb.iso_time(START)
        report = self.score(run)
        self.assertIn("final_review_before_maturity", self.result(report, "P1")["issues"])
        self.assertIsNone(self.result(report, "P1")["formal_score"])

    def test_baseline_requires_both_clocks_in_origin_first_month(self):
        for field in ("planned_at", "observed_at"):
            run = fictional_run(self.catalog, "Integrated")
            baseline = self.item(run, "P1")["bundles"][0]["required_observations"][0]
            baseline[field] = cepb.iso_time(cepb.add_calendar_months(START, 1))
            report = self.score(run)
            self.assertIn("baseline_outside_initial_month", self.result(report, "P1")["issues"])
            self.assertIsNone(self.result(report, "P1")["formal_score"])

    def test_independent_review_requires_two_distinct_reviewers(self):
        run = fictional_run(self.catalog, "Integrated")
        run["verification"].update(level="independently_reviewed", reviewer_ids=["fictional_reviewer_1"], report_ref=REFERENCE)
        report = self.score(run)
        self.assertIn("reviewer_missing", self.codes(report))
        self.assertIsNone(report["official_score"])
        self.assertFalse(report["full_attainment_eligible"])
        run["verification"]["reviewer_ids"] = ["fictional_reviewer_1", "fictional_reviewer_1"]
        self.assertIn("duplicate_id", self.codes(self.score(run)))
        run["verification"]["reviewer_ids"] = ["fictional_reviewer_1", "fictional_reviewer_2"]
        self.assertTrue(self.score(run)["full_attainment_eligible"])

    def test_invalid_clocks_never_mature_missing_evidence_bounds(self):
        for fault in ("pre_floor", "future_as_of", "future_registration"):
            run = fictional_run(self.catalog, "Integrated", complete=False)
            if fault == "pre_floor":
                for field in ("rule_publication_at", "registered_at", "first_independent_observation_at"):
                    run["lineage"][field] = "2020-01-01T00:00:00Z"
            elif fault == "future_as_of":
                run["as_of"] = "2030-01-01T00:00:00Z"
            else:
                run["lineage"]["registered_at"] = "2030-01-01T00:00:00Z"
            report = self.score(run)
            self.assertIsNone(report["temporal"]["lineage_t0"])
            self.assertTrue(all(i["temporal_cap"] == 4 for i in report["items"] if cepb.short_id(i["id"]).startswith("P")))
            self.assertEqual(report["bounds"]["upper"], 990)
            self.assertFalse(report["full_attainment_eligible"])

    def test_required_gates_and_weighted_coverage_are_separate_from_points(self):
        run = fictional_run(self.catalog, "Integrated")
        run["verification"].update(level="independently_reviewed", reviewer_ids=["fictional_reviewer_1", "fictional_reviewer_2"], report_ref=REFERENCE)
        run["gates"] = [run["gates"][0]]
        report = self.score(run)
        self.assertEqual(report["official_score"], 1000)
        self.assertFalse(report["full_attainment_eligible"])
        self.assertIn("longitudinal", report["missing_gates"])
        missing = self.item(run, "A1")
        missing.update(status="unobserved", score=None, bundles=[])
        report = self.score(run)
        self.assertEqual(report["item_coverage"], 95 / 96)
        self.assertAlmostEqual(report["weighted_coverage"], (1000 - 80 / 6) / 1000)
        quick = self.score(fictional_run(self.catalog, "Quick"))
        self.assertIsNone(quick["weighted_coverage"])

    def test_missing_local_evidence_and_https_no_network_check(self):
        run = fictional_run(self.catalog)
        self.item(run)["evidence_refs"] = ["missing.md"]
        self.assertIsNone(self.result(self.score(run))["formal_score"])
        self.item(run)["evidence_refs"] = ["https://example.org/unfetched-evidence"]
        self.assertEqual(self.result(self.score(run))["formal_score"], 5)

    def test_json_duplicate_keys_nan_and_overflow_are_rejected(self):
        path = self.base / "invalid.json"
        for raw in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}', '{"x":1e999}'):
            path.write_text(raw, encoding="utf-8")
            with self.assertRaises(ValueError):
                cepb.load_json(path)

    def test_cli_init_validate_score_and_nonoverwrite(self):
        path = self.base / "run.json"
        script = str(PACKAGE / "cepb.py")
        def command(*args):
            return subprocess.run([sys.executable, script, *args], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(command("init", "--track", "Quick", "--output", str(path)).returncode, 0)
        self.assertEqual(command("init", "--output", str(path)).returncode, 2)
        self.assertEqual(command("validate", str(path)).returncode, 0)
        out, markdown = self.base / "report.json", self.base / "report.md"
        self.assertEqual(command("score", str(path), "--json", str(out), "--markdown", str(markdown), "--lang", "ja").returncode, 0)
        report = cepb.load_json(out)
        self.assertEqual(report["known_items"], 0)
        self.assertFalse(report["certification_issued"])
        self.assertIn("意味の自動採点", markdown.read_text(encoding="utf-8"))
        self.assertEqual(command("score", str(path), "--json", str(out)).returncode, 2)
        self.assertEqual(command("score", str(path), "--json", str(path)).returncode, 2)


def write_fictional_examples():
    """Used only by maintainers to create the checked-in fictional examples."""
    catalog = cepb.load_catalog()
    examples = PACKAGE / "examples"
    examples.mkdir(exist_ok=True)
    current = cepb.utc_time("2026-10-09T15:00:00Z")
    core = fictional_run(catalog, "Core")
    core["as_of"] = cepb.iso_time(current)
    cepb.write_json(examples / "synthetic_core_complete.json", core)
    integrated = fictional_run(catalog, "Integrated", complete=False)
    integrated["as_of"] = cepb.iso_time(current)
    for item in integrated["items"]:
        if not cepb.short_id(item["id"]).startswith(("O", "P")):
            item.update(status="scored", score=3, reason="Fictional ordinary support only.", evidence_refs=[REFERENCE], bundles=[behavioral_bundle(item["id"], 3)])
    cepb.write_json(examples / "synthetic_integrated_partial.json", integrated)
    quick = fictional_run(catalog, "Quick", complete=False)
    quick["as_of"] = cepb.iso_time(current)
    quick["items"][0].update(provisional_score=3, evidence_refs=[REFERENCE], reason="Fictional provisional example only.")
    quick["items"][1].update(status="unsupported", score=0, evidence_refs=[REFERENCE], reason="Fictional unsupported capability declaration.")
    cepb.write_json(examples / "synthetic_quick_partial.json", quick)
    for track in catalog["tracks"]:
        template = cepb.make_run(catalog, track, current)
        cepb.write_json(PACKAGE / "templates" / f"{track.lower()}.run.json", template)
    for name, value in (("behavioral_bundle.json", behavioral_bundle("A1", 0)),
                        ("human_presence_bundle.json", presence_bundle("O1", 0)),
                        ("cumulative_window_bundle.json", cumulative_bundle("P1", 0))):
        value["description"] = "FICTIONAL STRUCTURE EXAMPLE. Replace all IDs, observations, evidence and scores; do not claim these as real observations."
        if value["kind"] == "behavioral":
            for row in value["case_results"]:
                row.update(outcome="unknown", evidence_refs=[])
        elif value["kind"] == "human_presence":
            value["raw_ratings"] = []
        else:
            value.update(window_start=None, window_end=None)
            value["required_observations"] = [{"id": "replace-with-observation-id", "kind": "baseline",
                "planned_at": cepb.iso_time(current), "observed_at": None, "status": "unobserved", "clock": "utc_calendar", "evidence_refs": []}]
        cepb.write_json(PACKAGE / "templates" / name, value)


if __name__ == "__main__":
    unittest.main()
