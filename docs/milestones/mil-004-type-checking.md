# MIL-004 Type checking, packaging fixes and notebook answers

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6bcfb5d] |

---

## Purpose

Decides whether the code passes a strict type check, the packaging metadata uses the current setuptools licence form, and the notebook answers the five assignment questions both where the answer is found and in its introduction, as requested by S01 after the first run, and the notebook's images load.

## Deliverable

`pyproject.toml` with mypy configuration and an SPDX licence, source and tests that pass `mypy --strict`, a notebook whose introduction states the five answers and whose challenge sections each end with their answer, and a delta review record.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m mypy` (strict) reports no errors on `src` and `tests` | 0 errors | Any error |
| 2 | `pip install -e .[dev]` prints no licence deprecation warning | No warning | Warning shown |
| 3 | `pytest` passes, including a test that the five answers in the notebook introduction match the computed values | All tests pass | Any failure |
| 4 | The notebook has an answer cell after each of the five questions' challenge cells and an answers list in the introduction | Both present | Either missing |
| 5 | opengrep scan reports no findings | 0 findings | Any finding |
| 6 | Every local image referenced by the notebook exists relative to the notebook, and JupyterLab started in `notebooks/` or in the repository root shows them | Test passes | A path is broken |
| 7 | Python code re-reviewed against `QC-PY` and recorded as an RC | Verdict Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | The code and documents being changed exist after MIL-003 |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objective 3 (tests and correctness), success criterion 6 (dependencies stay minimal: mypy is a development dependency) | CN-001, CN-006 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the Business Case constraint (completion by 2026-11-12).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add mypy to the project | Add `mypy` and `pandas-stubs` to the `dev` extra and a strict `[tool.mypy]` section to `pyproject.toml`, so the type checker runs the same way for everyone (action item of RC-007, criterion 12). | No | |
| 2 | Fix the strict mypy findings | Fix the three findings of `mypy --strict src tests`: the `float(...)` argument in `application/report.py` and two `len(...)` calls in `tests/unit/test_presentation_charts.py`, without changing behaviour. | No | |
| 3 | Fix the setuptools licence deprecation | Replace the table form of `project.license` with the SPDX string `AGPL-3.0-only` plus `license-files`, and require `setuptools>=77`, before the deprecation removes support on 2027-02-18. | No | |
| 4 | Document the type check | Add the `python -m mypy` command to the README Tests section. | No | |
| 5 | Answer the five questions where they are found | Add a markdown answer cell after each challenge that resolves one of the five questions (largest set, first year and sets, theme with most sets, sets and themes per year, parts per set), written from the executed outputs. | No | |
| 6 | Put the five answers in the notebook introduction | Add an "Answers at a glance" list after the question list in the introduction, with a test that its numbers equal the computed values so it cannot drift. | No | |
| 7 | Fix the missing notebook images | The notebook's `<img>` tags point to `../assets/`, which JupyterLab cannot serve when it is started inside `notebooks/` (S01's session shows no images). Move the lecture images to `notebooks/assets/`, point the tags at `assets/`, update the README, and add a test that every local image the notebook references exists next to it. | No | |
| 8 | Re-review the code against QC-PY | Record a delta re-review of criteria 12 and 13 of `qc-programming-python.md` and close the matching action item of RC-007. | No | |

---

[BC-001]: ../business-case.md
[MIL-003]: ./mil-003-notebook-and-docs.md
[6bcfb5d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/commit/6bcfb5d5c10e7f5512493b75214bcf1baa512314
