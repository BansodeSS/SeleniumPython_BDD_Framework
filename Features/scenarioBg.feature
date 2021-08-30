Feature: OrangeHRM Login

  Background: common steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on login

  Scenario: Login to HRM Application
    Then User must login to the Dashboard page

  Scenario: Search user
    When navigate to search page
    Then search page should display

  Scenario: Advanced Search user
    When navigate to advance search page
    Then advance search page should display