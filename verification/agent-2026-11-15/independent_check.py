#!/usr/bin/env python3
"""Independent A023194 audit: prime-power enumeration + deterministic 64-bit MR.

No code or data tables are imported from the target repository.  We use the
mathematical necessary condition that sigma(n) prime implies n=p^(q-1),
with p and q primes, rather than a divisor-sum sieve over all arguments.
"""
from bisect import bisect_right
from collections import defaultdict
from math import isqrt
from time import perf_counter

LIMIT = 100_000_000_000_000  # all integer arguments 1..10^14
SMALL_LIMIT = 100_000
# A proven deterministic witness set for every unsigned 64-bit integer.
MR_BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def primes_through(high):
    """Bytearray Eratosthenes, yielding all primes up to high inclusively."""
    marks = bytearray(b'\x01') * (high + 1)
    marks[0:2] = b'\x00\x00'
    for d in range(2, isqrt(high) + 1):
        if marks[d]:
            start = d * d
            marks[start: high + 1: d] = b'\x00' * ((high - start) // d + 1)
    return [k for k in range(2, high + 1) if marks[k]]


def prime64(n):
    """Deterministic Miller-Rabin on [0, 2^64), including small cases."""
    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p
    assert n < (1 << 64)
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in MR_BASES_64:
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def divisors_sum_slow(n):
    """Elementary direct divisor pairing for spot-checks (not geometric sums)."""
    total = 0
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
    return total


def nontrivial_representations(value):
    """Search *all* bases and lengths >=3 by growing each repunit."""
    found = []
    for base in range(2, isqrt(value) + 1):
        power = base * base
        repunit = 1 + base + power
        length = 3
        while repunit <= value:
            if repunit == value:
                found.append((base, length))
            power *= base
            repunit += power
            length += 1
    return found


def main():
    start = perf_counter()
    ps = primes_through(isqrt(LIMIT))
    exponents = primes_through(LIMIT.bit_length() + 1)
    # q=2 gives sigma(p)=p+1; only p=2 works.
    valid = [(3, 2)]
    candidates = 1
    by_value = defaultdict(list)
    by_value[3].append(2)
    q_stats = []

    for q in exponents:
        if q < 3 or (1 << (q - 1)) > LIMIT:
            continue
        evaluated = accepted = 0
        e = q - 1
        for base in ps:
            arg = base ** e
            if arg > LIMIT:
                break
            # This is sigma(base**e), with base prime, via a geometric sum.
            value = (arg * base - 1) // (base - 1)
            assert value < (1 << 64)
            evaluated += 1
            if prime64(value):
                accepted += 1
                valid.append((value, arg))
                by_value[value].append(arg)
        candidates += evaluated
        q_stats.append((q, evaluated, accepted))

    terms_small = sorted(n for _, n in valid if n <= SMALL_LIMIT)
    collisions = sorted((v, sorted(ns)) for v, ns in by_value.items() if len(ns) > 1)
    assert len(valid) == sum(len(ns) for ns in by_value.values())
    assert all(prime64(v) for v in by_value)
    assert all(divisors_sum_slow(n) == v for v, n in valid if n <= 100_000)
    assert 1 not in terms_small

    print('method: enumerate p^(q-1), primes p,q; deterministic 64-bit Miller-Rabin')
    print('argument range: 1..%d inclusive' % LIMIT)
    print('sieve prime-base bound: %d' % isqrt(LIMIT))
    print('prime bases generated: %d' % len(ps))
    print('prime exponents used: %s' % [q for q, _, _ in q_stats])
    print('per-exponent (q, candidates, prime sigma): %s' % q_stats)
    print('candidate prime powers tested (including n=2): %d' % candidates)
    print('arguments with prime sigma (full range): %d' % len(valid))
    print('distinct prime sigma values (full range): %d' % len(by_value))
    print('collisions (full range): %s' % collisions)
    print('arguments with prime sigma (1..100000): %d' % len(terms_small))
    print('terms through 100000: %s' % terms_small)

    for value in (31, 8191):
        reps = nontrivial_representations(value)
        primes_only = [(p, m, p ** (m - 1)) for p, m in reps if prime64(p)]
        print('%d nontrivial repunits (base,length): %s' % (value, reps))
        print('%d prime-base preimages (base,length,n): %s' % (value, primes_only))
        print('%d primality: %s' % (value, prime64(value)))
        for _, _, arg in primes_only:
            assert divisors_sum_slow(arg) == value
            print('direct sigma(%d) = %d' % (arg, divisors_sum_slow(arg)))

    assert collisions == [(31, [16, 25])]
    assert len(terms_small) == 23
    assert nontrivial_representations(31) == [(2, 5), (5, 3)]
    assert nontrivial_representations(8191) == [(2, 13), (90, 3)]
    print('all assertions: PASS')
    print('elapsed wall-clock seconds: %.3f' % (perf_counter() - start))


if __name__ == '__main__':
    main()
