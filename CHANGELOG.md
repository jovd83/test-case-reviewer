# Changelog

All notable changes to this repository are documented here. The format follows Keep a Changelog, and the repository uses semantic versioning.

## [2.0.0] - 2026-09-27

`test-case-reviewer` replaces two skills: `agentic-bdd-test-case-mentor` (1.1.0) and `tss-test-case-reviewer` (0.1.8). Both reviewed drafted tests against requirements with the same discipline, one for classic test cases and one for Gherkin. This repository continues the history of the first and carries the full history of the second.

### Added
- One skill with two tracks: classic test cases (the tss review workflow, suite protocol, scoring and graded examples) and BDD/Gherkin (the mentor's review, rewrite, generate and hybrid modes).
- A shared intake: artifact track, mode, one oracle order, and the rule that implementation code is never the primary oracle.
- `references/test-cases/`, carried over from `tss-test-case-reviewer`, and the tss trigger evals, merged into `eval/trigger-evals.json` (38 cases).
- `author` and `version` in the SKILL.md metadata.

### Changed
- One severity scale for both tracks: `Critical`, `High`, `Medium`, `Low`. The BDD track's `Major` becomes `High`, `Minor` becomes `Low`, and `Medium` is new.
- BDD files moved to `references/bdd/`, `examples/bdd/` and `assets/bdd-*`; `references/bdd-quality-rules.md` is now `references/bdd/quality-rules.md`.
- `dispatcher-layer` is `feedback` (review), no longer `information`.
- README rewritten to the house standard.

### Removed
- The shared-memory integration notes: the shared-memory skill is retired.
- The separate `tss-test-case-reviewer` skill name. Callers should use `test-case-reviewer`.

## History of agentic-bdd-test-case-mentor

### [1.0.1] - 2026-04-30

#### Changed
- Trimmed `SKILL.md` frontmatter to fit the 1000-character dispatcher limit.

### [1.1.0] - 2026-03-26

#### Changed
- Rewrote `SKILL.md` into a tighter operating contract with clearer mode selection, oracle handling, confidence rules, guardrails and response expectations.
- Reworked the supporting references into intake, review workflow, quality heuristics, structure rules, scoring and output contracts.
- Upgraded the README and contribution guidance.
- Improved `agents/openai.yaml`.

#### Fixed
- The feature template no longer implies default metadata tags.
- Strong artifacts are no longer forced into artificial findings by the examples and evals.
- Packaging aligned with the Agent Skills specification.

#### Added
- `references/intake-and-decision-flow.md`, rewrite and formal-report examples, `eval/forward-test-matrix.md`, `scripts/validate_skill_repo.py`, `.github/workflows/validate.yml`.

### [1.0.0] - 2026-03-26

#### Added
- Initial public repository packaging: core skill, references, templates, examples and evaluation artifacts.

## History of tss-test-case-reviewer

### [0.1.8] - 2026-03-26
- Simplified `SKILL.md` frontmatter; added tables of contents to the longer example references.

### [0.1.7] - 2026-03-26
- Normalized wording across the example references; fixed a text-encoding issue in `examples-mini-review-reports.md`.

### [0.1.6] - 2026-03-26
- Added `references/examples-bad-input-artifacts.md` (10 poor-quality review inputs).

### [0.1.5] - 2026-03-26
- Added `references/examples-mini-review-reports.md` (graded mini review reports).

### [0.1.4] - 2026-03-26
- Added `references/examples-review-comments.md` (graded review-comment examples).

### [0.1.3] - 2026-03-26
- Added `references/examples-test-case-quality.md` (graded test-case examples).

### [0.1.2] - 2026-03-26
- Moved trigger intent into the frontmatter description; regenerated `agents/openai.yaml`.

### [0.1.1] - 2026-03-26
- Tightened marketplace metadata; expanded the trigger evals with near-miss prompts; added publishing guidance.

### [0.1.0] - 2026-03-26
- Initial release: review workflow, test case protocol, test suite protocol, report template, trigger evals.
