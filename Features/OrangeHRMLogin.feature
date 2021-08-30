Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valide parameters
    Given I launch chrome browser
    When I open ornage hrm homepage
    And Enter username "admin" and password "admin123"
    And Click on the login Button
    Then User must succesfully login to the Dashboard page

  Scenario Outline: Login to OrangeHRM with valide parameters
    Given I launch chrome browser
    When I open ornage hrm homepage
    And Enter username "<username>" and password "<password>"
    And Click on the login Button
    Then User must succesfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | admin    | xyz      |
      | admin    | xyz      |