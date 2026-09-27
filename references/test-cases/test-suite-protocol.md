# Test Suite Protocol Reference

## 1. Purpose of a Test Suite

1. Treat the suite as a logical container that improves findability and reduces redundancy.
2. Prefer a structure that makes the purpose of a test obvious from its place in the hierarchy.

## 2. High-Level Structure

1. Group the highest level by component, subsystem, or deployable area when possible.
2. Typical examples:
   1. web application
   2. API services
   3. batches
   4. routing platform

## 3. Intermediate Structure

1. Group intermediate levels by test level or test type when useful.
2. Typical examples:
   1. integration tests
   2. contract tests
   3. service tests
   4. system tests
   5. E2E tests
   6. UI tests

## 4. Lower-Level Structure

1. Group the lower levels by oracle source or requirement unit.
2. Typical examples:
   1. use cases
   2. data flows
   3. acceptance-criteria groups
   4. cookbooks
3. Reuse the same requirement unit name across multiple branches only when the test type differs.

## 5. Splitting Rules

1. Split a low-level suite when it becomes hard to search, review, or maintain.
2. Use about 20 test cases as a practical threshold for a split discussion.
3. Split by meaningful behavior, input type, or flow variant instead of arbitrary numbering.

## 6. Redundancy Rules

1. Avoid placing one logical path in multiple suites just to satisfy traceability optics.
2. Use the hierarchy itself to support requirement mapping where possible.
3. Flag duplicate scenarios when the same path is executed more than once in a normal run without a justified test-type difference.

## 7. Review Questions

1. Can a reviewer find a test quickly from the hierarchy and title?
2. Does the structure expose covered requirements without opening every case?
3. Does each low-level suite map cleanly to an implementation class or automation unit?
4. Are suites too broad, too flat, or too duplicated?
