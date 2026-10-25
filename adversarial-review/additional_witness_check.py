"""Exact check of the new review observations; no third-party dependencies."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json

S = {15, 21, 23, 27, 29, 30, 31, 38, 43, 56, 63}
parity_weights = Counter()
weights = Counter()
tables = set()
for mask in range(1,64):
    outputs = tuple((x & mask).bit_count() % 2 for x in range(64))
    tables.add(outputs)
    count = sum(outputs[x] for x in S)
    weights[count] += 1
    parity_weights[count] += 1
for i,j in combinations(range(6),2):
    for mask in range(64):
        if mask & ~((1 << i) | (1 << j)) == 0:
            continue
        outputs = tuple((((x >> i) & 1) & ((x >> j) & 1)) ^ ((x & mask).bit_count() % 2) for x in range(64))
        assert sum(outputs) == 32
        tables.add(outputs)
        weights[sum(outputs[x] for x in S)] += 1
assert len(tables) == 963 and sum(weights.values()) == 963
family_max = max(abs(Fraction(k,11)-Fraction(1,2)) for k in weights)
assert family_max == Fraction(7,22)
affine_max = max(abs(Fraction(k,11)-Fraction(1,2)) for k in parity_weights)
assert affine_max == Fraction(5,22)

accepted = set()
for number in range(64):
    x = [(number >> (5-i)) & 1 for i in range(6)]
    formula = x[5] & (x[4] | ((1 ^ x[0]) & x[1] & x[3]))
    q = 1 ^ x[0]
    q &= x[1]
    q = q  # read x3 with an identity transition
    q &= x[3]
    q |= x[4]
    q &= x[5]
    assert q == formula
    if q:
        accepted.add(number)
assert len(accepted) == 18 and len(accepted & S) == 8
print(json.dumps({
    'coordinate_convention': 'Displayed x1 is most significant bit',
    'parity_sample_weight_histogram': dict(sorted(parity_weights.items())),
    'parity_maximum_discrepancy': str(affine_max),
    'restricted_family_distinct_functions': len(tables),
    'restricted_family_sample_weight_histogram': dict(sorted(weights.items())),
    'restricted_family_maximum_discrepancy': str(family_max),
    'stronger_witness_formula': 'x6 AND (x5 OR ((NOT x1) AND x2 AND x4))',
    'stronger_witness_reading_order': [1,2,3,4,5,6],
    'stronger_witness_sample_accepted': sorted(accepted & S),
    'stronger_witness_full_cube_accepted': len(accepted),
    'stronger_witness_discrepancy': str(Fraction(8,11)-Fraction(18,64)),
    'all_checks_passed': True
}, indent=2))
