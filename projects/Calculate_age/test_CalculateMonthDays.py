# ********RoostGPT********
"""
Test generated by RoostGPT for test python-code-testing using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=month_days_1396fdc0ba
ROOST_METHOD_SIG_HASH=month_days_5dd3c5e333


Scenario 1: Test for months with 31 days
Details:
  TestName: test_month_days_for_31_days
  Description: This test is intended to verify that the function returns 31 days for the months January, March, May, July, August, October, and December.
Execution:
  Arrange: No setup required.
  Act: Invoke the month_days function with month as one of the months with 31 days (1, 3, 5, 7, 8, 10, 12) and leap_year as False.
  Assert: The function should return 31.
Validation:
  The test ensures that the function correctly returns the number of days for months with 31 days irrespective of whether the year is a leap year or not.

Scenario 2: Test for months with 30 days
Details:
  TestName: test_month_days_for_30_days
  Description: This test is intended to verify that the function returns 30 days for the months April, June, September, and November.
Execution:
  Arrange: No setup required.
  Act: Invoke the month_days function with month as one of the months with 30 days (4, 6, 9, 11) and leap_year as False.
  Assert: The function should return 30.
Validation:
  The test ensures that the function correctly returns the number of days for months with 30 days irrespective of whether the year is a leap year or not.

Scenario 3: Test for February in a non-leap year
Details:
  TestName: test_month_days_for_february_non_leap_year
  Description: This test is intended to verify that the function returns 28 days for February if the year is not a leap year.
Execution:
  Arrange: No setup required.
  Act: Invoke the month_days function with month as 2 and leap_year as False.
  Assert: The function should return 28.
Validation:
  The test ensures that the function correctly returns the number of days for February in a non-leap year.

Scenario 4: Test for February in a leap year
Details:
  TestName: test_month_days_for_february_leap_year
  Description: This test is intended to verify that the function returns 29 days for February if the year is a leap year.
Execution:
  Arrange: No setup required.
  Act: Invoke the month_days function with month as 2 and leap_year as True.
  Assert: The function should return 29.
Validation:
  The test ensures that the function correctly returns the number of days for February in a leap year.

Scenario 5: Test for invalid month
Details:
  TestName: test_month_days_for_invalid_month
  Description: This test is intended to verify that the function returns None for an invalid month.
Execution:
  Arrange: No setup required.
  Act: Invoke the month_days function with month as an invalid number (e.g., 13) and leap_year as False.
  Assert: The function should return None.
Validation:
  The test ensures that the function correctly handles the case when an invalid month is passed.
"""

# ********RoostGPT********
import pytest
from Calculate_age.calculate import month_days

class Test_CalculateMonthDays:
    @pytest.mark.parametrize("month", [1, 3, 5, 7, 8, 10, 12])
    def test_month_days_for_31_days(self, month):
        assert month_days(month, False) == 31

    @pytest.mark.parametrize("month", [4, 6, 9, 11])
    def test_month_days_for_30_days(self, month):
        assert month_days(month, False) == 30

    def test_month_days_for_february_non_leap_year(self):
        assert month_days(2, False) == 28

    def test_month_days_for_february_leap_year(self):
        assert month_days(2, True) == 29

    @pytest.mark.parametrize("month", [0, 13, -1])
    def test_month_days_for_invalid_month(self, month):
        assert month_days(month, False) is None
