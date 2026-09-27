# Changelog

All notable changes to this skill will be documented in this file.

## [0.1.8] - 2026-03-26

### Enhanced

- Simplified `SKILL.md` frontmatter to keep only `name` and `description`, aligning more closely with the local `skill-creator` guidance
- Added lightweight tables of contents to the longer example reference files for easier progressive disclosure
- Updated `README.md` version and release commands to match the current package version

### Metadata

- Author: `jovd83`

## [0.1.7] - 2026-03-26

### Enhanced

- Normalized wording across the example reference files so they follow a more consistent quality ladder
- Rewrote `references/examples-mini-review-reports.md` to remove a text encoding issue and align its labels with the other example files
- Updated `README.md` version and release commands to match the current package version

### Metadata

- Author: `jovd83`

## [0.1.6] - 2026-03-26

### Added

- Added `references/examples-bad-input-artifacts.md` with 10 examples of poor-quality review inputs
- Linked the bad-input examples from `SKILL.md`
- Documented the new reference in `README.md`

### Metadata

- Author: `jovd83`

## [0.1.5] - 2026-03-26

### Added

- Added `references/examples-mini-review-reports.md` with graded mini review reports ranging from very weak to excellent
- Linked the mini report examples from `SKILL.md`
- Documented the new reference in `README.md`

### Metadata

- Author: `jovd83`

## [0.1.4] - 2026-03-26

### Added

- Added `references/examples-review-comments.md` with 10 graded review-comment examples ranging from very weak to excellent
- Linked the new review-comment examples from `SKILL.md`
- Documented the new example reference in `README.md`

### Metadata

- Author: `jovd83`

## [0.1.3] - 2026-03-26

### Added

- Added `references/examples-test-case-quality.md` with 10 graded examples ranging from very bad to excellent
- Linked the new examples reference from `SKILL.md` for selective loading
- Documented the new example set in `README.md`

### Metadata

- Author: `jovd83`

## [0.1.2] - 2026-03-26

### Enhanced

- Strengthened `SKILL.md` frontmatter description so more trigger intent lives where skill systems actually read it
- Replaced the body-level trigger section with a leaner scope-selection section to reduce duplicated trigger text
- Regenerated `agents/openai.yaml` with cleaner deterministic metadata based on the local `skill-creator` tooling
- Removed optional UI color metadata that was not explicitly requested
- Kept repository-facing extras while noting that they are outside the minimal core skill format

### Metadata

- Author: `jovd83`

## [0.1.1] - 2026-03-26

### Enhanced

- Tightened marketplace metadata in `agents/openai.yaml`
- Strengthened the default prompt for clearer explicit invocation
- Expanded `eval_queries.json` into a more realistic trigger test set with positive, negative, and near-miss prompts
- Added publishing guidance and suggested release commands to `README.md`

### Metadata

- Author: `jovd83`

## [0.1.0] - 2026-03-26

### Added

- Initial public release of `tss-test-case-reviewer`
- Core `SKILL.md` with structured review workflow
- Reference files for review workflow, test case protocol, test suite protocol, and report template
- `agents/openai.yaml` marketplace metadata
- `eval_queries.json` for trigger evaluation
- `README.md` with packaging and usage overview
- `LICENSE` with MIT terms

### Metadata

- Author: `jovd83`
