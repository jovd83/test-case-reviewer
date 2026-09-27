@requirement-AUTH-101
Feature: Account sign-in
  As a registered user
  I want to sign in to my account
  So that I can access my dashboard

  Scenario: Login works
    Given I open the login page
    When I type valid credentials
    And I click submit
    Then I am logged in

  Scenario: Locked account is blocked after repeated invalid attempts
    Given a registered user entered an invalid password three times
    When the user submits the credentials again
    Then the user sees a message that the account is locked
