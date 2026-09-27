"""Refuse to dispatch a visual builder without the owner's anchor.

Lesson from a real failure: 6 consecutive rounds of agent-built UI prototypes were rejected
by the owner before a different method got approval on the first batch. This script is the
mechanical version of a stop-rule that, written only as prose, kept getting ignored.

usage: python3 check_brief.py <brief.md>   -> exit 0 releases, exit 1 blocks

The brief needs these lines (values after the colon):
  ANCHOR: <path(s) to what the owner picked on the recognition board>
  ANCHOR_DATE: YYYY-MM-DD or YYYY-MM-DDTHH:MM (the time, if it lands on rejection day)
  ANCHOR_QUOTE: <the owner's own words about the pick>
  CONSECUTIVE_REJECTIONS: <n>
  LAST_REJECTION: YYYY-MM-DD[THH:MM]   (or "none")
  RULES_CONSULTED: <design memories and ADRs read before this brief>
  ART_IN_CODE: no   (a character, mascot, or vehicle is never drawn in code)
"""
import re
import sys
from datetime import datetime

FIELDS = ["ANCHOR", "ANCHOR_DATE", "ANCHOR_QUOTE", "CONSECUTIVE_REJECTIONS",
          "LAST_REJECTION", "RULES_CONSULTED", "ART_IN_CODE"]


def main(path):
    text = open(path, encoding="utf-8").read()
    values = {f: (m.group(1).strip() if (m := re.search(rf"^{f}:\s*(.+)$", text, re.M)) else "")
              for f in FIELDS}
    errors = [f"missing {f}" for f, v in values.items() if not v]
    if not errors:
        if values["ART_IN_CODE"].lower() != "no":
            errors.append("ART_IN_CODE must be 'no'")
        try:
            n = int(values["CONSECUTIVE_REJECTIONS"])
            anchor = datetime.fromisoformat(values["ANCHOR_DATE"])
            last = values["LAST_REJECTION"]
            if n >= 2 and last != "none" and anchor <= datetime.fromisoformat(last):
                errors.append(
                    f"{n} consecutive rejections and the anchor ({anchor}) is not newer than "
                    f"the last rejection ({last}): go back to the recognition board, do not "
                    f"dispatch a third build"
                )
        except ValueError as e:
            errors.append(f"invalid value: {e}")
    for e in errors:
        print("BLOCKED:", e)
    if not errors:
        print("ok: brief carries the owner's anchor and does not repeat a round blind")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python3 check_brief.py <brief.md>")
    sys.exit(main(sys.argv[1]))
