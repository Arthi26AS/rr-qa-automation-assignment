# Test Case Document – TMDB Discover Demo Site

## Scope
This document covers functional test cases for filtering options, pagination, and basic negative scenarios on the TMDB Discover demo website.

Application URL: https://tmdb-discover.surge.sh

---

## Filtering Options

### TC-001: Verify Popular category filter
Objective:  
Ensure that selecting the Popular category updates the listing accordingly.

Steps:
1. Open the application.
2. Click on the Popular category.

Expected Result:  
The page refreshes and displays titles belonging to the Popular category.

Priority: High

---

### TC-002: Verify Trending category filter
Objective:  
Confirm that the Trending category shows trending movies or TV shows.

Steps:
1. Open the application.
2. Select Trending from the category options.

Expected Result:  
Only trending titles are displayed in the results.

Priority: High

---

### TC-003: Verify Newest category filter
Objective:  
Validate that the Newest category sorts content by recent release date.

Steps:
1. Open the application.
2. Select Newest category.

Expected Result:  
Titles are displayed based on the most recent release dates.

Priority: Medium

---

### TC-004: Verify Top Rated category filter
Objective:  
Ensure that selecting Top Rated displays highly rated content.

Steps:
1. Open the application.
2. Select Top Rated category.

Expected Result:  
Titles are sorted and displayed in descending order of ratings.

Priority: High

---

### TC-005: Verify title search functionality
Objective:  
Validate that users can search for content using a title name.

Steps:
1. Enter a valid title (for example, Inception) in the search field.
2. Click on Search.

Expected Result:  
Matching titles related to the search term are displayed.

Priority: High

---

### TC-006: Verify filtering by content type - Movies
Objective:  
Ensure that selecting Movies filters out TV shows from the results.

Steps:
1. Select Movies from the type filter.

Expected Result:  
Only movie entries are shown in the listing.

Priority: High

---

### TC-007: Verify filtering by content type - TV Shows
Objective:  
Ensure that selecting TV Shows filters out movies from the results.

Steps:
1. Select TV Shows from the type filter.

Expected Result:  
Only TV show entries are displayed.

Priority: High

---

### TC-008: Verify filtering by year of release
Objective:  
Validate that content can be filtered by a specific release year.

Steps:
1. Enter 2020 in the year filter.
2. Apply the filter.

Expected Result:  
Only titles released in the year 2020 are displayed.

Priority: Medium

---

### TC-009: Verify filtering by rating
Objective:  
Ensure that rating-based filtering works correctly.

Steps:
1. Apply a rating filter of 5 stars or above.

Expected Result:  
Only titles with a rating greater than or equal to 5 are shown.

Priority: Medium

---

### TC-010: Verify filtering by genre
Objective:  
Validate genre-based filtering functionality.

Steps:
1. Select Action from the genre filter.

Expected Result:  
Only action genre titles are displayed in the results.

Priority: Medium

---

### TC-018: Verify year range allows same start and end year selection
Objective:
Validate that the application properly handles when the start and end year range are set to the same year.

Steps:
1. Open the application.
2. Select "TV Shows" from the type filter.
3. Set the year range from "1900" to "1900" (same start and end year).

Expected Result:
The page should display TV shows released in the year 1900 or handle the same year selection gracefully without breaking the UI.

Priority: Medium

**Note:** This is currently a bug - the application does not properly handle same start and end year selection.

---

## Pagination

### TC-011: Verify navigation to the next page
Objective:  
Ensure users can navigate forward using pagination.

Steps:
1. Click on the Next Page button.

Expected Result:  
The next set of titles is displayed successfully.

Priority: High

---

### TC-012: Verify navigation to the previous page
Objective:  
Ensure users can navigate backward using pagination controls.

Steps:
1. Click on the Previous Page button.

Expected Result:  
The previous page’s titles are displayed.

Priority: High

---

### TC-013: Verify pagination behavior on the last page
Objective:  
Observe system behavior when navigating to the final pagination page.

Steps:
1. Navigate through pagination until the last page is reached.

Expected Result:  
The last page should load correctly or fail gracefully without breaking the application.

Priority: Medium

---

### TC-014: Verify pagination reset after applying filters
Objective:  
Ensure pagination resets when a new filter is applied.

Steps:
1. Navigate to any page beyond page 1.
2. Apply any filter such as category or type.

Expected Result:  
Results refresh and pagination resets to page 1.

Priority: Medium

---

## Negative Test Scenarios

### TC-015: Verify behavior when accessing category via direct URL slug
Objective:  
Validate application behavior when accessing a category directly via URL.

Steps:
1. Navigate to https://tmdb-discover.surge.sh/popular.

Expected Result:  
The page should load the Popular category or handle the error gracefully.

Priority: Medium

---

### TC-016: Verify search behavior with empty input
Objective:  
Check how the application handles an empty search request.

Steps:
1. Leave the search field empty.
2. Click Search.

Expected Result:  
Either all results are displayed or a user-friendly validation message appears.

Priority: Low

---

### TC-017: Verify behavior for invalid genre selection
Objective:  
Observe how the system behaves when an invalid or unsupported genre is selected.

Steps:
1. Attempt to select a non-existent genre.

Expected Result:  
No results are displayed or an appropriate error message is shown without breaking the UI.

Priority: Low
