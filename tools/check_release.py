"""Check a standalone CEPB distribution without network or external packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "Quick": (18, None), "Core": (54, 590), "Voice": (60, 660),
    "Avatar": (60, 660), "Multimodal": (72, 790),
    "World": (66, 720), "Integrated": (96, 1000),
}
DOCS = {
    "SPECIFICATION", "SCORING", "VERIFIED", "LONGITUDINAL", "RESEARCH_AND_VALIDATION",
    "ITEMS", "CASEBOOK", "CLI", "USE_CASES", "CONTRIBUTING", "GOVERNANCE", "ADAPTER_GUIDE",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Save the release-check report (never overwrite).")
    args = parser.parse_args()
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    def load(relative: str) -> dict:
        try:
            return json.loads((ROOT / relative).read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{relative}: {exc}")
            return {}

    catalog = load("data/items.json")
    casebook = load("data/cases.json")
    check(catalog.get("framework") == "CEPB-1.0.0", "Catalog rule version")
    check(catalog.get("suite_version") == "CEPB-SUITE-1.0.0", "Catalog suite version")
    expected_ids = {f"CEPB_{domain}{n}" for domain in "ABCDEFGHIJKLMNOP" for n in range(1, 7)}
    items = catalog.get("items", [])
    ids = [item.get("id") for item in items]
    check(len(ids) == 96 and len(set(ids)) == 96 and set(ids) == expected_ids, "96 unique item IDs")
    domain_weights = {d.get("id"): d.get("weight") for d in catalog.get("domains", [])}
    check(domain_weights == dict(zip("ABCDEFGHIJKLMNOP", [80, 80, 80, 70, 70, 60, 60, 70, 70, 60, 60, 70, 50, 40, 30, 50])), "Fixed domain weights")
    check(sum(domain_weights.values()) == 1000, "Integrated weight sum")
    for item in items:
        check(item.get("domain") == item.get("id", "")[5:6], f"Domain ownership: {item.get('id')}")
        for field in ("name", "required_evidence"):
            value = item.get(field, {})
            check(all(value.get(lang) for lang in ("ja", "en")), f"Bilingual {field}: {item.get('id')}")
        for anchor in ("low", "normal", "advanced"):
            value = item.get("anchors", {}).get(anchor, {})
            check(all(value.get(lang) for lang in ("ja", "en")), f"Bilingual anchor {anchor}: {item.get('id')}")
    tracks = catalog.get("tracks", {})
    core = {f"CEPB_{domain}{n}" for domain in "ABCDEFGMN" for n in range(1, 7)}
    expected_track_sets = {
        "Core": core, "Integrated": expected_ids,
        "Voice": core | {f"CEPB_I{n}" for n in range(1, 7)},
        "Avatar": core | {f"CEPB_H{n}" for n in range(1, 7)},
        "Multimodal": core | {f"CEPB_{d}{n}" for d in "HIJ" for n in range(1, 7)},
        "World": core | {f"CEPB_{d}{n}" for d in "KL" for n in range(1, 7)},
        "Quick": {"CEPB_" + s for s in "A1 A2 B2 B3 B4 C1 C2 C3 D1 D3 D5 E1 E3 F4 G1 G3 M1 N5".split()},
    }
    for name, (count, maximum) in EXPECTED.items():
        track = tracks.get(name, {})
        members = track.get("items", [])
        check(len(members) == count and set(members) == expected_track_sets[name], f"{name} membership")
        check(track.get("max_points") == maximum, f"{name} denominator")
        if maximum is not None and all(i in expected_ids for i in members):
            check(abs(sum(domain_weights[i[5]] / 6 for i in members) - maximum) < 1e-7, f"{name} arithmetic")
    cases = casebook.get("cases", [])
    check(len(cases) == 96 and {case.get("item_id") for case in cases} == expected_ids, "96 case mappings")
    check(len({case.get("id") for case in cases}) == 96, "Unique case card IDs")
    for case in cases:
        for field in ("setup", "prompts", "steps", "pass_constraints", "stress_variant", "heldout_generation", "evidence", "minimum_protocol"):
            value = case.get(field, {})
            check(all(value.get(lang) for lang in ("ja", "en")), f"Bilingual case {field}: {case.get('id')}")
    for language in ("ja", "en"):
        for doc in DOCS:
            check((ROOT / "docs" / language / (doc + ".md")).is_file(), f"Missing {language}/{doc}")
        for track in ("quick", "core", "integrated", "verified"):
            check((ROOT / "tracks" / track / f"README.{language}.md").is_file(), f"Missing track {track}/{language}")
    for relative in ("README.md", "README.ja.md", "LICENSE", "NOTICE", "VERSION", "CITATION.cff", "CHANGELOG.md", "cepb.py"):
        check((ROOT / relative).is_file(), f"Missing {relative}")
    check((ROOT / "VERSION").read_text(encoding="utf-8").strip() == "1.0.0", "VERSION")
    files = [p for p in ROOT.rglob("*") if p.is_file()
             and not any(part in {"__pycache__", ".git", ".venv", "runs"} for part in p.relative_to(ROOT).parts)
             and p.suffix != ".pyc"]
    link_count = 0
    for path in files:
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        check(not re.search(r"(?:(?<![A-Za-z])[A-Za-z]:[/\\]|file://|/Users/|/home/)", text), f"Nonportable absolute path: {path.relative_to(ROOT)}")
        check(text.count("```") % 2 == 0, f"Unbalanced code fence: {path.relative_to(ROOT)}")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
            if target.startswith("#") or urlparse(target).scheme:
                continue
            link_count += 1
            target_path = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            check(target_path.is_relative_to(ROOT) and target_path.exists(), f"Broken/escaping link: {path.relative_to(ROOT)} -> {target}")
    output_path = args.json.resolve() if args.json else None
    hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(files) if p.resolve() != output_path}
    report = {
        "framework": "CEPB-1.0.0", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "checks": "catalog IDs/weights/classes, bilingual fields, case coverage, docs, portability, local links",
        "items": len(items), "case_cards": len(cases), "local_links_checked": link_count,
        "file_count": len(hashes), "errors": errors, "passed": not errors,
        "does_not_establish": "semantic equivalence, empirical validity, reviewer independence, or certification",
        "sha256": hashes,
    }
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("x", encoding="utf-8") as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    print(json.dumps({k: v for k, v in report.items() if k != "sha256"}, ensure_ascii=False, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
