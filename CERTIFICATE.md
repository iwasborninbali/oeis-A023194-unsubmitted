# Verification certificate

## Claim

The cited uniqueness argument assumes the Goormaghtigh conjecture; Grantham's finite bound does not remove that assumption globally.

## Evidence

| What | Path | Author and date | Coverage | Result |
|---|---|---|---|---|
| Derivation | [proof.md](proof.md) | OpenAI Codex, 2026-11-13, based on reviewed source | Conditional reduction | Uniqueness follows from the conjecture |
| Independent finite sieve | [verification/check.py](verification/check.py) | OpenAI Codex, 2026-11-13 | Arguments 1..100000 | Only collision is 31 |

The sieve shares no code or input table with the source answer. It uses the same divisor-sum definition.

## Replayed for this repository

2026-11-13, macOS local workstation: `python3 verification/check.py`; output: [verification/logs/check.txt](verification/logs/check.txt).

## Not covered

Global uniqueness, the Goormaghtigh conjecture, Grantham's proof and 10^700 computation were not checked. The finite sieve restricts both arguments, not the common prime value.

## Guide's independent check

pending

## Verdict

complete — the independent finite check was replayed in full for its stated range; the conditional proof and external result retain the stated limitations.
