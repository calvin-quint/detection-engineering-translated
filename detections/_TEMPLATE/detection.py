"""[Entry title] — translated detection logic.

Runs against a generic list-of-dicts log schema (see test_logs.json),
not any specific vendor's SDK or query language. Field names below are
placeholders — rename to match whatever generic schema this entry uses.
"""
from __future__ import annotations

from typing import Iterable


def detect(events: Iterable[dict]) -> list[dict]:
    """Return the subset of events (or derived findings) that match the
    detection logic. Keep this function importable and testable —
    no I/O, no side effects."""
    findings = []
    for event in events:
        # TODO: replace with the real translated condition(s)
        if False:
            findings.append(event)
    return findings


if __name__ == "__main__":
    import json
    from pathlib import Path

    logs = json.loads((Path(__file__).parent / "test_logs.json").read_text())
    for finding in detect(logs):
        print(finding)
