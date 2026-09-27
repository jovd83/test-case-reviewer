# Review Comment Examples

Use this reference when you need examples of reviewer feedback quality. The examples below use a consistent quality ladder from very weak to excellent.

## Contents

1. Very Weak Comment: Generic Complaint
2. Very Weak Comment: Vague Coverage Advice
3. Weak Comment: Unclear Expected Result Feedback
4. Weak Comment: No Oracle Reference
5. Weak Comment: Missing Reproducibility Guidance
6. Moderate Comment: Useful but Not Fully Actionable
7. Good Comment: Specific Naming Fix
8. Good Comment: Strong Negative Coverage Feedback
9. Very Good Comment: Technique-Based Guidance
10. Excellent Comment: Review-Ready Coaching Feedback

## 1. Very Weak Comment: Generic Complaint

### Weak Review Comment

`This test is not good.`

### Why It Is Weak

- no evidence
- no named defect
- no improvement direction

### Stronger Version

`High: The test case title "test login" does not identify the requirement, path type, or behavior under test, which makes the case hard to trace and easy to duplicate. Rename it to include the use case, sequence number, and scenario intent.`

## 2. Very Weak Comment: Vague Coverage Advice

### Weak Review Comment

`Add more tests.`

### Why It Is Weak

- does not name the missing requirement or path
- does not explain what kind of tests are missing

### Stronger Version

`High: REQ-07 has only one MSS scenario. Add ERR coverage for suspended and closed account states because the requirement defines both as rejection conditions.`

## 3. Weak Comment: Unclear Expected Result Feedback

### Weak Review Comment

`Expected result is unclear.`

### Why It Is Weak

- does not identify what is unclear
- gives no observable replacement

### Stronger Version

`Medium: The expected result "transfer succeeds" is too vague to verify. State the observable outcomes: transfer status, updated source balance, updated target balance, and confirmation message.`

## 4. Weak Comment: No Oracle Reference

### Weak Review Comment

`I think this value should be different.`

### Why It Is Weak

- opinion-based
- no oracle reference
- easy to dispute

### Stronger Version

`High: The expected discount value appears derived from current implementation behavior instead of REQ-18. Re-anchor the expected result to the approved pricing rule and explain how the amount is calculated.`

## 5. Weak Comment: Missing Reproducibility Guidance

### Weak Review Comment

`Preconditions need work.`

### Why It Is Weak

- does not say which condition is missing
- does not explain the execution risk

### Stronger Version

`Medium: The preconditions do not define why password reset should fail. Add the exact token state, such as expired token or already-used token, so the ERR path is reproducible.`

## 6. Moderate Comment: Useful but Not Fully Actionable

### Moderate Review Comment

`Consider adding boundary tests around the shipping threshold.`

### Why It Is Only Moderate

- points in the right direction
- still does not specify which boundaries to add

### Stronger Version

`Medium: This scenario covers 49.99 EUR but leaves the threshold under-tested. Add adjacent cases at 50.00 EUR and 50.01 EUR to verify the boundary behavior defined in REQ-44.`

## 7. Good Comment: Specific Naming Fix

### Good Review Comment

`Low: The title "error test" is too generic for traceability. Rename it to include the requirement context, test type, and behavior, for example: "UC09 TC02: ERR - password reset rejected when reset token has expired".`

### Why It Is Good

- names the defect
- explains impact
- gives a concrete replacement pattern

## 8. Good Comment: Strong Negative Coverage Feedback

### Good Review Comment

`High: The suite covers only the main transfer path. The requirement also defines insufficient funds, blocked account, and invalid amount failures, but no ERR cases cover those outcomes. Add one case per failure path instead of one generic negative case.`

### Why It Is Good

- ties feedback to requirement behavior
- names specific missing scenarios
- avoids vague "more negative tests" language

## 9. Very Good Comment: Technique-Based Guidance

### Very Good Review Comment

`Medium: The current set checks one valid and one invalid value, but the requirement defines a numeric threshold. Apply boundary value analysis and add cases at limit - 1, exact limit, and limit + 1 rather than selecting arbitrary values.`

### Why It Is Very Good

- identifies the right test design technique
- explains why the current selection is weak
- provides the missing test pattern

## 10. Excellent Comment: Review-Ready Coaching Feedback

### Excellent Review Comment

`High: UC21 TC11 is strong on traceability and expected-result observability, but the suite still lacks the paired timing boundary around the 3-D Secure timeout. Add one MSS case where confirmation happens just before 5 minutes and keep this ERR case for expiry after 5 minutes. That pair will demonstrate both sides of AC-21.4 and reduce sign-off risk.`

### Why It Is Excellent

- acknowledges strengths without hiding risk
- names the exact remaining gap
- recommends the right adjacent scenario
- ties the advice to sign-off confidence
