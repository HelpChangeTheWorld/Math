"""Deterministic adversarial AI review; no randomized support sampling."""
import hashlib
import importlib.util
import itertools
import json
import math
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

BASE = (Path(sys.argv[1]).resolve() if len(sys.argv) > 1
        else Path(__file__).resolve().parents[1] / 'source_publication')
OUT = Path(__file__).parent
spec = importlib.util.spec_from_file_location('constructor', BASE / 'evidence/eleven_point_obstruction.py')
constructor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(constructor)
canonical = [15, 21, 23, 27, 29, 30, 31, 38, 43, 56, 63]

def bits(x):
    return [int(c) for c in f'{x:06b}'][::-1]

def expected(x, a, b, pair=None):
    z = bits(x)
    value = (sum(z[k] * ((a >> k) % 2) for k in range(6)) + b) % 2
    return value if pair is None else (value + z[pair[0]] * z[pair[1]]) % 2

def simulate(x, order, codes):
    z = bits(x)
    state = 0
    for coordinate, code in zip(order, codes):
        table = [int(c) for c in f'{code:04b}'][::-1]
        state = table[state * 2 + z[coordinate]]
    return state

def packed(values):
    return sum(v * 2**i for i, v in enumerate(values))

results = {}
hashes = []
for entry in (BASE / 'SHA256SUMS.txt').read_text().splitlines():
    digest, name = entry.split('  ')
    hashes.append({'file': name, 'matches': hashlib.sha256((BASE / name).read_bytes()).hexdigest() == digest})
assert all(row['matches'] for row in hashes)
results['hashes'] = hashes

reproduced = json.loads(subprocess.check_output([sys.executable, str(BASE / 'evidence/publication_sanity_check.py')]))
assert reproduced == json.loads((BASE / 'evidence/publication_sanity_check.json').read_text())
results['publication_rerun'] = reproduced

formula_counts = Counter()
distinct = set()
distinct_with_complements = set()
for a in range(64):
    for b in (0, 1):
        order, codes = constructor.affine_program(a, b)
        assert sorted(order) == list(range(6)) and len(codes) == 6 and all(0 <= c < 16 for c in codes)
        values = [expected(x, a, b) for x in range(64)]
        assert [simulate(x, order, codes) for x in range(64)] == values
        assert sum(values) == (32 if a else 64 * b)
        formula_counts['affine_including_constants'] += 1
        if a:
            distinct_with_complements.add(packed(values))
            if not b:
                distinct.add(packed(values))
for pair in itertools.combinations(range(6), 2):
    for a in range(64):
        for b in (0, 1):
            values = [expected(x, a, b, pair) for x in range(64)]
            outside = any((a >> k) % 2 for k in range(6) if k not in pair)
            order, codes = constructor.quadratic_program(*pair, a, b)
            assert sorted(order) == list(range(6)) and len(codes) == 6 and all(0 <= c < 16 for c in codes)
            assert [simulate(x, order, codes) for x in range(64)] == values
            assert sum(values) == 32 if outside else sum(values) in (16, 48)
            formula_counts['balanced_quadratic' if outside else 'excluded_local_quadratic'] += 1
            if outside:
                distinct_with_complements.add(packed(values))
                if not b:
                    distinct.add(packed(values))
assert len(distinct) == 963 and len(distinct_with_complements) == 1926
results['formula_exhaustion'] = {'counts': dict(formula_counts), 'inputs_per_formula': 64,
                                'unique_without_constants': len(distinct), 'unique_with_constants': len(distinct_with_complements)}

example_ones = [x for x in range(64) if expected(x, 7, 0, (0, 1))]
results['example'] = {'full_accepted': len(example_ones), 'sample_accepted_words': sorted(set(example_ones) & set(canonical)),
                      'error': str(Fraction(1, 2) - Fraction(2, 11)),
                      'excess_over_allowance': str(Fraction(7, 22) - Fraction(1, 4))}
assert results['example']['sample_accepted_words'] == [27, 43]

# Independent syndrome mapping via binary matrix dot products, not XOR-pair counting.
low_vectors = [(0,) * 11]
for weight in (1, 2):
    for positions in itertools.combinations(range(11), weight):
        low_vectors.append(tuple(int(i in positions) for i in range(11)))
