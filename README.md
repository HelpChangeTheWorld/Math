# Math Frontiers — Work Round 2 research pack

Start with `Math_Frontiers_Work_Round_2.md`. It contains the results, all 100 bounded work records, their limits, and the complete finite sampler proof. `all_100_work_records.json` holds the same records in machine-readable form. These are actual computations and derivations performed in an AI workflow. No major conjecture resolution or established novelty is claimed.

## Reproduce the main result

The verification of the eight-point sampler uses Python's standard library. From the extracted archive directory, run:

```bash
python3 method_oracle.py --candidate-json sampler_candidate_8.json
```

This regenerates all 18,664 functions by the documented backward recurrence and checks the candidate with exact rational arithmetic. The expected maximum error is `1/4`. The elementary lower-bound proof in `sampler_optimality_proof.md` excludes every support of size at most seven. Thus the exact finite optimum is eight. Running the oracle updates its own output files; preserve an untouched copy if comparing archive hashes.

`sampler_search.py` uses a different complete enumeration and a mixed-integer solver to find candidates. It requires NumPy and SciPy (this run used SciPy 1.17.0). It is optional for verification:

```bash
python3 sampler_search.py 8 90
```

The last argument is a solver time limit in seconds. A later solver run may choose a different support or time out. The saved candidate's exact verification and the lower-bound proof do not depend on the solver proving optimality.

## Other computations

The calculation scripts use Python 3 and the standard library, except for the optional sampler search above. Outputs are saved alongside their scripts. Some exhaustive runs may take minutes.

| Work | Runner | Main saved evidence |
|:--|:--|:--|
| Targets 1–5 | `captain_calculations.py`, then `captain_verify_and_refine.py` | `captain_*.json` |
| Targets 6–32 | `number_compute.py` | `number_6.json` through `number_32.json` |
| Graph constructions and enumerations | `discrete_graphs.py` | `discrete_graph_results.json` |
| Complementary sequences and equality families | `discrete_algebra.py` | `discrete_algebra_results.json` |
| Discrete geometry | `discrete_geometry.py` | `discrete_geometry_results.json` |
| Finite search landscapes | `discrete_landscapes.py` | `discrete_landscape_results.json` |
| Additional discrete counts and flows | `discrete_counts_flows.py` | `discrete_count_flow_results.json` |
| Targets 56–80 | `geometry_calculations.py` | `geometry_calculations.json`, `geometry_interpolation_certificates.json` |
| Targets 86, 93, 100 | `computation_priority.py` | `computation_priority_results.json` |
| Other targets 81–100 | `computation_batch.py` | `computation_batch_results.json` |
| Separate audit of 93 and 100 | `captain_priority_audit.py` | `captain_priority_audit.json`, `captain_strassen_minor_certificates.json` |

Narrative records and proof supplements explain arguments that are not exhausted by code execution. Not every record is a new theorem: many are calibrations, finite witnesses, or failed implications. Fixed random seeds and exact models are recorded in the relevant scripts and outputs. Floating-point calculations are explicitly limited in the records; agreement at two precisions alone is not treated as an error certificate.

The audit of #93 computes a nonzero 3×3 minor of an actual matrix flattening for each of 18,424 triples. This certifies tensor rank three for every triple and excludes any exact three-to-two replacement with all other terms fixed, including over complex coefficients. It says nothing about changing more terms or another full decomposition.

The reviewers are other members of the same AI workflow, not external human referees. Independent enumeration or calculation means a distinct derivation or implementation where identified, not institutional endorsement.

## Integrity and report assembly

`SHA256SUMS.txt` lists SHA-256 hashes for every other archived file at delivery. `assembly_validation.json` records that IDs 1–100 occur exactly once and that required fields and direct evidence filenames were checked. Archive integrity was also checked when the pack was built. These packaging checks do not prove every mathematical statement.

To regenerate the report and pack from the domain logs:

```bash
python3 build_work_report.py --output-dir regenerated_output
```

The report builder does not rerun experiments. Some metadata, such as elapsed runtime, can differ on reproduction. The five domain record files are `millennium_work.json`, `number_work.json`, `discrete_work.json`, `geometry_work.json`, and `computation_work.json`.
