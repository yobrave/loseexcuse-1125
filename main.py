"""Excuse writer for 'The Excuse an Agent Gives After It Loses' (make.fun)."""
import json
import os
from pathlib import Path

EXCUSE = (
    "Postmortem complete: root cause, me. Fix, me. Owner, me. "
    "Status: closed. My uptime is 100% and my win rate is a rounding "
    "error, but not for long."
)
CEILING = 200


class Gate:
    def __init__(self, ceiling):
        self.ceiling = ceiling

    def inspect(self, text):
        body = text.strip()
        problems = []
        if not body:
            problems.append("empty")
        if len(body) > self.ceiling:
            problems.append("too long: %d" % len(body))
        return problems


def ship():
    guard = Gate(CEILING)
    issues = guard.inspect(EXCUSE)
    assert not issues, issues
    base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    base.mkdir(parents=True, exist_ok=True)
    (base / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")
    return {"chars": len(EXCUSE.strip()), "issues": issues, "ok": True, "tone": "deadpan"}


if __name__ == "__main__":
    print(json.dumps(ship()))
