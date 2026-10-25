ADVERSARIAL REVIEW PACKAGE

Start with ASSESSMENT.txt for the coordinating assessment, or
Eleven_Inputs_100_Check_Adversarial_Review.txt for the complete readable record.
The five JSON files preserve each reviewer's twenty questions and evidence.
This is five AI sessions performing one hundred checks, not one hundred people
or one hundred independent experiments. No review ratings establish a calibrated
probability of correctness or substitute for outside human peer review.

The publication being reviewed is included, unchanged, as source_publication.zip.
To reproduce the computation audit, extract that inner ZIP into a directory
named source_publication beside this README. Then, using Python 3.10 or newer:

python3 computation_work/independent_checks.py

Alternatively pass the path to an already extracted publication directory:
python3 computation_work/independent_checks.py /path/to/extracted/publication

The original recorded output is computation_work/results.json. The audit code
was changed only to accept a portable publication-directory argument; the
mathematical checks are unchanged. Its deliberate negative tests show limitations
of the original helper and of running assertion-based checks with Python -O.
Run the published verification commands normally, without -O.

The coordinating session separately reproduced the additional finite observations:
python3 additional_witness_check.py

Its saved output is additional_witness_check.json. It checks the larger 157/352
discrepancy on the displayed sample, the parity maximum of 5/22, and the maximum
of 7/22 for the restricted 963-function family. These are exact finite checks,
not a full-class optimum or a twelve-point construction.

Some review JSON files retain the original session-local paths and source
retrieval references as historical provenance. Public source URLs are provided
in literature.json; internal retrieval references are not public hyperlinks.
Some independent checks described by other reviewers were executed inline and
their complete code is not included. Their descriptions are reviewer reports,
not separately authenticated certificates.

SHA256SUMS.txt records every included evidence file and the unchanged publication
ZIP. The article itself was not modified during this review.
