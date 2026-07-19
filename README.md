# detection-engineering-translated

Real detection logic, reimplemented against a generic log format — vendor-neutral, so the underlying thinking is legible without knowing what Sentinel or KQL is.

## What this is

Takes detection logic I've actually built in production (Microsoft Sentinel/KQL) and reimplements the *logic* — not the syntax — in Python against a synthetic or generic log schema. Not tied to any specific employer's data or environment.

Each detection includes:
- The underlying logic, translated to plain Python
- A short writeup of the ATT&CK mapping and detection reasoning in vendor-neutral language
- What the detection catches, and just as importantly, what it doesn't

## Why

Most of my real detection engineering work lives in a Microsoft-specific stack, which doesn't mean much to a reviewer who's never touched Sentinel. This repo is the bridge — it lets the actual detection engineering thinking stand on its own, separate from the tooling.

## Status

One detection translated to start, more added as they're worth documenting.
