"""Exact width-two ordered read-once Boolean-function oracle; stdlib only.

Truth table bit x is f(x), with the first input bit most significant.
Backward closure stores unordered pairs of functions jointly computable from
the two possible states of one shared suffix program. The terminal pairs are
(0,0), (0,1), (1,1), covering arbitrary final accepting subsets up to relabeling.

Given a jointly realizable pair (a,b) on r suffix bits, each preceding state
can select a or b independently for input0 and input1. Its new truth table is
lo | (hi << 2**r). Any two of these four tables form a jointly realizable pair.
Conversely every program's preceding layer has exactly this form. This proves
the recurrence exhausts the model, without enumerating 16**n full programs.

Equivalent characterization: at every prefix cut, at most two distinct suffix
residual truth functions occur. Necessity follows from the state count.
For sufficiency use these residuals as states, their restrictions as the next
transitions, and the constant residual1 as the accepting terminal state.

No novelty or general derandomization result is claimed.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path


def residual_widths(mask, n):
    widths = []
    for prefix_bits in range(n + 1):
        chunk_size = 1 << (n - prefix_bits)
        chunk_mask = (1 << chunk_size) - 1
        residuals = {(mask >> (prefix * chunk_size)) & chunk_mask
                     for prefix in range(1 << prefix_bits)}
        widths.append(len(residuals))
    return widths


def enumerate_functions(n=6):
    if n < 1:
        raise ValueError('n must be positive')
    pairs = {(0, 0), (0, 1), (1, 1)}
    stages = []
    for suffix_bits in range(1, n):
        shift = 1 << (suffix_bits - 1)
        next_pairs = set()
        for a, b in pairs:
            candidates = sorted({lo | (hi << shift)
                                 for lo in (a, b) for hi in (a, b)})
            next_pairs.update(combinations_with_replacement(candidates, 2))
        pairs = next_pairs
        stages.append({'suffix_bits': suffix_bits, 'joint_pairs': len(pairs),
                       'distinct_functions': len({f for pair in pairs for f in pair})})
    shift = 1 << (n - 1)
    functions = sorted({lo | (hi << shift) for a, b in pairs
                        for lo in (a, b) for hi in (a, b)})
    return functions, stages


def verify_support(support, functions, n=6):
    if (not support or len(set(support)) != len(support)
            or any(type(x) is not int or x < 0 or x >= 1 << n for x in support)):
        raise ValueError('Support must contain distinct integers in the input domain.')
    full_size = 1 << n
    size = len(support)
    worst = Fraction(-1)
    witness = None
    # Explicit rational sample/full means, separate from bitcount error formulas.
    for f in functions:
        sampled = sum((f // 2**x) % 2 for x in support)
        full = sum((f // 2**x) % 2 for x in range(full_size))
        error = abs(Fraction(sampled, size) - Fraction(full, full_size))
        if error > worst:
            worst = error
            witness = {'function_mask': f, 'sample_accepted': sampled,
                       'full_accepted': full, 'residual_widths': residual_widths(f, n)}
    return {'support': sorted(support), 'support_size': size,
            'uniform_on_distinct_inputs': True, 'functions_checked': len(functions),
            'maximum_error': str(worst), 'meets_error_one_quarter': worst <= Fraction(1, 4),
            'witness': witness}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate-json', type=Path,
                        help='JSON list of selected integers or object with a support list')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    functions, stages = enumerate_functions(6)
    assert len(functions) == 18664
    assert stages[2]['distinct_functions'] == 88  # Earlier three-bit calibration.
    assert all(max(residual_widths(f, 6)) <= 2 for f in functions)
    full_mask = (1 << 64) - 1
    assert {f ^ full_mask for f in functions} == set(functions)
    oracle_path = root / 'method_oracle_functions.json'
    oracle_path.write_text(json.dumps(functions) + '\n')
    report = {
        'model': 'Six ordered bits read once; two states per layer; fixed start0; arbitrary final accepting subset.',
        'method': 'Backward closure of jointly realizable unordered residual-function pairs.',
        'equivalent_characterization': 'At every prefix cut, at most two distinct suffix residual truth functions.',
        'stages': stages, 'input_bits': 6, 'distinct_functions': len(functions),
        'all_output_functions_pass_residual_characterization': True,
        'complement_closed': True,
        'uniform_support_lower_bound_at_error_one_quarter': 8,
        'lower_bound_argument': 'Affine parities are width2. At most six selected points lie in an affine hyperplane over F2, giving parity error1/2. Seven selected points either also lie in a hyperplane, or are affinely independent; in the latter case an affine parity can isolate one point, giving error|1/7-1/2|=5/14. Therefore every support of size<=7 fails.',
        'lower_bound_limit': 'This proves only support>=8, not optimality of any size16 construction.',
        'function_list_file': oracle_path.name,
        'function_list_sha256': hashlib.sha256(oracle_path.read_bytes()).hexdigest(),
        'status': 'Exact finite enumeration with elementary completeness argument; no novelty claim, no formal proof assistant.'
    }
    if args.candidate_json:
        candidate = json.loads(args.candidate_json.read_text())
        support = candidate['support'] if isinstance(candidate, dict) else candidate
        report['candidate_verification'] = verify_support(support, functions)
    (root / 'method_oracle_output.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
