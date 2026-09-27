# Bad Input Artifact Examples

Use this reference when the skill needs examples of low-quality inputs before the review even begins. These examples help the agent recognize ambiguity, weak traceability, overloaded suites, and incomplete test assets before applying the quality ladder used in the other example files.

## Contents

1. Bad Requirement: Ambiguous Business Rule
2. Bad Requirement: Missing Negative Behavior
3. Bad Requirement Set: Contradictory Rules
4. Bad Traceability Matrix: Unusable Mapping
5. Bad Traceability Matrix: Overstated Completeness
6. Bad Draft Test Case: Missing Oracle
7. Bad Draft Test Case Set: Only Happy Paths
8. Bad Suite Structure: Overloaded Low-Level Suite
9. Bad Suite Structure: Flat and Opaque
10. Bad Review Input Package: Incomplete for Sign-Off

## 1. Bad Requirement: Ambiguous Business Rule

### Artifact

```text
REQ-11: Important customers should receive a better discount when possible.
```

### Why It Is Bad

- `important` is undefined
- `better discount` is undefined
- `when possible` is undefined
- not directly testable

### Review Implication

- mark the requirement as ambiguous
- avoid inventing expected values
- request clarification on customer classification, discount amount, and decision conditions

## 2. Bad Requirement: Missing Negative Behavior

### Artifact

```text
AC-07: The user can upload a PDF document.
```

### Why It Is Bad

- no file-size rule
- no invalid-type behavior
- no duplicate upload behavior
- no failure message expectation

### Review Implication

- traceability review must note that negative-path expectations are missing from the source oracle
- coverage conclusions should be marked as limited

## 3. Bad Requirement Set: Contradictory Rules

### Artifact

```text
REQ-21: Orders over 50 EUR qualify for premium shipping.
AC-21.2: Premium shipping is available only for baskets above 50 EUR.
```

### Why It Is Bad

- `over 50 EUR` may include 50.00 depending on interpretation
- `above 50 EUR` usually excludes 50.00
- boundary rule is contradictory

### Review Implication

- flag the boundary ambiguity before reviewing test coverage
- prevent false negatives against test cases at exactly 50.00 EUR

## 4. Bad Traceability Matrix: Unusable Mapping

### Artifact

```text
REQ-01 -> tested
REQ-02 -> tested
REQ-03 -> partial
```

### Why It Is Bad

- no test case IDs
- no suite references
- no coverage rationale
- cannot support an audit trail

### Review Implication

- mark traceability as insufficient
- require named test links such as `REQ-03 -> TC04, TC05`

## 5. Bad Traceability Matrix: Overstated Completeness

### Artifact

```text
AC-10 -> TC09
```

### Why It Is Bad

- implies full coverage from a single link
- no indication of MSS, EXT, or ERR path support
- no note on missing alternate outcomes

### Review Implication

- inspect whether the linked case covers only the happy path
- avoid accepting one-link-equals-complete assumptions

## 6. Bad Draft Test Case: Missing Oracle

### Artifact

```text
Title: TC05 calculate tax
Preconditions:
- service deployed
Steps:
- send request
Expected result:
- tax is correct
```

### Why It Is Bad

- no requirement ID
- no input values
- no calculation rule
- no measurable output target

### Review Implication

- classify as technically weak and non-traceable
- request the source rule and explicit numeric assertions

## 7. Bad Draft Test Case Set: Only Happy Paths

### Artifact

```text
UC08 TC01: MSS - login succeeds with valid credentials
UC08 TC02: MSS - login succeeds with remembered device
UC08 TC03: MSS - login succeeds after password change
```

### Why It Is Bad

- no invalid credentials case
- no locked-account case
- no MFA failure case
- looks broad but still misses risk-heavy paths

### Review Implication

- coverage review should flag missing ERR and EXT scenarios explicitly

## 8. Bad Suite Structure: Overloaded Low-Level Suite

### Artifact

```text
Password Reset
- 34 test cases covering token expiry, reused token, unknown user, locked user, rate limits, email template checks, localization, and audit logging
```

### Why It Is Bad

- too many behaviors in one low-level suite
- hard to search and maintain
- encourages duplicate tests
- weak mapping to implementation or automation classes

### Review Implication

- recommend splitting by meaningful behavior group
- mark maintainability and redundancy risk

## 9. Bad Suite Structure: Flat and Opaque

### Artifact

```text
Tests
- TC01
- TC02
- TC03
- TC04
```

### Why It Is Bad

- no component grouping
- no test type grouping
- no oracle or requirement grouping
- impossible to understand from hierarchy alone

### Review Implication

- require at least component or test-type structure before claiming suite quality

## 10. Bad Review Input Package: Incomplete for Sign-Off

### Artifact

```text
Available:
- 7 drafted manual test cases

Missing:
- requirements
- acceptance criteria
- suite structure
- priority or test level
```

### Why It Is Bad

- no reliable oracle
- no way to confirm completeness
- no sign-off basis

### Review Implication

- continue with a limited structural and technical review only
- explicitly state that coverage and traceability conclusions are provisional
