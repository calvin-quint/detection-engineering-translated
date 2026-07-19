# detections/

One folder per entry, dated. Each entry is either a production detection
translated into vendor-neutral Python, a current security-news campaign
researched and written up (with translated detection logic if one
resulted), or both.

## Structure

```
detections/
  YYYY-MM-DD-<slug>/
    README.md         # required — the writeup: what this is, ATT&CK mapping,
                        # detection reasoning, what it catches, what it doesn't
    detection.py         # optional — only if translatable logic exists
    test_logs.json         # optional — synthetic log fixtures detection.py runs against
```

Use `_TEMPLATE/` as the starting point for a new entry.

## What goes in README.md

- **Source**: a production rule (no employer-identifying detail) or a
  named public campaign — cite the reporting (vendor blog, news, MITRE
  ATT&CK Groups page) if it's the latter.
- **ATT&CK mapping**: tactic/technique, in plain language first, IDs
  second.
- **Detection reasoning**: the hypothesis — what normal looks like, what
  specific deviation this catches, stated as a claim that could be wrong.
- **What it catches / what it doesn't**: be as explicit about the misses
  as the hits — this is what separates a real writeup from a summary.

## What goes in detection.py (when present)

Plain Python against a generic/synthetic log schema — no vendor SDK, no
KQL, no employer-specific field names. The point is that the underlying
logic is legible to someone who's never touched Sentinel, Splunk, or
whatever the original was built in.

## Index

| Date | Entry | Source | Has detection.py |
|---|---|---|---|
| — | — | — | — |

Update this table when adding an entry.