distribution = Counter()
zero_counts = set()
for columns in itertools.combinations(range(1, 16), 11):
    rows = [tuple((column // (2**r)) % 2 for column in columns) for r in range(4)]
    counts = Counter()
    for vector in low_vectors:
        syndrome = sum((sum(v * h for v, h in zip(vector, row)) % 2) * (2**r) for r, row in enumerate(rows))
        counts[syndrome] += 1
    zero_counts.add(counts[0])
    for syndrome in range(1, 16):
        distribution[counts[syndrome]] += 1
assert zero_counts == {1}
assert distribution == Counter({4: 12600, 5: 7560, 6: 315})
results['independent_syndromes'] = {'column_sets': math.comb(15, 11), 'syndrome_cases': sum(distribution.values()),
                                   'weight_at_most_two_vectors_per_set': len(low_vectors),
                                   'nonzero_syndrome_representation_distribution': dict(sorted(distribution.items())),
                                   'zero_syndrome_low_vectors': 1}

affine = {tuple(expected(x, a, b) for x in canonical): (a, b) for a in range(64) for b in (0, 1)}
weights = Counter(map(sum, affine))
products = []
for pair in itertools.combinations(range(6), 2):
    h = tuple(bits(x)[pair[0]] * bits(x)[pair[1]] for x in canonical)
    if h in affine:
        continue
    corrections = [(a, b) for ev, (a, b) in affine.items() if sum((v + w) % 2 for v, w in zip(h, ev)) <= 2]
    local = [(a, b) for a, b in corrections if not any((a >> k) % 2 for k in range(6) if k not in pair)]
    cells = Counter((bits(x)[pair[0]], bits(x)[pair[1]]) for x in canonical)
    assert len(corrections) >= 4 and len(local) <= 3 and len(cells) == 4
    products.append({'lsb0_pair': list(pair), 'low_coset': len(corrections), 'low_local': len(local),
                     'cell_sizes_00_01_10_11': [cells[cell] for cell in itertools.product((0, 1), repeat=2)]})
assert len(affine) == 128 and min(w for w in weights if w) == 3
results['canonical_code'] = {'distinct_affine_evaluations': len(affine), 'dimension': int(math.log2(len(affine))),
                             'weight_enumerator': dict(sorted(weights.items())), 'outside_products': products}

compositions = 0
local_maximum = 0
for cells in itertools.product(range(1, 9), repeat=4):
    if sum(cells) != 11:
        continue
    local_weights = [n for cell in cells for n in (cell, 11 - cell)]
    low_count = sum(n <= 2 for n in local_weights)
    assert low_count <= 3
    local_maximum = max(local_maximum, low_count)
    compositions += 1
assert compositions == math.comb(10, 3) == 120
results['cell_size_exhaustion'] = {'positive_compositions_of_11': compositions, 'max_low_local': local_maximum}

targeted = []
for name, support in [('all_odd', list(range(1, 22, 2))), ('all_even', list(range(0, 22, 2))), ('canonical', canonical)]:
    witness = constructor.witness(support)
    targeted.append({'case': name, 'kind': witness['formula']['kind'], 'sample_accepted': witness['sample_accepted'],
                     'full_accepted': witness['full_accepted'], 'exact_error': witness['exact_error'], 'formula': witness['formula']})
results['targeted_witnesses'] = targeted

base = constructor.witness(canonical)
orders = [canonical[i:] + canonical[:i] for i in range(11)] + [list(reversed(canonical))]
for support in orders:
    witness = constructor.witness(support)
    assert witness['formula'] == base['formula'] and witness['function_mask'] == base['function_mask']
results['support_order_invariance'] = {'orders_checked': len(orders), 'same_formula_and_mask': True}

invalid = [canonical[:-1], canonical[:-1] + [canonical[0]], canonical[:-1] + [64], canonical[:-1] + [-1], canonical[:-1] + [True], canonical[:-1] + [1.0]]
rejected = 0
for support in invalid:
    try:
        constructor.witness(support)
    except AssertionError:
        rejected += 1
assert rejected == len(invalid)
results['default_validation'] = {'invalid_inputs': len(invalid), 'rejected': rejected}

truncated = constructor.execute_and_verify(list(range(1, 22, 2)), [0], [6], {'kind': 'affine', 'a_mask_lsb0': 1, 'b': 0})
results['verifier_structure_gap'] = {'one_read_program_accepted_by_helper': True, 'returned_order': truncated['order_x1_msb'],
                                    'valid_generated_programs_exhaustively_checked_separately': True}
optimized = json.loads(subprocess.check_output([sys.executable, '-O', str(BASE / 'evidence/eleven_point_obstruction.py'), '--support'] + ['1'] * 11))
results['optimization_validation_gap'] = {'optimized_cli_accepted_eleven_repetitions_of_one': True,
                                         'sample_accepted': optimized['sample_accepted'], 'exact_error': optimized['exact_error']}

complement_errors = []
for k in range(12):
    e1 = abs(Fraction(k, 11) - Fraction(1, 2))
    e2 = abs(Fraction(11-k, 11) - Fraction(1, 2))
    assert e1 == e2
    if k <= 2 or k >= 9:
        assert e1 >= Fraction(7, 22)
    complement_errors.append(str(e1))
results['complements'] = {'all_twelve_acceptance_counts_checked': True, 'exact_errors_k_0_through_11': complement_errors}
results['support_universe'] = math.comb(64, 11)
(OUT / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
