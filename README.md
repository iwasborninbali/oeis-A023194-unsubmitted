# OEIS A023194: conditional uniqueness argument (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 15 Nov 2026).

- [A023194](https://oeis.org/A023194), the 'Proof' assumes the Goormaghtigh conjecture (check Grantham 2024): **candidate** (2026-11-13: repository built (core c6)). Certificate: complete.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

The sequence lists positive integers n for which σ(n), the sum of all positive divisors of n, is prime, in increasing order. Its offset is 1; σ(1)=1, which is not prime.

## Terms / result

No term changes. The live [A023194](https://oeis.org/A023194), read 2026-11-13, contains Bernard Schott's Aug 17 2026 statement: `Only two distinct terms a(4) = 16 and a(5) = 25 give the same prime: 31. Proof: according to the Goormaghtigh conjecture, only two numbers are repunits with at least three digits in two different bases, these two numbers are Mersenne primes 31 and 8191;` the subsequent argument excludes 8191. The argument explicitly assumes an unproved conjecture and therefore does not establish unconditional uniqueness.

## How it was obtained

Prime divisor sums arise from prime-power arguments and are repunits. The reduction and the conditional exclusion of 8191 are detailed in [proof.md](proof.md). Jon Grantham, *No new Goormaghtigh primes up to 10^700*, INTEGERS 24 (2024), A98, [arXiv:2410.03677](https://arxiv.org/abs/2410.03677), abstract read 2026-11-13, excludes other prime-valued repunit collisions below 10^700, not all larger values. The arXiv v3 notes a corrected computation; this repository does not recheck it.

## Verification

A separate divisor-sum sieve checks arguments through 100000 and finds the single collision 31. This is only a finite check; it does not establish global uniqueness or independently verify Grantham's bound. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Schott's entry gives the conditional argument. Grantham's result gives a large unconditional range. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 verification/check.py` (under one second). Expected output:

```text
arguments checked: 100000
prime divisor-sum arguments: 23
collisions within range: [(31, [16, 25])]
8191 repunits: 8191 8191
all nontrivial repunit representations of 8191: [(2, 13), (90, 3)]
all nontrivial repunit representations of 31: [(2, 5), (5, 3)]
```

## Provenance

Source: `projects/science/athanor-oeis`, commit `11b7ea9cc6f4c0057731d8e36c023f8b36e7c27f`, `tasks/2026-11-12-A000668-sigma-collision-31/answers/2026-11-12-chatgpt.md`. The checker and reduction were written for this repository.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
