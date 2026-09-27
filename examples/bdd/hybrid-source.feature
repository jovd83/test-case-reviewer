Feature: Password reset

  Scenario: Reset password works
    Given a registered user is on the reset page
    When the user enters a new password and clicks submit
    Then the password works
