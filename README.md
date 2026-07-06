# Metric Contract Check

![Metric Contract Check cover](assets/readme-cover.svg)

Validate metric names and event contracts before analytics changes ship.

## The rule file is the product

- `missing-owner` (high): metric ownership is missing. Fix: Assign an owning team before accepting the metric..
- `currency-unit-risk` (medium): money metric may not declare units. Fix: Declare currency and scale explicitly..
- `high-cardinality-tag` (low): high-cardinality tag detected. Fix: Remove per-user tags or route to logs instead of metrics..

Everything else in the repo exists to feed records into those checks and render the answer in a way a person can act on.

## Shell session

```bash
git clone https://github.com/mertefekurt/metric-contract-check.git
cd metric-contract-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
metric-contract-check examples/sample.txt
metric-contract-check examples/sample.txt --json
```

## Repository shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
