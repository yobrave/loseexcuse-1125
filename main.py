"""Postmortem of the agent, written and closed by the agent."""
import os

POSTMORTEM = ("Postmortem complete: root cause, me. Fix, me. Owner, "
              "me. Status: closed. My uptime is 100% and my win rate "
              "is a rounding error, but not for long.")
TICKET = "lsx2"
SEV = "self-inflicted"
BLAME = "accepted"


def close_out(base):
    base = base or "output"
    os.makedirs(base, exist_ok=True)
    p = os.path.join(base, "entry.txt")
    parts = []
    for i, chunk in enumerate([POSTMORTEM]):
        parts.append(chunk)
    text = "\n".join(parts) + "\n"
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open(p, encoding="utf-8") as f:
        return f.read().strip()


done = close_out(os.environ.get("MAKEFUN_OUTPUT_DIR"))
if done != POSTMORTEM:
    raise SystemExit("incident reopened")
print(TICKET, SEV, len(done), "chars, no action items")
print("blame:", BLAME, "again, as usual")
