---
name: tss-test-case-reviewer
description: Use when the user wants to review, audit, critique, score, or mentor drafted software test cases, manual scenarios, UAT cases, or test suites for requirement traceability, coverage gaps, technical correctness, standards compliance, weak expected results, or TSS or TDD-style test design quality before execution, automation, or sign-off.
metadata:
  dispatcher-output-artifacts: review_findings, scored_review, mentoring_feedback
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-input-artifacts: test_cases, requirements, standards, review_scope
  dispatcher-capabilities: test-case-review, test-case-scoring, test-design-mentoring
  dispatcher-stack-tags: testing, review, test-design
  dispatcher-accepted-intents: review_test_cases, score_test_cases, mentor_test_case_quality
  dispatcher-category: testing
---

# TSS Test Case Reviewer

## 1. Scope Selection

1. Classify the request as one of these modes:
   1. requirements and traceability review
   2. individual test case quality review
   3. suite architecture and redundancy review
   4. full review with scoring and mentoring
2. Stay in review mode unless the user explicitly asks for rewriting, redesign, or automation after the review.
3. If the user mixes review and authoring, deliver the review first and then propose corrections or rewrites.

## 2. Required Inputs

1. Collect the available artifacts before reviewing:
   1. requirements, user stories, acceptance criteria, use cases, or analysis notes
   2. drafted test cases
   3. optional suite hierarchy
   4. optional template, export, or naming convention
2. Identify the strongest non-code oracle:
   1. approved requirements
   2. acceptance criteria
   3. analysis documentation
   4. user manuals or stakeholder-approved business rules
3. Refuse to treat implementation code as the primary oracle unless the user explicitly asks for a code-vs-test consistency check.
4. If requirements are missing, continue with a limited review and state the limitation explicitly.

## 3. Load References Selectively

1. Read `references/review-workflow.md` for the full six-step review flow.
2. Read `references/test-case-protocol.md` when judging titles, preconditions, steps, expected results, or prioritization.
3. Read `references/test-suite-protocol.md` only when the task includes suites, folders, hierarchy, redundancy, or class-to-suite mapping.
4. Read `references/review-report-template.md` before writing the final review.
5. Read `references/examples-test-case-quality.md` when you need concrete examples that range from very bad to very good test-case quality.
6. Read `references/examples-review-comments.md` when you need examples of weak versus strong review feedback.
7. Read `references/examples-mini-review-reports.md` when you need examples of complete review outputs from weak to strong.
8. Read `references/examples-bad-input-artifacts.md` when you need examples of poor-quality requirements, traceability inputs, or suite structures that should trigger review findings.
9. Do not load all reference files by default if the task is narrow.

## 4. Review Workflow

1. Identify the review scope:
   1. requirements only
   2. test cases only
   3. test cases plus suite hierarchy
   4. full package with requirements, suites, and template
2. Build a quick inventory:
   1. count requirements
   2. count test cases
   3. count suites if present
   4. list missing artifacts
3. Review requirements and traceability:
   1. mark each requirement as clear, ambiguous, or missing detail
   2. map each requirement to one or more test cases
   3. flag uncovered requirements
4. Review suite architecture if present:
   1. check whether hierarchy moves from component or level to test type to oracle or requirement unit
   2. flag oversized low-level suites
   3. flag duplicate coverage caused by poor suite structure
5. Review coverage quality:
   1. verify every requirement has at least one test
   2. verify main success, extension, and error paths are represented when applicable
   3. verify the selected test design technique matches the behavior under test
6. Review technical correctness:
   1. verify preconditions establish the needed state
   2. verify actions are executable and deterministic
   3. verify expected results are specific and observable
   4. verify test data is realistic and covers boundaries or invalid input where needed
7. Review standards compliance:
   1. check naming quality
   2. check required fields
   3. check traceability links
   4. check classification such as MSS, EXT, or ERR
   5. check test level or priority if used
8. Write mentoring feedback:
   1. list strengths
   2. list recurring issues
   3. give 3 to 5 concrete recommendations ordered by impact
9. Produce the report using `references/review-report-template.md`.

## 5. Review Rules

1. Cite evidence for every major finding.
2. Name the affected requirement, suite, or test case whenever possible.
3. Separate critical gaps from minor improvements.
4. Prefer statements such as `REQ-04 has no negative-path coverage` over vague advice such as `add more tests`.
5. Recommend the missing test design technique when the current coverage is weak:
   1. equivalence partitioning for input classes
   2. boundary value analysis for limits or ranges
   3. decision tables for rule combinations
   4. state transitions for status-driven behavior
   5. use case paths for actor-flow behavior
