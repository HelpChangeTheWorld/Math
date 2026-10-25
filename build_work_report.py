"""Assemble the completed 100-item work log and reproducibility archive."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import re
import shutil
import zipfile

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
DEST = BASE / 'output' / 'math'
INPUTS = ['millennium_work.json', 'number_work.json', 'discrete_work.json',
          'geometry_work.json', 'computation_work.json']
LABELS = {
    'finite_verified': 'Finite computation verified',
    'proved_restricted_statement': 'Restricted statement proved',
    'failed_approach': 'Attempted approach failed',
    'unresolved_attempt': 'Attempt remains unresolved',
}
REQUIRED = {'id', 'title', 'attempt', 'result', 'evidence', 'status',
            'scope_limit', 'next_decision', 'source_urls'}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=DEST)
    dest = parser.parse_args().output_dir.resolve()
    records = []
    for name in INPUTS:
        data = json.loads((HERE / name).read_text())
        assert isinstance(data, list), name
        records.extend(data)
    records.sort(key=lambda x: x['id'])
    assert [r['id'] for r in records] == list(range(1, 101))
    for r in records:
        assert REQUIRED <= r.keys(), (r['id'], REQUIRED - r.keys())
        assert r['status'] in LABELS, (r['id'], r['status'])
        for field in REQUIRED - {'id'}:
            assert r[field], (r['id'], field)
        evidence_text = json.dumps(r['evidence'], ensure_ascii=False)
        for name in re.findall(r'[A-Za-z0-9_][A-Za-z0-9_.-]*\.(?:json|py|md|csv|txt)\b', evidence_text):
            assert (HERE / name).is_file(), (r['id'], name)
    (HERE / 'all_100_work_records.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n')
    counts = Counter(r['status'] for r in records)
    lines = [
        '# Math Frontiers — Work Round 2',
        '',
        'Actual mathematical attempts for all 100 catalog targets',
        '',
        '**Date:** 11 September 2026. **Team:** the simulated research team, with computations and reviews performed within this AI workflow.',
        '',
        'This round contains 100 bounded attempts: explicit arguments, exact finite enumerations, numerical experiments, and counterexamples to proposed methods. Each entry states what was attempted, what was obtained, its evidence, its precise limit, and the next decision. A completed entry means that a bounded attempt was performed; it does not mean its parent conjecture was solved.',
        '',
        '**No major catalog conjecture has been resolved by this work, and no claim of previously unknown mathematics has been established.** Several smaller questions posed in the earlier round now have exact answers. Some other entries reproduce established special cases to test whether a proposed method actually has purchase.',
        '',
        '## Results that change the next move',
        '',
        '- **#81: the six-bit sampler optimum is exactly 8.** We found eight inputs whose uniform average has error at most 1/4 against every Boolean function computed by the specified ordered, width-two program. Two different enumeration methods agree on all 18,664 functions, and exact arithmetic verifies the candidate. An elementary affine-parity argument excludes every support of seven or fewer points. This repairs the previous product construction, which failed its six-bit test.',
        '- **#93: every local three-to-two replacement is impossible in the tested construction.** All 18,424 triples in the fixed 49-term Strassen tensor-square decomposition have tensor rank exactly three. A separate audit saved a direct nonzero 3×3 flattening minor for each triple. With the other 46 terms fixed, even unrestricted rational or complex coefficients cannot compress a selected triple to two terms. Larger changes and other decompositions remain available.',
        '- **#49: every valid normalized parent in the finite extension test extends.** All 108 valid length-three periodically complementary quadruples have a length-five extension in the prescribed append model. This resolves that finite test and supplies witnesses; it does not produce Hadamard matrices at every required order.',
        '- **#53: the proposed descent rule has a certified trap.** At an explicit cube coefficient vector, every single-coordinate ±1 move increases the defect, even without a coefficient-box restriction. A saved escape path reaches a valid flow with a maximum defect of two, from an initial defect of one. The exact required barrier increase is one for this move rule; a general monotone-descent argument using it fails.',
        '- **#100: the selected first-order perturbation has an interior Melnikov zero.** Exact endpoint integrals are 6/5 and 6/35, so the ratio moves from zero near the center to 1/7 at the separatrix. Continuity gives an interior ratio of 1/10. A simple zero, an actual perturbed cycle, and a global cycle bound have not been established.',
        '',
        '## Coverage and meaning of the labels',
        '',
        '| Label | Entries | What the label establishes |',
        '|:--|--:|:--|',
    ]
    meanings = {
        'finite_verified': 'An exact finite calculation for the stated model; no extension beyond that model is implied.',
        'proved_restricted_statement': 'A displayed argument for a special case or obstruction, often using established theorems; novelty is unclaimed.',
        'failed_approach': 'A calculation or witness defeats the particular attempted method or benchmark.',
        'unresolved_attempt': 'An actual attempt was made, but the claimed implication or a rigorous certificate remains missing.',
    }
    for key, label in LABELS.items():
        lines.append(f'| {label} | {counts[key]} | {meanings[key]} |')
    lines += [
        '',
        'The labels describe different types of output, not a ranking of conjectures by tractability. Counts do not measure new discoveries. Numerical observations are identified where they occur. The separate checks of #81, #93, and #100 used other members of this same AI workflow; they are not external peer review or proof-assistant certification.',
        '',
        '## All 100 work records',
        '',
        'Evidence filenames refer to files in the accompanying research archive. Source links provide mathematical background; they do not endorse the new calculations or establish their novelty.',
        '',
    ]
    for r in records:
        lines += [f"### {r['id']}. {r['title']}", '', f"**Status:** {LABELS[r['status']]}", '',
                  f"**Attempt performed.** {r['attempt']}", '', f"**Result.** {r['result']}", '']
        evidence = r['evidence']
        if isinstance(evidence, list):
            evidence = '; '.join(f'`{v}`' if isinstance(v, str) and (HERE / v).is_file() else str(v) for v in evidence)
        lines += [f'**Evidence.** {evidence}', '', f"**Limit.** {r['scope_limit']}", '',
                  f"**Next decision.** {r['next_decision']}", '']
        sources = r['source_urls']
        if isinstance(sources, str):
            sources = [sources]
        links = []
        for i, source in enumerate(sources, 1):
            if isinstance(source, dict):
                links.append(f"[{source.get('title', 'Background source ' + str(i))}]({source.get('url', '')})")
            else:
                links.append(f'[Background source {i}]({source})')
        lines += ['**Background.** ' + '; '.join(links), '']
    proof = (HERE / 'sampler_optimality_proof.md').read_text()
    lines += ['## Appendix: complete statement and proof for #81', '',
              '\n'.join('#' + line if line.startswith('#') else line for line in proof.splitlines()), '']
    dest.mkdir(parents=True, exist_ok=True)
    report = dest / 'Math_Frontiers_Work_Round_2.md'
    report.write_text('\n'.join(lines))
    shutil.copy2(report, HERE / report.name)
    (HERE / 'sampler_candidate_8.json').write_text('[0, 4, 13, 14, 26, 31, 33, 35]\n')
    validation = {
        'records': len(records), 'ids_exactly_1_through_100': True,
        'status_counts': dict(counts),
        'required_fields_present': True,
        'direct_evidence_file_references_checked': True,
        'claims_of_major_conjecture_resolution': 0,
        'claims_of_established_novelty': 0,
    }
    (HERE / 'assembly_validation.json').write_text(json.dumps(validation, indent=2) + '\n')
    files = [p for p in HERE.iterdir() if p.is_file() and p.suffix in {'.py', '.json', '.md', '.csv', '.txt'} and p.name != 'SHA256SUMS.txt']
    files.sort()
    manifest = HERE / 'SHA256SUMS.txt'
    manifest.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in files))
    archive = dest / 'Math_Frontiers_Work_Round_2_Research_Pack.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in files + [manifest]:
            z.write(p, p.name)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(files) + 1
    print(json.dumps({'report': str(report), 'archive': str(archive), 'archive_files': len(files)+1,
                      'archive_bytes': archive.stat().st_size, **validation}, indent=2))

if __name__ == '__main__':
    main()
