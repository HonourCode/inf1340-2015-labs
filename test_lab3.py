#!/usr/bin/env python3

""" Module to test lab3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_or_29 = ["February"]


def test_months_with_31():
    """
    Test months with 31 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31

# Write a test function for the months with 30 days
def test_months_with_30():
    """
    Test months with 30 days
    """
    for item in MONTHS_WITH_30:
        assert days_in_month(item) == 30

# Write a test function for the months with 28 or 29 days
def test_months_with_28_or_29():
    """
    Test months with 28 or 29 days
    """
    for item in MONTHS_WITH_28_or_29:
        assert days_in_month(item) == "28 or 29"

# Write a test function for months that are not capitalized properly
# Hint: use the lower() string method

def test_lower_months_with_31():
    """
    Test months with 31 days with lowercase entry
    """
    for item in MONTHS_WITH_31:
        item.lower()
        assert days_in_month(item) == 31


# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input
"""
try:
    some funtion call
except SomeError:
        We get here because an exception was raised
        assert False
"""


def test_wrong_strings():
    """
    Test for incorrect strings
    """

    wrong_strings = ["this", "can't", "be", "right", "12345"]
    for item in wrong_strings:
        try:
            days_in_month(item)
        except ValueError:
            assert True


def test_wrong_attribute():
    """
    Test for wrong data types
    """
    wrong_attributes = [1, 4.5, False, ["january", "March"]]
    for item in wrong_attributes:
        try:
            days_in_month(item) == False
        except AttributeError:
            assert True