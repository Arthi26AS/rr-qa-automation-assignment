Feature: Pagination functionality on Discover page


  @smoke
  Scenario: User navigates to next page of results
    Given user is on discover page
    When user selects "Top rated" category
    And user clicks on next page
    Then movie results for page "2" should be displayed
    And URL should contain "?page=2"
    And pagination should show current page as "2"

  @smoke
  Scenario: User navigates back to previous page
    Given user is on discover page
    When user selects "Top rated" category
    And user clicks on next page
    And user clicks on previous page
    Then movie results for page "1" should be displayed
    And URL should contain "?page=1"
    And pagination should show current page as "1"

  Scenario: Direct page number navigation
    Given user is on discover page
    When user selects "Top rated" category
    And user clicks on page number "3"
    Then movie results for page 3 should be displayed
    And URL should contain "?page=3"
    And pagination should show current page as "3"

  # Known issue as per assignment

  Scenario: User selects last page directly (known defect)
    Given user is on discover page
    When user selects "Top rated" category
    And user clicks on last page number
    Then movie results should be displayed for known defect

