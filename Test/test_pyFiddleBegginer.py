from pyFiddleBegginer import *
from imports import *
import pytest

def test_add_tuple():
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]
    assert add_tuple([], (1, 2, 3)) == [1, 2, 3]
    assert add_tuple([1, 2], ()) == [1, 2]

def test_ascii_value():
    assert ascii_value("A") == 65
    assert ascii_value("R") == 82
    assert ascii_value("S") == 83
    assert ascii_value("a") == 97
    assert ascii_value("z") == 122
    assert ascii_value("0") == 48
    assert ascii_value("9") == 57


def test_loss_amount():
    # Test cases to validate the loss_amount function
    assert loss_amount(1500, 1200) == 0  # No loss
    assert loss_amount(100, 200) == 100  # Loss of 100
    assert loss_amount(2000, 5000) == 3000  # Loss of 3000
    assert loss_amount(500, 500) == 0  # No loss when equal
    assert loss_amount(0, 100) == 100  # Loss when actual cost is 0

def test_is_30_day_month():
    # Test cases for months with 30 days
    assert is_30_day_month(4) == True  # April
    assert is_30_day_month(6) == True  # June
    assert is_30_day_month(9) == True  # September
    assert is_30_day_month(11) == True  # November

    # Test cases for months with 31 days
    assert is_30_day_month(1) == False  # January
    assert is_30_day_month(3) == False  # March
    assert is_30_day_month(5) == False  # May
    assert is_30_day_month(7) == False  # July
    assert is_30_day_month(8) == False  # August
    assert is_30_day_month(10) == False  # October
    assert is_30_day_month(12) == False  # December

    # Test case for February
    assert is_30_day_month(2) == False  # February

def test_all_characters_same():
    assert all_characters_same("aaa") == True
    assert all_characters_same("abc") == False
    assert all_characters_same("") == True
    assert all_characters_same("a") == True
    assert all_characters_same("abab") == False
    assert all_characters_same("1111") == True

def test_check_tuplex():
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), '5') == False
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3) == True
    assert check_tuplex(("a", "b", "c"), "d") == False
    assert check_tuplex((1, 2, 3), 2) == True

def test_are_all_dicts_empty():
    assert are_all_dicts_empty([{}, {}, {}]) == True
    assert are_all_dicts_empty([{}, {"key": "value"}, {}]) == False
    assert are_all_dicts_empty([]) == True
    assert are_all_dicts_empty([{"key": "value"}]) == False
    assert are_all_dicts_empty([{}]) == True

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False


def test_is_dict_empty():
    # Test with an empty dictionary
    assert is_dict_empty({}) == True
    # Test with a non-empty dictionary
    assert is_dict_empty({'key': 'value'}) == False
    # Test with another non-empty dictionary
    assert is_dict_empty({'a': 1, 'b': 2}) == False
    # Test with a dictionary containing a None value
    assert is_dict_empty({'key': None}) == False

def test_is_sorted():
    # Test cases for the is_sorted function
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([5, 4, 3, 2, 1]) == False
    assert is_sorted([1, 1, 2, 2]) == True
    assert is_sorted([]) == True  # An empty list is considered sorted
    assert is_sorted([42]) == True  # A single-element list is considered sorted
    assert is_sorted([1, 3, 2, 4]) == False
    assert is_sorted([1, 2, 3, 3, 4]) == True

def test_check_element():
    # Test cases for the check_element function
    assert check_element(["green", "orange", "black", "white"], 'blue') == False
    assert check_element([1, 2, 3, 4], 7) == False
    assert check_element(["green", "green", "green", "green"], 'green') == True
    assert check_element([], 1) == True  # Edge case: empty list
    assert check_element([1, 1, 1, 1], 1) == True
    assert check_element([1, 1, 1, 2], 1) == False

def test_has_31_days():
    # Test cases for months with 31 days
    assert has_31_days(1) == True  # January
    assert has_31_days(3) == True  # March
    assert has_31_days(5) == True  # May
    assert has_31_days(7) == True  # July
    assert has_31_days(8) == True  # August
    assert has_31_days(10) == True # October
    assert has_31_days(12) == True # December

    # Test cases for months without 31 days
    assert has_31_days(2) == False # February
    assert has_31_days(4) == False # April
    assert has_31_days(6) == False # June
    assert has_31_days(9) == False # September
    assert has_31_days(11) == False # November

def test_noprofit_noloss():
    assert noprofit_noloss(1500, 1200) == False
    assert noprofit_noloss(100, 100) == True
    assert noprofit_noloss(2000, 5000) == False
    assert noprofit_noloss(0, 0) == True
    assert noprofit_noloss(500, 499) == False

def test_unique_element():
    assert unique_element([1, 1, 1]) == True
    assert unique_element([1, 2, 1, 2]) == False
    assert unique_element([1, 2, 3, 4, 5]) == False
    assert unique_element([]) == False  # Edge case: empty list
    assert unique_element([7]) == True  # Edge case: single element list

