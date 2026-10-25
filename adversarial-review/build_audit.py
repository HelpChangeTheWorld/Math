from collections import Counter
from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parent
names = ['algebra', 'model', 'computation', 'literature', 'editorial']
all_checks = []
documents = []
for name in names:
    data = json.loads((root / (name + '.json')).read_text())
    assert len(data['checks']) == 20, (name, len(data['checks']))
    for check in data['checks']:
        assert all(isinstance(check.get(k), str) and check[k].strip()
                   for k in ['id', 'question', 'verdict', 'evidence'])
        assert check['verdict'] in ['pass', 'fail', 'limitation', 'unresolved']
    documents.append((name, data))
    all_checks.extend(data['checks'])
assert len(all_checks) == 100 and len({c['id'] for c in all_checks}) == 100

parts = [(root / 'ASSESSMENT.txt').read_text()]
parts.append('\nONE HUNDRED STRUCTURED CHECKS\n')
number = 0
for name, data in documents:
    parts.append('\n' + name.upper() + '\n' + data['reviewer'] + '\n')
    for check in data['checks']:
        number += 1
        parts.append(f"{number:03d} | {check['id']} | {check['verdict'].upper()}\n"
                     + check['question'] + '\n' + check['evidence'] + '\n')
    summary = data['summary'] if isinstance(data['summary'], str) else json.dumps(data['summary'], ensure_ascii=False, indent=2)
    parts.append('Reviewer assessment\n' + summary + '\n')
    for source in data.get('sources', []):
        parts.append('Source\n' + json.dumps(source, ensure_ascii=False) + '\n')
report = root / 'Eleven_Inputs_100_Check_Adversarial_Review.txt'
report.write_text('\n'.join(parts), encoding='utf-8')

files = [root / 'ASSESSMENT.txt', report, root / 'build_audit.py', root / 'README.txt']
files += [root / (name + '.json') for name in names]
files += [root / 'computation_work/independent_checks.py', root / 'computation_work/results.json',
          root / 'additional_witness_check.py', root / 'additional_witness_check.json']
entries = {p.relative_to(root).as_posix(): p for p in files}
entries['source_publication.zip'] = root.parent / 'output/Stakeholders_Letter_Eleven_Inputs_Publication_Pack.zip'
manifest = ''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + name + '\n' for name,p in entries.items())
manifest_path = root / 'SHA256SUMS.txt'
manifest_path.write_text(manifest)
entries['SHA256SUMS.txt'] = manifest_path
output = root.parent / 'output' / 'Eleven_Inputs_100_Check_Adversarial_Review.zip'
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name, path in entries.items():
        z.write(path, name)
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    for line in manifest.splitlines():
        digest, filename = line.split('  ', 1)
        assert hashlib.sha256(z.read(filename)).hexdigest() == digest
print(json.dumps({'checks': len(all_checks), 'ratings':dict(Counter(c['verdict'] for c in all_checks)),
                  'archive':str(output),'bytes':output.stat().st_size,'verified':True}, indent=2))
