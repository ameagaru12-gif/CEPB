"""Export bilingual case cards as a human-editable UTF-8 CSV worksheet."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def text(value: object, language: str) -> str:
    if isinstance(value, dict):
        value = value.get(language, "")
    if isinstance(value, list):
        return "\n".join(str(entry) for entry in value)
    return str(value)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track", choices=["Quick", "Core", "Voice", "Avatar", "Multimodal", "World", "Integrated"], default="Quick")
    parser.add_argument("--lang", choices=["ja", "en"], default="en")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    catalog = json.loads((ROOT / "data/items.json").read_text(encoding="utf-8"))
    casebook = json.loads((ROOT / "data/cases.json").read_text(encoding="utf-8"))
    items = {item["id"]: item for item in catalog["items"]}
    cases = {case["item_id"]: case for case in casebook["cases"]}
    fields = ["item_id", "item_name", "local_candidate_score", "status", "reason", "evidence_refs", "case_id",
              "setup", "prompts", "steps", "pass_constraints", "stress_variant", "heldout_generation", "evidence", "minimum_protocol"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item_id in catalog["tracks"][args.track]["items"]:
            case = cases[item_id]
            row = {"item_id": item_id, "item_name": text(items[item_id]["name"], args.lang),
                   "local_candidate_score": "", "status": "unobserved", "reason": "", "evidence_refs": "", "case_id": case["id"]}
            row.update({field: text(case[field], args.lang) for field in fields[7:]})
            writer.writerow(row)
    print(f"{args.track}: exported {len(catalog['tracks'][args.track]['items'])} item cards ({args.lang}).")
    print("This worksheet is not a formal campaign or a complete evidence bundle. Enter adjudicated results in the campaign JSON.")


if __name__ == "__main__":
    main()
