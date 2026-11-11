# MIL-002 Analysis library

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decides whether the analysis functions are correct, tested and reviewed against the Python checklist before the notebook and the documentation depend on them.

## Deliverable

The Python package `lego_analysis` with data loading, the analysis functions that carry the assignment's names, chart functions and a command line entry point, plus a pytest suite that asserts every lecture value.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes | All tests pass | Any failure |
| 2 | Tests assert the lecture values (135 colours, 1949 with 5 sets, Star Wars with the most sets) | All assertions present and passing | A value is not asserted |
| 3 | Python code reviewed against `QC-PY` and recorded as an RC | Verdict Go | No-Go |
| 4 | opengrep scan reports no findings | 0 findings | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The package, configuration and data it builds on |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 1 and 3, success criterion 1 | CN-001, CN-004 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-11 — inside the Business Case constraint.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement data loading | `data.py` reads the three CSV files from a data directory into DataFrames so every function works on the same typed input. | No |  |
| 2 | Implement colour functions | Count unique colour names and the transparent versus opaque colours, in two ways each, as the lecture asks. | No |  |
| 3 | Implement set functions | Find the first release year, the sets of that year, the number of sets in a year and the largest sets by parts. | No |  |
| 4 | Implement per-year aggregations | `sets_by_year`, `themes_by_year` using `.agg()` and `parts_per_set`, with a helper that drops the incomplete last two years. | No |  |
| 5 | Implement theme functions | Find the Star Wars theme ids and their sets, count sets per theme and merge the counts with the theme names. | No |  |
| 6 | Implement chart functions | Line chart, two-axis line chart, scatter plot and bar chart with Matplotlib, returning figures so tests and screenshots can use them without a display. | No |  |
| 7 | Add command line entry point | `python -m lego_analysis` prints the answers to the five questions. | No |  |
| 8 | Write pytest suite | Assert every lecture value and every function's edge cases. | No |  |
| 9 | Review code against QC-PY | Review `src/` against `qc-programming-python.md` and record the RC. | No |  |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-foundation.md