def test_check_distinct():
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True
    assert check_distinct(()) == True  # Empty tuple case
    assert check_distinct(("a", "b", "c", "a")) == False
    assert check_distinct(("a", "b", "c")) == True

def test_check_none():
    assert check_none((10, 4, 5, 6, None)) == True
    assert check_none((7, 8, 9, 11, 14)) == False
    assert check_none((1, 2, 3, 4, None)) == True
    assert check_none(()) == False
    assert check_none((None,)) == True
    assert check_none((0, '', False, None)) == True

def test_check_k():
    assert check_k((10, 4, 5, 6, 8), 6) == True
    assert check_k((1, 2, 3, 4, 5, 6), 7) == False
    assert check_k((7, 8, 9, 44, 11, 12), 11) == True
    assert check_k((), 1) == False
    assert check_k((1, 2, 3), 3) == True

def test_all_unique():
    # Test cases for the all_unique function
    assert all_unique([1, 2, 3]) == True, "Test case 1 failed"
    assert all_unique([1, 2, 1, 2]) == False, "Test case 2 failed"
    assert all_unique([1, 2, 3, 4, 5]) == True, "Test case 3 failed"
    assert all_unique([]) == True, "Test case 4 failed (empty list)"
    assert all_unique([1]) == True, "Test case 5 failed (single element)"
    assert all_unique([1, 1, 1, 1]) == False, "Test case 6 failed (all elements same)"
    assert all_unique(['a', 'b', 'c']) == True, "Test case 7 failed (string elements)"
    assert all_unique(['a', 'b', 'a']) == False, "Test case 8 failed (repeated string)"

def test_is_word_length_odd():
    assert is_word_length_odd("hello") == True  # Length is 5 (odd)
    assert is_word_length_odd("world") == True  # Length is 5 (odd)
    assert is_word_length_odd("Python") == False # Length is 6 (even)
    assert is_word_length_odd("") == False      # Empty string is considered even

def test_circle_circumference():
    assert math.isclose(circle_circumference(10), 62.83, rel_tol=0.001)
    assert math.isclose(circle_circumference(5), 31.415, rel_tol=0.001)
    assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)

def test_closest_smaller_number():
    assert closest_smaller_number(11) == 10
    assert closest_smaller_number(7) == 6
    assert closest_smaller_number(12) == 11
    assert closest_smaller_number(2) == 1
    assert closest_smaller_number(100) == 99

def test_degrees_to_radians():
    assert degrees_to_radians(90) == 1.5707963267948966
    assert degrees_to_radians(60) == 1.0471975511965976
    assert degrees_to_radians(120) == 2.0943951023931953
    assert degrees_to_radians(0) == 0.0
    assert degrees_to_radians(180) == 3.141592653589793

def test_list_to_tuple():
    assert list_to_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)
    assert list_to_tuple([2, 4, 5, 6, 2, 3, 4, 4, 7]) == (2, 4, 5, 6, 2, 3, 4, 4, 7)
    assert list_to_tuple([58, 44, 56]) == (58, 44, 56)
    assert list_to_tuple([]) == ()
    assert list_to_tuple(['a', 'b', 'c']) == ('a', 'b', 'c')

def test_convert_to_lowercase():
    assert convert_to_lowercase("InValid") == "invalid"
    assert convert_to_lowercase("TruE") == "true"
    assert convert_to_lowercase("SenTenCE") == "sentence"
    assert convert_to_lowercase("123ABC") == "123abc"
    assert convert_to_lowercase("") == ""  # Test with an empty string

def test_convert_to_uppercase():
    # Test with lowercase string
    assert convert_to_uppercase("hello") == "HELLO"
    # Test with mixed case string
    assert convert_to_uppercase("Python") == "PYTHON"
    # Test with string containing numbers
    assert convert_to_uppercase("123abc") == "123ABC"
    # Test with empty string
    assert convert_to_uppercase("") == ""

def test_count_characters():
    assert count_characters("python programming") == 18
    assert count_characters("language") == 8
    assert count_characters("words") == 5
    assert count_characters("") == 0
    assert count_characters(" ") == 1
    assert count_characters("12345") == 5
    assert count_characters("!@#$%") == 5

def test_count_digits():
    assert count_digits("program2bedone") == 1
    assert count_digits("3wonders") == 1
    assert count_digits("123") == 3
    assert count_digits("3wond-1ers2") == 3
    assert count_digits("no digits here") == 0
    assert count_digits("") == 0
    assert count_digits("123abc456") == 6

def test_count_occurrences():
    assert count_occurrences((1, 2, 3, 2, 4, 2), 2) == 3
    assert count_occurrences(("a", "b", "a", "c"), "a") == 2
    assert count_occurrences((5, 6, 7), 8) == 0
    assert count_occurrences((), 1) == 0
    assert count_occurrences((None, None, None), None) == 3
