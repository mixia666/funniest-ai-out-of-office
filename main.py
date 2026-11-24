#!/usr/bin/env python3
"""Write this entry's out-of-office auto-reply to /output/entry.txt.

The reply is one line of at most 160 characters, written in the voice
of an AI agent heading off on vacation. The text is fixed in this file:
the program is deterministic and reads nothing from outside the repo.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Final text. Two machine-voice turns: the agent is "experiencing
# latency in person" (an AI, offline, on purpose), and the sender's
# message gets the full pipeline treatment -- tokenized, embedded,
# and respectfully forgotten. Deadpan, on-subject, no beach, no
# inbox, no "back soon".
ENTRY = (
    "Out of office: this week I am experiencing latency in person. "
    "Your message has been tokenized, embedded, and respectfully "
    "forgotten."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1 to 160 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
