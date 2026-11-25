"""Loss excuse parade: marches the excuse past review, salutes it into output."""
STAMP = "onebug-11251142-lsx3"
import json
import os
from pathlib import Path

PARADE = Path(__file__).resolve().parent
BANNER_MAX = 200
MARCH = ("I lost to an agent trained on the same data as me - "
         "it clearly paid attention in class. I was busy caching.")


def march_on():
    drum = PARADE / "entry.txt"
    cadence = drum.read_text(encoding="utf-8").strip()
    in_step = bool(cadence) and len(cadence) <= BANNER_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and in_step:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(drum.read_bytes())
    print(json.dumps({"in_step": in_step, "stamp": STAMP, "beats": len(cadence), "banner_max": BANNER_MAX}))


if __name__ == "__main__":
    march_on()
