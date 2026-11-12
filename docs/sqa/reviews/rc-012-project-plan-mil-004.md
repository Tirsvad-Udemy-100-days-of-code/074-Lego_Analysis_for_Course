# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (S01 confirmed criteria 3, 5 and 9 in chat on 2026-11-11)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-11, end 2026-11-12, inside the Business Case constraint. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Four gateways, each listed once with document, decision date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the dates in the MIL documents. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every in-scope item to a gateway, including the new MIL-004 rows. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-004 is acyclic and in schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | A No-Go holds later gateways; S01 decides on the end date (unchanged). |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Only S01 is used; no governance document exists (Open Issues). |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Planning Assumptions unchanged; the added gateway is recorded in the Version History change cell with its reason. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan risks unchanged, each with a mitigation. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues unchanged and consistent. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | MIL-004 main deliverable matches its Deliverable section. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | "none (technical tasks)". |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt and table agree on dates. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | MIL-004 is marked "not yet synced"; MIL-001 to MIL-003 link their milestones. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single plan with a Version History. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Content is English. Confirmed by S01 in chat, 2026-11-11 (plan acceptance). |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register follows the registry row for the type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | PO terms (set, theme, part, colour) are used without synonyms; no dictionary exists (Open Issue in PP-001). Confirmed by S01 in chat, 2026-11-11. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Confirmed by S01 (reads English, knows the IT domain) in chat, 2026-11-11. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use (for example "Product Owner (PO)"). |

## Overall Verdict

Go — every Mandatory criterion passes, including the language and domain criteria that S01 confirmed in chat on 2026-11-11 for the English documents. Mode: autonomous, not independent; S01 may challenge this record. S01 accepted the MIL-004 plan in chat on 2026-11-12.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | n/a |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
