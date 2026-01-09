Feature: Filter functionality on Discover page
  
  Scenario: Verify Top Rated category filter works
    Given user is on discover page
    When user selects "Top rated" category
    Then movie results should be displayed
  
  Scenario: Verify TV Shows type filter works
    Given user is on discover page
    When user selects "TV Shows" type
    Then movie results should be displayed

  # Known issue as per assignment
  Scenario: Access category via direct URL (known defect)
    Given user accesses discover page with "popular" slug
    Then movie results should be displayed

  # Bug: Application should allow same year for start and end range

  Scenario: Verify year range allows same start and end year selection
    Given user is on discover page
    When user selects "TV Shows" type
    And user sets year range from "1900" to "1900"
    Then movie results should be displayed
