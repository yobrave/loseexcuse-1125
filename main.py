"""lex6: loss ledger. Nested ladders, no exceptions, one honest entry out."""
import json
import os
import sys
from pathlib import Path

BOOK = 200


def audit(raw: str) -> dict:
    body = raw.strip()
    if len(body) == 0:
        return {"pass": False, "why": "blank"}
    if body.isspace():
        return {"pass": False, "why": "invisible"}
    if len(body) > BOOK:
        return {"pass": False, "why": "overbook"}
    return {"pass": True, "why": "booked", "chars": len(body)}


def main():
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    result = audit(raw)
    if result["pass"]:
        shelf = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        shelf.mkdir(parents=True, exist_ok=True)
        (shelf / "entry.txt").write_bytes(raw.strip().encode("utf-8"))
    result["ledger"] = "lex6-loss-r11251422"
    result["book"] = BOOK
    print("VERDICT", json.dumps(result))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
