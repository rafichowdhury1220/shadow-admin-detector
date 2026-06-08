# Shadow Admin Detector

A concise project that demonstrates a solution architect's thinking and an IAM engineer's implementation for detecting "shadow admins" — accounts that have effective administrative privileges without an explicit Admin role.

## Highlights

- Design-first architecture notes in [architecture.md](architecture.md).
- Small, readable Python implementation in `src/`.
- Run the detector against a minimal sample graph in `data/sample_graph.json`.

## Quick start

Install (optional virtual env) and run the sample:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.cli data/sample_graph.json
```

Expected output: a short list of detected shadow admins with a short explanation.

## What to look for (for recruiters)

- `architecture.md`: narrative showing architect-level tradeoffs, threat model, and design rationale.
- `src/`: clean, testable modules (`PermissionGraph`, `analyzer`) that show practical engineering.
- `README.md`: small runnable demo so reviewers can try it in seconds.

## Next steps

- Add more advanced policies, role/permission scoring, and visualization (Graphviz / networkx).
- Integrate with cloud provider IAM exports and GitHub Actions for CI.
