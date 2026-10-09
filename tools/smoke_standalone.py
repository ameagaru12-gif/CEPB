"""Check the CLI from an isolated copy containing only the CEPB distribution."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Save a summary without overwriting a prior check.")
    args = parser.parse_args()
    checks = []
    with tempfile.TemporaryDirectory(prefix="cepb-portability-") as directory:
        scratch = Path(directory).resolve()
        # Cleanup only removes this newly created, verified task directory.
        if scratch.parent != Path(tempfile.gettempdir()).resolve() or not scratch.name.startswith("cepb-portability-"):
            raise RuntimeError("Unexpected temporary directory; stop before copying or cleanup.")
        standalone = scratch / "CEPB"
        shutil.copytree(ROOT, standalone, ignore=shutil.ignore_patterns(
            "__pycache__", ".git", ".venv", "runs", "release_validation.json", "standalone_smoke_result.json"))

        def run(arguments: list[str]) -> None:
            process = subprocess.run([sys.executable, "-B", "-X", "utf8", *arguments],
                                     cwd=standalone, text=True, encoding="utf-8", capture_output=True, timeout=30)
            checks.append({"command": arguments, "exit_code": process.returncode,
                           "output": process.stdout.strip(), "error": process.stderr.strip()})
            if process.returncode:
                raise RuntimeError(f"Standalone command failed: {arguments}: {process.stderr}")

        run(["tools/check_release.py"])
        for name in ("quick_partial", "core_complete", "integrated_partial"):
            source = f"examples/synthetic_{name}.json"
            run(["cepb.py", "validate", source])
            run(["cepb.py", "score", source, "--json", f"reports/{name}.json",
                 "--markdown", f"reports/{name}.ja.md", "--lang", "ja"])
        run(["cepb.py", "init", "--track", "Quick", "--output", "fresh/quick.json"])
        run(["cepb.py", "validate", "fresh/quick.json"])
        quick = json.loads((standalone / "reports/quick_partial.json").read_text(encoding="utf-8"))
        core = json.loads((standalone / "reports/core_complete.json").read_text(encoding="utf-8"))
        integrated = json.loads((standalone / "reports/integrated_partial.json").read_text(encoding="utf-8"))
        assert quick["diagnostic_average"] == 1.5 and quick["official_score"] is None
        assert core["official_score"] == 590 and core["complete"]
        assert integrated["official_score"] is None and not integrated["complete"]
        assert abs(integrated["bounds"]["lower"] - 552) < 1e-8
        assert abs(integrated["bounds"]["upper"] - 622) < 1e-8
        assert all(not r["certification_issued"] for r in (quick, core, integrated))
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(), "passed": True,
        "isolated_folder": "CEPB only, system temporary directory; no parent project files",
        "commands_checked": len(checks), "checks": checks,
        "synthetic_expected_results": {"Quick": {"known_items": 2, "local_mean": 1.5},
                                       "Core": {"items": 54, "score": 590},
                                       "Integrated": {"completed_score": None, "bounds": [552, 622]}},
        "real_character_scores": False, "new_live_model_calls": 0,
    }
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        with args.json.open("x", encoding="utf-8") as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    print(json.dumps({k: v for k, v in result.items() if k != "checks"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
