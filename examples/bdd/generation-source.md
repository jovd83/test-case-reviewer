# Example Generation Source

## User story

As a registered user  
I want to reset my password  
So that I can regain access to my account

## Acceptance criteria

1. The user can request a password reset from the sign-in page.
2. The system sends a reset link to the user's verified email address.
3. A valid reset link allows the user to set a new password.
4. An expired reset link is rejected with a clear message.
5. After a successful reset, the user can sign in with the new password.
6. The criteria do not define whether a second reset request invalidates the first link.

## Example generation request

```text
Generate a BDD feature file from this user story and acceptance criteria.
Include the main path and the expired-link rejection path.
List any unresolved assumptions separately instead of inventing behavior.
```
