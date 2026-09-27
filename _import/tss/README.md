# TDD Test Case Reviewer

Structured Agent Skill for reviewing drafted software test cases and test suites before execution or automation.

## Overview

This skill performs an evidence-based QA review focused on:

- requirement traceability
- coverage completeness
- suite architecture and redundancy
- technical correctness
- standards compliance
- mentoring feedback for test authors

## Skill Metadata

- Name: `tss-test-case-reviewer`
- Display name: `TSS Test Case Reviewer`
- Version: `0.1.8`
- Author: `jovd83`
- License: `MIT`

## Repository Layout

```text
tss-test-case-reviewer/
|-- SKILL.md
|-- README.md
|-- CHANGELOG.md
|-- LICENSE
|-- eval_queries.json
|-- agents/
|   `-- openai.yaml
`-- references/
    |-- examples-bad-input-artifacts.md
    |-- examples-mini-review-reports.md
    |-- examples-review-comments.md
    |-- examples-test-case-quality.md
    |-- review-report-template.md
    |-- review-workflow.md
    |-- test-case-protocol.md
    `-- test-suite-protocol.md
```

## When to Use

Use this skill when reviewing:

- drafted test cases
- test suite hierarchy
- requirement-to-test traceability
- TSS or TDD-style test design quality
- mentoring feedback for junior testers

## Main Output

The skill produces a structured review with:

- executive summary
- findings by severity
- coverage and traceability gaps
- standards compliance issues
- coaching recommendations
- action plan

## Included Examples

The skill now includes `references/examples-test-case-quality.md` with 10 graded examples that range from very bad to excellent. Use those examples when you want the agent to explain why a test case is weak, show what better looks like, or coach a junior tester with concrete comparisons.

It also includes `references/examples-review-comments.md` with 10 review-comment examples that range from vague and unhelpful to precise, evidence-based coaching feedback.

It also includes `references/examples-mini-review-reports.md` with graded end-to-end review examples, so the skill can pattern-match against complete outputs as well as individual comments.

It also includes `references/examples-bad-input-artifacts.md` with examples of poor requirement statements, weak traceability inputs, overloaded suites, and incomplete review packages.

The example references now use a more consistent grading ladder so the skill can pattern-match quality more reliably across test cases, review comments, and mini reports.
The longer reference files now include short tables of contents so agents can preview their structure before loading the full file.

## Trigger Evaluation

Use `eval_queries.json` to test whether the skill triggers on realistic review requests and stays quiet on unrelated testing tasks such as automation authoring, planning, CI setup, or requirements drafting.

Recommended quality bar:

- at least 8 realistic positive queries
- at least 8 realistic negative queries
- include near-miss prompts that mention testing but do not ask for review

## Publishing

Suggested initial commit message:

```text
feat: publish tss-test-case-reviewer skill v0.1.8
```

Suggested annotated tag:

```text
git tag -a v0.1.8 -m "Release tss-test-case-reviewer v0.1.8"
```

Suggested push commands:

```text
git add tss-test-case-reviewer
git commit -m "feat: publish tss-test-case-reviewer skill v0.1.8"
git tag -a v0.1.8 -m "Release tss-test-case-reviewer v0.1.8"
git push origin HEAD
git push origin v0.1.8
```

## Notes

- The core skill follows progressive disclosure: `SKILL.md` stays lean, while detailed protocol guidance lives in `references/`.
- `eval_queries.json` can be used to test trigger quality before publishing.
- `SKILL.md` frontmatter intentionally keeps only `name` and `description` to stay closer to the `skill-creator` authoring guidance.
- `README.md` and `CHANGELOG.md` are repository-facing extras kept intentionally for GitHub publishing convenience; they are not required by the core Agent Skills package format.
