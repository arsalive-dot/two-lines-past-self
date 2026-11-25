#!/usr/bin/env python3
"""Write the two-line warning to your past self to /output/entry.txt.

Line one warns about one concrete moment: the 2 a.m. email to the
boss, with a time, a decision and a physical action (close the laptop).
Line two traces real cause and effect from that moment — the unsent
email is why the job was still there on Monday, and five years later.
The voice is plain and written to one specific person, not an audience.
The warning sets the moment up and the second line lands the
consequence, with no wasted words.
"""
import os

TEXT = (
    "Do not send the 2 a.m. email to your boss \u2014 close the laptop "
    "and sleep on it.\n"
    "That unsent email is why you still had a job on Monday, and the "
    "same job five years later."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
