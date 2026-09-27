---
name: test-case-reviewer
description: Review, score and mentor drafted tests before execution, automation or sign-off - manual, UAT and regression test cases, test suites and traceability matrices, and BDD/Gherkin feature files, scenarios and outlines - against requirements, acceptance criteria and business rules. Finds traceability and coverage gaps, missing negative, boundary and error paths, weak or unobservable expected results, suite redundancy, UI-scripted or overloaded Gherkin, and invented metadata. Rewrites the reviewed artifact on request, and drafts Gherkin from rules, acceptance criteria or example maps. Not for designing classic test cases from scratch (test-design-orchestrator), automation code, or step definitions.
metadata:
  author: jovd83
  version: 2.0.0
  dispatcher-category: testing
  dispatcher-layer: feedback
  dispatcher-lifecycle: active
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-capabilities: test-case-review, test-suite-review, test-case-scoring, test-design-mentoring, bdd-review, bdd-rewrite, bdd-generation
  dispatcher-accepted-intents: review_test_cases, score_test_cases, mentor_test_case_quality, review_bdd_test_cases, rewrite_bdd_test_cases, generate_bdd_test_cases
  dispatcher-input-artifacts: test_cases, test_suite, traceability_matrix, bdd_feature, requirements, acceptance_criteria, business_rules, example_map
  dispatcher-output-artifacts: review_findings, scored_review, mentoring_feedback, rewritten_artifact, bdd_feature
  dispatcher-stack-tags: testing, test-design, review, bdd, gherkin
---

# Test Case Reviewer

> **Author:** jovd83 | **Version:** 2.0.0 | **License:** MIT

Review drafted tests the way a senior test designer would: against the source of truth, findings first, with evidence, and with advice concrete enough to act on. One skill covers two kinds of artifact that share the same review discipline: classic test cases and BDD/Gherkin.

## 1. Classify the artifact and the mode

**Artifact track**

| Track | Artifacts | References |
|---|---|---|
| Test cases | Manual, UAT or regression test cases with preconditions, steps and expected results; test suites and hierarchies; requirement-to-test traceability matrices | `references/test-cases/` |
| BDD | Gherkin feature files, scenarios, Scenario Outlines, `Rule:` blocks, example maps | `references/bdd/` |

A package with both gets each part reviewed on its own track, then one combined report.

**Mode**

- `review` (default, both tracks): assess, rank findings, score when asked.
- `rewrite` (both tracks): improve the artifact while preserving its intent. On the test-case track, finish the review first and only then propose corrected cases, each tied to a named defect.
- `generate` (BDD track only): draft Gherkin from business rules, acceptance criteria, user stories or example maps. Designing classic test cases from scratch belongs to `test-design-orchestrator`.
- `hybrid` (both tracks): short findings, then the corrected artifact.

State the track and mode at the start of the response when they are not obvious. Stay in review mode unless the user asks for more.

## 2. Establish the oracle

Judge correctness only against a source of truth, strongest first:

1. approved business rules and requirements
2. acceptance criteria
3. user stories, use cases, analysis documentation
4. stakeholder-approved notes, user manuals
5. the artifact's own text (weakest: it can only show internal consistency)

Always:

- name the oracle sources you used, and rate them strong, partial or weak;
- separate confirmed behavior from assumptions;
- when requirements are missing, continue with a structure-and-quality review, mark traceability and coverage conclusions as limited, and list what is needed for a full review.

Never:

- use implementation code as the primary oracle, unless the user explicitly asks for a code-versus-test consistency check (tests that mirror the code pass while the business rule is wrong);
- invent requirement IDs, personas, tags, priorities, business rules, policy limits or framework semantics. Report missing metadata as a gap.

## 3. Rate findings on one scale

| Severity | Meaning |
|---|---|
| `Critical` | The tested behavior is wrong, contradictory, missing, or too ambiguous to trust; a requirement has no coverage at all |
| `High` | Likely to mislead execution, automation, review or sign-off: a missing negative or error path, an unobservable expected result, a scenario that mixes rule branches |
| `Medium` | A real quality defect with limited reach: one weak expected result, a generic title that hides the condition, a readable but overloaded scenario |
| `Low` | Wording, readability, naming, metadata or low-risk cleanup |

Cite evidence for every Critical and High finding and name the affected requirement, suite, test case or scenario. Prefer `REQ-04 has no negative-path coverage` over `add more tests`. When the artifact is strong, say `No material defects identified` rather than inventing findings.

## 4. Test-case track

Read `references/test-cases/review-workflow.md` for the full flow. Load the others only when the task needs them:

- `test-case-protocol.md` when judging titles, preconditions, steps, expected results or priorities;
- `test-suite-protocol.md` when suites, folders, hierarchy or redundancy are in scope;
- `report-template.md` before writing the final review;
- `examples-test-case-quality.md`, `examples-review-comments.md`, `examples-mini-review-reports.md`, `examples-bad-input-artifacts.md` when calibrating what weak and strong look like.

Workflow:

1. **Scope and inventory.** Requirements only, test cases only, cases plus suites, or the full package. Count requirements, test cases and suites; list missing artifacts.
2. **Requirements and traceability.** Mark each requirement clear, ambiguous or missing detail. Map each to its test cases and flag the uncovered ones.
3. **Suite architecture** (when present). Hierarchy should run component or level → test type → oracle or requirement unit. Flag low-level suites above about 20 cases and structures that invite duplicate tests.
4. **Coverage.** Every requirement has at least one test. Main success (MSS), extension (EXT) and error (ERR) paths are represented where they apply. When coverage is weak, name the missing technique: equivalence partitioning for input classes, boundary value analysis for limits, decision tables for rule combinations, state transitions for status-driven behavior, use case paths for actor flows.
5. **Technical correctness.** Preconditions establish the needed state, including the invisible ones. Steps are executable and deterministic. Expected results are specific and observable: a UI message, API status and body, database record, event or file, never `Success` or `OK`. Test data describes the state it needs ("an active user with no pending orders") instead of hard-coding ephemeral IDs, and covers boundaries and invalid input.
6. **Standards compliance.** Naming, required fields, traceability links, MSS/EXT/ERR classification, test level or priority when used.
7. **Mentoring.** Strengths, recurring issues, and 3 to 5 recommendations ordered by impact.

Output the review with these sections: executive summary, requirements analysis and traceability, suite architecture (if applicable), coverage analysis, technical correctness, standards compliance, mentoring and development plan, scoring matrix, action plan. Put findings before praise when defects could cause wrong or incomplete testing, add a limitation note when traceability could not be verified, and end with the next concrete actions for the test author.

A good finding and its fix:

```text
High: REQ-07 is only covered by one happy-path test. The requirement also defines invalid account
states, but no ERR scenario covers suspended or closed accounts.
Fix: add two ERR tests using equivalence partitions for account status (one suspended, one closed).
Assert the rejection message and the unchanged account balance.
```

## 5. BDD track

Treat BDD as a business-readable behavioral specification, not a UI script. Load references as needed:

- `references/bdd/intake-and-decision-flow.md` when the request, oracle or mode is unclear;
- `references/bdd/review-workflow.md` for formal or findings-first reviews;
- `references/bdd/quality-rules.md` for anti-patterns and rewrite heuristics;
- `references/bdd/feature-and-scenario-protocol.md` for `Feature:`, `Rule:`, `Background:`, `Scenario Outline`, tags and naming;
- `references/bdd/report-rubric.md` and `assets/bdd-review-report-template.md` for scores and formal reports;
- `references/bdd/output-contracts.md` when a stricter response shape is needed.

Guardrails. Always prefer business behavior over UI choreography, keep one behavior path per scenario and one main event in `When`, make `Then` externally observable, keep `Given` minimal but sufficient, use concrete domain examples the source supports, and keep traceability explicit. Never narrate test scripts in Gherkin, mix rule branches in one scenario, or add implementation detail the behavior does not need.

- **review:** assess intent and scope, traceability, scenario architecture (naming, grouping, duplication), path coverage (main, alternate, error, plus persona, permission, boundary or lifecycle where relevant), and BDD quality (business language, observable outcomes, concrete examples, no UI scripting, no mixed branches). Findings first.
- **rewrite:** preserve intent; retitle scenarios as condition plus outcome; split overloaded scenarios; replace UI steps with business behavior unless the UI interaction is the rule; replace vague outcomes with observable ones; keep unsupported metadata as an explicit gap. Use `assets/bdd-feature-template.feature` for full feature files.
- **generate:** start from rules, decisions and examples; map the rule space into main, alternate and error behavior; one scenario per behavior path or rule branch; concrete roles, dates, states and amounts. Generate only the supported behaviors and list the unresolved gaps; stop when the source is too thin.
- **hybrid:** the most material findings, then the improved artifact, then open assumptions.

Default response shapes: review gives mode, oracle, confidence, ranked findings, coverage and traceability notes, top recommendations; rewrite gives strategy, revised artifact, open assumptions; generate gives source inputs, generated artifact, assumptions and gaps. Examples of each live in `examples/bdd/`.

## 6. Handle weak input

- **Weak oracle:** review structure and quality, lower confidence, avoid correctness claims, ask for the authoritative source.
- **Unclear suite hierarchy:** infer the current grouping, compare it with the suite protocol, recommend the cleaner structure.
- **Generic expected results:** restate the finding in observable terms and name the missing assertion target.
- **Too much scope in one feature or suite:** recommend splitting by capability, rule set, persona or lifecycle phase.
- **The user wants rewrites, not only a review:** finish the review, then rewrite, each change traced to a finding.

## 7. Gotchas

- **Happy-path bias:** do not stop at the main success path; check extension, error, state-transition and boundary coverage.
- **Automation handoff:** no Cucumber, Playwright or Cypress code unless explicitly requested; that belongs to the framework skills.
- **Over-correction:** a well-built artifact gets `No material defects identified`, not invented findings.
- **Well-written is not correct:** always check behavior against the oracle, not just the structure.
- **Scope creep:** review what was asked; do not generate a whole feature when the user asked about two scenarios.

## 8. Files and memory

Keep working notes in the conversation. Write files only when the user asks for a saved report, scorecard or rewritten artifact, and put them where the user says.

## 9. Final check

1. Every major claim is backed by an artifact.
2. Every coverage gap is tied to a named requirement, path, rule or state.
3. Recommendations are specific enough to act on without guessing.
4. Must-fix items are separated from coaching advice.
