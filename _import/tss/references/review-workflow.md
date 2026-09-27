# Review Workflow Reference

## Purpose

Use this reference when the task needs the full structured review method instead of a lightweight critique.

## Step 1. Requirements Analysis and Traceability

1. Gather every available oracle document.
2. Extract identifiable requirement units such as requirement IDs, use cases, acceptance criteria, or business rules.
3. Mark each requirement as:
   1. clear and testable
   2. ambiguous
   3. incomplete
4. Record missing details that block precise testing.
5. Build a requirement-to-test map.
6. Flag any requirement with no linked test case.

## Step 2. Test Suite Architecture Review

1. Use this step only when suite or folder structure exists.
2. Inspect whether the hierarchy helps people find tests quickly.
3. Prefer high-level grouping by component or deployable area.
4. Prefer intermediate grouping by test level or test type.
5. Prefer lower-level grouping by oracle source or requirement unit such as use case.
6. Flag low-level suites with more than about 20 test cases as split candidates.
7. Flag structures that encourage duplicate tests across multiple suites.
8. Check whether the structure supports readable mapping to implementation classes.

## Step 3. Coverage Analysis

1. Confirm that every requirement is covered by at least one test.
2. Confirm that functional paths are covered:
   1. MSS
   2. EXT
   3. ERR
3. Confirm that all meaningful business-rule outcomes are covered.
4. Confirm that each calculation category is tested individually when categories exist.
5. Evaluate whether the correct design technique is used:
   1. equivalence partitioning for representative input classes
   2. boundary value analysis for edges and limits
   3. decision tables for business-rule combinations
   4. state transition testing for status changes
   5. use case testing for actor-driven flows
6. Flag uncovered scenarios and redundant scenarios separately.

## Step 4. Technical Correctness Validation

1. Validate the test oracle.
2. Prefer approved requirements, acceptance criteria, analysis documents, manuals, or stakeholder-confirmed behavior.
3. Flag code-based oracle usage as a review risk.
4. Check preconditions:
   1. needed systems available
   2. needed data present
   3. needed user role or system state established
5. Check actions:
   1. executable
   2. deterministic
   3. free of hidden assumptions
6. Check expected results:
   1. specific
   2. measurable
   3. verifiable
   4. tied to observable outcomes
7. Check test data:
   1. realistic
   2. representative
   3. boundary-aware
   4. negative-path capable

## Step 5. Standards Compliance

1. Check title quality.
2. Check required fields.
3. Check traceability notation.
4. Check test classification such as MSS, EXT, or ERR.
5. Check numbering or lettering of preconditions and steps if the local template expects it.
6. Check prioritization or test level if used by the project.
7. Flag generic titles such as `test 1`, `OK`, or `error case`.

## Step 6. Mentoring and Assessment

1. Summarize strengths without hiding serious gaps.
2. Group recurring issues into skill-development themes.
3. Recommend 3 to 5 concrete improvements.
4. Order recommendations by business impact.
5. Produce a scoring matrix only when the user asks for scoring or when the workflow requires it.
6. End with the next actions that make the test set review-ready.
