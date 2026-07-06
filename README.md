# Metric Contract Check

<p align="center">
  <img src="assets/readme-cover.svg" alt="Metric Contract Check cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-4b5563?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-2563eb?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-16a34a?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-dc2626?style=flat-square)

Validate metric names and event contracts before analytics changes ship.

## The short version

`metric-contract-check` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-owner` | high | metric ownership is missing |
| `currency-unit-risk` | medium | money metric may not declare units |
| `high-cardinality-tag` | low | high-cardinality tag detected |

## Usage

```bash
python -m pip install -e ".[dev]"
metric-contract-check examples/sample.txt
metric-contract-check examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m metric_contract_check --help
```
