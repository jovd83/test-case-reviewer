# Test Case Protocol Reference

## 1. Core Principle

1. Treat a test case as a specification of preconditions, inputs, actions, and expected results for one testing objective.

## 2. Oracle Rules

1. Use approved requirements, acceptance criteria, analysis documents, user manuals, or stakeholder-confirmed rules as the oracle.
2. Do not use implementation code as the primary oracle.
3. Flag green-but-wrong risk when tests appear derived from the implementation instead of business behavior.

## 3. Coverage Rules

1. Aim for full functional outcome coverage when no lower target is defined.
2. Do not stop after one true, one false, and one not-executed case if multiple paths can lead to those outcomes.
3. Add separate tests for each meaningful outcome category in calculations or classifications.

## 4. Test Design Technique Expectations

1. Use equivalence partitioning for input classes with similar expected behavior.
2. Use boundary value analysis for numeric, date, length, count, or threshold limits.
3. Use decision table testing for interacting business rules and conditions.
4. Use state transition testing for workflows with statuses, guards, and lifecycle changes.
5. Do not treat exploratory testing, checklist testing, or error guessing as the primary basis for formal designed test cases.

## 5. Title Rules

1. Require descriptive titles.
2. Include:
   1. requirement or suite context when available
   2. sequence identifier
   3. test type such as MSS, EXT, or ERR
   4. behavior-specific wording
3. Prefer titles such as:
   1. `UC04 TC01: MSS - affiliability OK when residence in Flanders`
4. Reject titles such as:
   1. `test 1`
   2. `OK`
   3. `error test`

## 6. Preconditions

1. Define the system state before the first action.
2. Include data setup, user role, service state, or inbound artifacts as needed.
3. Accept either style when logical:
   1. setup item as precondition
   2. setup item as first action
4. Prefer explicit numbering or lettering for easy mapping to implementation.

## 7. Actions

1. Write actions as clear executable steps.
2. Allow user-facing or system-facing wording depending on test type.
3. Prefer numbered steps when the execution order matters.

## 8. Expected Results

1. Write expected results as observable outcomes.
2. Allow assertion targets such as:
   1. UI message
   2. API payload
   3. database record
   4. file movement
   5. outgoing event
   6. log entry when behaviorally relevant
3. Reject expected results that are subjective or unverifiable.

## 9. Prioritization

1. Check whether the project uses test levels or priorities.
2. If a five-level scale exists, interpret it as:
   1. level 1 for MSS and most common paths
   2. level 2 for important extensions and uncovered paths
   3. level 3 for additional combinations and data variants
   4. level 4 for loop-focused or low-value variants
   5. level 5 for tests that can be ignored or deferred
3. Flag inconsistent prioritization when trivial cases outrank core business paths.
