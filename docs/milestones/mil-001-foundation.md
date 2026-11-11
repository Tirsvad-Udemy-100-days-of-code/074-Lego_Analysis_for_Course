# MIL-001 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [1ee907b] |

---

## Purpose

Decides whether the repository is set up well enough to hold code: Python project configuration, ignore rules, source data, set-up instructions and a public description.

## Deliverable

A repository with `pyproject.toml`, a Python `.gitignore`, the lecture data and images, a README skeleton with the `.venv` guide, a clean opengrep scan and a repository description with topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` succeeds in a fresh `.venv` on Python 3.13 | Exit code 0 | Any error |
| 2 | `data/` holds colors.csv, sets.csv and themes.csv | All three files present | A file is missing |
| 3 | opengrep scan of the repository reports no findings | 0 findings | Any finding |
| 4 | Repository has a description and at least five topics on the git host | Both set | Either missing |
| 5 | `.env` is ignored by git | `git check-ignore .env` prints it | Not ignored |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 5 and 6, success criteria 5 and 6 | CN-005, CN-006 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-11 — inside the Business Case constraint (completion by 2026-11-12).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Configure the project for Python 3.13 or newer with pandas and matplotlib as runtime dependencies and pytest, jupyter and nbconvert as development extras, so S02 and S03 can install it with one command. | No |  |
| 2 | Add Python .gitignore | Ignore `.venv`, caches, notebook checkpoints and `.env`, so secrets and build output never reach the repository. | No |  |
| 3 | Add lecture data and images | Place colors.csv, sets.csv and themes.csv in `data/` and the lecture images in `assets/`, and record their source in the README, so the analysis runs offline. | No |  |
| 4 | Create package skeleton and smoke test | Add `src/lego_analysis/__init__.py` and a first test under `tests/` so the test command runs from the first milestone. | No |  |
| 5 | Write the .venv set-up guide | Document creating and activating `.venv`, `python -m pip install --upgrade pip` and installing the project, in the README skeleton built from the framework template. | No |  |
| 6 | Set repository description and topics | Use the git host's API with the repository token from `.env` (never printed) to set the description and topics. | No |  |
| 7 | Run opengrep before pushing | Scan with `~/.opengrep/cli/latest/opengrep.exe` before each push and record the command in the README. | No |  |

---

[BC-001]: ../business-case.md
[1ee907b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/074-Lego_Analysis_for_Course/commit/1ee907ba62907d8d6db910d9c4ecdc94ee8ad9d0
