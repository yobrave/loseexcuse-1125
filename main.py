import json
import os

COVER = "lsx3-alibi"
LIMIT = 200


class Alibi:
    __slots__ = ("line",)

    def __init__(self, line):
        self.line = line

    @classmethod
    def from_draft(cls, blob):
        for row in blob.replace("\r", "").split("\n"):
            if row.strip():
                return cls(row)
        return cls("")

    def holds(self):
        return 1 <= len(self.line) <= LIMIT

    def place(self, root):
        folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
        os.makedirs(folder, exist_ok=True)
        sheet = os.path.join(folder, "entry.txt")
        ink = self.line.encode("utf-8")
        with open(sheet, "wb") as clerk:
            clerk.write(ink)
        with open(sheet, "rb") as notary:
            if notary.read() != ink:
                raise RuntimeError("alibi notarized wrong")
        return sheet


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as draft:
    story = Alibi.from_draft(draft.read())

if not story.holds():
    print(json.dumps({"alibi": "thin", "size": len(story.line)}))
    raise SystemExit(1)
sheet = story.place(root)
print(json.dumps({"alibi": "airtight", "size": len(story.line), "cover": COVER, "sheet": os.path.basename(sheet)}))