6. State assumptions when the artifacts are incomplete.
7. Keep the review evidence-based and do not invent undocumented behavior.

## 6. Output Contract

1. Produce a structured review with these sections:
   1. executive summary
   2. requirements analysis and traceability
   3. suite architecture review if applicable
   4. coverage analysis
   5. technical correctness validation
   6. standards compliance review
   7. mentoring and development plan
   8. scoring matrix
   9. action plan
2. Put findings before praise when defects could cause wrong or incomplete testing.
3. Mark each finding with severity:
   1. Critical
   2. High
   3. Medium
   4. Low
4. Include a short limitation note if the review could not verify full traceability.
5. End with the next concrete actions the test author should take.

## 7. Example Triggers

1. Input:
```text
Review these API test cases and tell me whether they fully cover the acceptance criteria.
```
Output:
```text
Use this skill. Perform traceability, coverage, correctness, and compliance review. Report uncovered acceptance criteria and weak expected results.
```

2. Input:
```text
Mentor a junior tester's draft scenarios for UC-12 and score the quality.
```
Output:
```text
Use this skill. Review requirement mapping, path coverage, naming quality, and coaching opportunities. Produce a scored report.
```

3. Input:
```text
I have 35 test cases in one suite. Check if the suite structure is OK.
```
Output:
```text
Use this skill. Load the suite protocol reference, inspect hierarchy and size, and recommend a split if the low-level suite is overloaded.
```

4. Input:
```text
These UAT scenarios feel weak. Can you score them and tell me what would block sign-off?
```
Output:
```text
Use this skill. Review traceability, expected-result quality, path coverage, and readiness risks. Produce a scored report with blocking issues first.
```

## 8. Example Findings

1. Good finding:
```text
High: REQ-07 is only covered by one happy-path test. The requirement also defines invalid account states, but no ERR scenario covers suspended or closed accounts.
```

2. Weak finding:
```text
Need more negative tests.
```

3. Good correction advice:
```text
Add two ERR tests for REQ-07 using equivalence partitions for account status: one suspended account and one closed account. Assert the rejection message and unchanged account balance.
```

## 9. Gotchas
1. **The Code-Mirroring Trap**: Do not use implementation code as the primary oracle. Reviewing tests against what the code *already does* instead of what the *requirement demands* leads to "green-but-wrong" tests that pass while the business logic is incorrect.
2. **The "Happy Path" Bias**: Ensure the review doesn't stop at the Main Success Scenario (MSS). Explicitly check for Error (ERR) and Extension (EXT) paths, state transitions, and boundary conditions that are often overlooked in initial drafts.
3. **Vague Expected Results**: Reject results like "Success," "OK," or "User is redirected." Demand observable, verifiable outcomes such as specific UI elements, API status codes, database record changes, or outgoing events.
4. **Data Hardcoding**: Flag tests that rely on specific, ephemeral data IDs (e.g., `userId=123`) instead of describing the *type* or *state* of data required (e.g., "an active user with no pending orders").
5. **Reviewing in a Vacuum**: If requirements are missing or ambiguous, do not guess the intended behavior. Explicitly state the limitation in the review and ask for the authoritative source before finalizing coverage scores.
6. **Implicit Assumptions**: Watch for "invisible" preconditions. If a test requires a specific configuration or background state that isn't listed, it will be non-deterministic or fail in execution.

## 10. Troubleshooting

1. Error: `Requirements are missing or too vague.`
   Fix:
   1. continue with structure and correctness review only
   2. mark traceability and coverage conclusions as limited
   3. list the missing requirement details needed for a full review
2. Error: `The test suite hierarchy is unclear.`
   Fix:
   1. infer the current grouping
   2. compare it to the suite protocol
   3. recommend a cleaner component -> test type -> oracle structure
3. Error: `Expected results are too generic to verify.`
   Fix:
   1. rewrite the finding in observable terms
   2. name the missing assertion target such as UI message, API response, database record, event, or file
4. Error: `The tests mirror the code instead of the requirements.`
   Fix:
   1. flag code-based oracle risk explicitly
   2. anchor the review to approved business behavior
   3. ask for the authoritative requirement source if none is available
5. Error: `The user wants rewritten test cases, not only a review.`
   Fix:
   1. finish the review first
   2. rewrite or propose corrected cases only after naming the defects and rationale

## 11. Final Check

1. Confirm that every major claim is backed by an artifact.
2. Confirm that missing coverage is tied to a named requirement, path, rule, or state.
3. Confirm that recommendations are specific enough to act on without guessing.
4. Confirm that the review distinguishes must-fix items from coaching advice.