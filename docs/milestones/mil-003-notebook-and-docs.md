# MIL-003 Notebook and documentation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decides whether the notebook, README and three-language wiki, with a screenshot for every lecture step, are ready for S02 and S03.

## Deliverable

The Jupyter notebook that follows the lecture steps, nine step screenshots generated from the code, the README from the framework template and the wiki in English, Danish and Bahasa Malaysia.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `jupyter nbconvert --execute` runs the notebook | Exit code 0 | Any error |
| 2 | `docs/images/` holds nine step screenshots | Nine files | Fewer |
| 3 | `docs/wiki/` holds the same pages in en, da and ms | Same page set in three languages | A page is missing |
| 4 | README passes the framework's `check-readme.sh` | Exit code 0 | Any error |
| 5 | Wiki reviewed against QC-WIKI-001 and recorded as an RC | Verdict Go | No-Go |
| 6 | opengrep scan reports no findings | 0 findings | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The notebook and screenshots call the library |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 2, 4 and 5, success criteria 2 to 4 | CN-003, CN-005 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the Business Case constraint.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Build the notebook | Create `notebooks/Lego_Analysis_for_Course.ipynb` with the lecture's headings, HTML markup, images and code cells that call the library. | No |  |
| 2 | Generate step screenshots | A script renders one PNG per lecture step (tables and charts) into `docs/images/` from the code. | No |  |
| 3 | Test the notebook | A test executes the notebook headlessly so it cannot rot. | No |  |
| 4 | Write README | Create README from the framework template with set-up, run and test instructions and the screenshots. | No |  |
| 5 | Write English wiki | Pages that explain what each lecture step teaches, with its screenshot. | No |  |
| 6 | Write Danish wiki | The same pages in Danish (`-da`). | No |  |
| 7 | Write Bahasa Malaysia wiki | The same pages in Bahasa Malaysia (`-ms`). | No |  |
| 8 | Review wiki against QC-WIKI-001 | Record the RC and fix findings. | No |  |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-analysis-library.md
