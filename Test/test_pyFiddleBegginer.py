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

def test_count_equal_numbers():
    assert count_equal_numbers(1, 1, 1) == 3
    assert count_equal_numbers(1, 2, 3) == 0
    assert count_equal_numbers(1, 2, 2) == 2
    assert count_equal_numbers(5, 5, 6) == 2
    assert count_equal_numbers(-1, -1, -1) == 3
    assert count_equal_numbers(0, 0, 1) == 2
    assert count_equal_numbers(7, 8, 9) == 0

def test_count_integer_elements():
    assert count_integer_elements([1, 2, 'abc', 1.2]) == 2
    assert count_integer_elements([1, 2, 3]) == 3
    assert count_integer_elements([1, 1.2, 4, 5.1]) == 2
    assert count_integer_elements([]) == 0
    assert count_integer_elements(['a', 'b', 'c']) == 0
    assert count_integer_elements([1, 2.0, 3, 4.5, 5]) == 3

def test_count_nested_lists():
    # Test cases for the count_nested_lists function
    assert count_nested_lists([[1, 2], [3, 4], 5, [6]]) == 3
    assert count_nested_lists([1, 2, 3]) == 0
    assert count_nested_lists([[1], [2], [3], [4]]) == 4
    assert count_nested_lists([]) == 0
    assert count_nested_lists([[], [1, 2], "string", 42, [3]]) == 3

def test_frequency():
    assert frequency([1, 2, 3], 4) == 0
    assert frequency([1, 2, 2, 3, 3, 3, 4], 3) == 3
    assert frequency([0, 1, 2, 3, 1, 2], 1) == 2
    assert frequency([], 1) == 0
    assert frequency([1, 1, 1, 1], 1) == 4
    assert frequency([1, 2, 3, 4, 5], 6) == 0

def test_count_odd_numbers():
    assert count_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert count_odd_numbers([2, 4, 6, 8, 10]) == 0
    assert count_odd_numbers([1, 3, 5, 7, 9]) == 5
    assert count_odd_numbers([]) == 0

def test_count_positive_numbers():
    assert count_positive_numbers([1, -2, 3, -4]) == 2
    assert count_positive_numbers([3, 4, 5, -1]) == 3
    assert count_positive_numbers([1, 2, 3, 4]) == 4
    assert count_positive_numbers([-1, -2, -3, -4]) == 0
    assert count_positive_numbers([]) == 0

def test_count_occurrences():
    assert count_occurrences("letstdlenstdporstd") == 3
    assert count_occurrences("truststdsolensporsd") == 1
    assert count_occurrences("makestdsostdworthit") == 2
    assert count_occurrences("stds") == 1
    assert count_occurrences("") == 0
    assert count_occurrences("stdstd") == 2
    assert count_occurrences("st") == 0
    assert count_occurrences("std") == 1

def test_count_true_booleans():
    assert count_true_booleans([True, False, True]) == 2
    assert count_true_booleans([False, False]) == 0
    assert count_true_booleans([True, True, True]) == 3
    assert count_true_booleans([]) == 0
    assert count_true_booleans([False, True, False, True, False]) == 2

def test_count_uppercase():
    assert count_uppercase("Hello World") == 2
    assert count_uppercase("python") == 0
    assert count_uppercase("PYTHON") == 6
    assert count_uppercase("12345") == 0
    assert count_uppercase("MixedCASE") == 5
    assert count_uppercase("") == 0

def test_count_vowels():
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("Python is awesome") == 6
    assert count_vowels("No vowels here") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("") == 0

def test_new_tuple():
    # Test cases
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')
    assert new_tuple([], "Empty") == ('Empty',)
    assert new_tuple(["Only"], "One") == ('Only', 'One')

def test_volume_cube():
    assert volume_cube(3) == 27.0
    assert volume_cube(2) == 8.0
    assert volume_cube(5) == 125.0
    assert volume_cube(1.5) == 3.375
    assert volume_cube(0.1) == 0.001

def test_volume_cylinder():
    assert math.isclose(volume_cylinder(10, 5), 1570.75, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4, 5), 251.32, rel_tol=0.001)
    assert math.isclose(volume_cylinder(4, 10), 502.64, rel_tol=0.001)

def test_decimal_to_binary():
    assert decimal_to_binary(8) == '1000'
    assert decimal_to_binary(18) == '10010'
    assert decimal_to_binary(7) == '111'
    assert decimal_to_binary(0) == '0'
    assert decimal_to_binary(1) == '1'
    assert decimal_to_binary(255) == '11111111'

def test_big_diff():
    assert big_diff([1, 2, 3, 4]) == 3
    assert big_diff([4, 5, 12]) == 8
    assert big_diff([9, 2, 3]) == 7
    assert big_diff([-10, 0, 10]) == 20
    assert big_diff([100, 100, 100]) == 0

def test_is_divisible_by_11():
    # Test cases for the is_divisible_by_11 function
    assert is_divisible_by_11(121) == True  # 121 is divisible by 11
    assert is_divisible_by_11(123) == False  # 123 is not divisible by 11
    assert is_divisible_by_11(0) == True  # 0 is divisible by 11
    assert is_divisible_by_11(-11) == True  # -11 is divisible by 11
    assert is_divisible_by_11(22) == True  # 22 is divisible by 11
    assert is_divisible_by_11(23) == False  # 23 is not divisible by 11

def test_divisible_numbers():
    assert divisible_numbers([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]) == "2001,2004,2007"
    assert divisible_numbers([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]) == "2010,2013,2019"
    assert divisible_numbers([2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]) == "2022,2025,2028"
    assert divisible_numbers([2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039]) == "2031,2034"
    assert divisible_numbers([]) == ""

def test_dog_age():
    assert dog_age(1) == 10.5
    assert dog_age(2) == 21.0
    assert dog_age(3) == 25.0
    assert dog_age(10) == 53.0
    assert dog_age(0) == 0.0

def test_drop():
    assert drop(3, [1, 2, 3, 4, 5]) == [4, 5]
    assert drop(2, [10, 20, 30, 40, 50]) == [30, 40, 50]
    assert drop(5, [1, 2, 3]) == []
    assert drop(0, [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert drop(4, []) == []

def test_drop_empty():
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}) == {'c1': 'Red', 'c2': 'Green'}
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3': None}) == {'c1': 'Red'}
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3': None}) == {'c2': 'Green'}
    assert drop_empty({}) == {}
    assert drop_empty({'c1': None, 'c2': None}) == {}

def test_check_voting_eligibility():
    assert check_voting_eligibility(20) == "Eligible to vote"
    assert check_voting_eligibility(16) == "Not eligible to vote"
    assert check_voting_eligibility(18) == "Eligible to vote"

def test_exclude_first_last_items():
    assert exclude_first_last_items([1, 2, 3, 4, 5]) == [2, 3, 4]
    assert exclude_first_last_items(["apple", "banana", "cherry"]) == ["banana"]
    assert exclude_first_last_items(["Hello", "World"]) == []
    assert exclude_first_last_items([1]) == []
    assert exclude_first_last_items([]) == []

def test_extract_first_elements():
    assert extract_first_elements([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert extract_first_elements([[1, 2, 3], [4, 5]]) == [1, 4]
    assert extract_first_elements([[9, 8, 1], [1, 2]]) == [9, 1]
    assert extract_first_elements([[10], [20], [30]]) == [10, 20, 30]
    assert extract_first_elements([["a", "b"], ["c", "d"]]) == ["a", "c"]

def test_rear_extract():
    assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
    assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
    assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]

def test_filter_negatives():
    assert filter_negatives([-1, 4, 5, -6]) == [-1, -6]
    assert filter_negatives([-1, -2, 3, 4]) == [-1, -2]
    assert filter_negatives([-7, -6, 8, 9]) == [-7, -6]
    assert filter_negatives([1, 2, 3, 4]) == []
    assert filter_negatives([]) == []

def test_filter_odds():
    assert filter_odds([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    assert filter_odds([10, 11, 12, 13]) == [11, 13]
    assert filter_odds([7, 8, 9, 1]) == [7, 9, 1]
    assert filter_odds([]) == []
    assert filter_odds([2, 4, 6, 8]) == []
    assert filter_odds([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_filter_odd_numbers():
    assert filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
    assert filter_odd_numbers([10, 20, 45, 67, 84, 93]) == [45, 67, 93]
    assert filter_odd_numbers([5, 7, 9, 8, 6, 4, 3]) == [5, 7, 9, 3]
    assert filter_odd_numbers([]) == []
    assert filter_odd_numbers([2, 4, 6, 8]) == []
    assert filter_odd_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_cube_nums():
    # Test cases to validate the solution
    assert cube_nums([1, 2, 3, 4, 5]) == [1, 8, 27, 64, 125]
    assert cube_nums([10, 20, 30]) == [1000, 8000, 27000]
    assert cube_nums([12, 15]) == [1728, 3375]
    assert cube_nums([]) == []  # Test with an empty list
    assert cube_nums([-1, -2, -3]) == [-1, -8, -27]  # Test with negative numbers

def test_find_even_numbers():
    # Test cases to validate the solution
    assert find_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_numbers([4, 5, 6, 7, 8, 0, 1]) == [4, 6, 8, 0]
    assert find_even_numbers([8, 12, 15, 19]) == [8, 12]
    assert find_even_numbers([]) == []  # Test with an empty list
    assert find_even_numbers([1, 3, 5]) == []  # Test with no even numbers
    assert find_even_numbers([2, 4, 6]) == [2, 4, 6]  # Test with all even numbers

def test_first_digit():
    assert first_digit(123) == 1
    assert first_digit(-456) == 4
    assert first_digit(7) == 7
    assert first_digit(987654321) == 9
    assert first_digit(-10) == 1

def test_last_digit():
    assert last_digit(123) == 3
    assert last_digit(-25) == 5
    assert last_digit(0) == 0
    assert last_digit(987654321) == 1
    assert last_digit(-987654321) == 1

def test_smallest_num():
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45
    assert smallest_num([-10, -20, -1, -45, -99]) == -99
    assert smallest_num([0, 0, 0]) == 0

def test_generate_dictionary():
    assert generate_dictionary(1) == {1: 1}
    assert generate_dictionary(2) == {1: 1, 2: 4}
    assert generate_dictionary(3) == {1: 1, 2: 4, 3: 9}
    assert generate_dictionary(4) == {1: 1, 2: 4, 3: 9, 4: 16}
    assert generate_dictionary(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert generate_dictionary(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def test_create_empty_dicts():
    assert create_empty_dicts(5) == [{}, {}, {}, {}, {}]
    assert create_empty_dicts(0) == []
    assert create_empty_dicts(3) == [{}, {}, {}]
    assert create_empty_dicts(1) == [{}]
    assert create_empty_dicts(10) == [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

def test_find_quotient():
    assert find_quotient(10, 3) == 3
    assert find_quotient(4, 2) == 2
    assert find_quotient(20, 5) == 4
    assert find_quotient(7, 3) == 2
    assert find_quotient(-10, 3) == -4
    assert find_quotient(10, -3) == -4
    assert find_quotient(-10, -3) == 3

def test_lateral_surface_area():
    assert lateral_surface_area(5) == 100
    assert lateral_surface_area(9) == 324
    assert lateral_surface_area(10) == 400
    assert lateral_surface_area(0) == 0
    assert lateral_surface_area(1) == 4

def test_multiply_list():
    assert multiply_list([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
    assert multiply_list([0, 10, 20, 30]) == [0, 20, 40, 60]
    assert multiply_list([-1, -2, -3, -4]) == [-2, -4, -6, -8]
    assert multiply_list([]) == []

def test_order_list():
    assert order_list(["banana", "apple", "grapes", "melon", "kiwi"]) == ['melon', 'kiwi', 'grapes', 'banana', 'apple']
    assert order_list(["zebra", "lion", "tiger", "elephant"]) == ['zebra', 'tiger', 'lion', 'elephant']
    assert order_list(["orange", "apple", "banana", "grapefruit"]) == ['orange', 'grapefruit', 'banana', 'apple']
    assert order_list([]) == []

def test_maximum():
    # Test cases to validate the maximum function
    assert maximum(5, 10) == 10
    assert maximum(-1, -2) == -1
    assert maximum(9, 7) == 9
    assert maximum(0, 0) == 0
    assert maximum(3.5, 2.5) == 3.5
    assert maximum(-3.5, -2.5) == -2.5

def test_median_trapezium():
    # Test cases for the median_trapezium function
    assert median_trapezium(15, 25) == 20.0
    assert median_trapezium(10, 20) == 15.0
    assert median_trapezium(6, 9) == 7.5
    assert median_trapezium(0, 0) == 0.0
    assert median_trapezium(5, 15) == 10.0

def test_median_of_three():
    assert median_of_three(25, 55, 65) == 55
    assert median_of_three(20, 10, 30) == 20
    assert median_of_three(15, 45, 75) == 45
    assert median_of_three(5, 5, 5) == 5
    assert median_of_three(0, -1, 1) == 0

def test_min_of_three():
    # Test cases to validate the solution
    assert min_of_three(10, 20, 0) == 0
    assert min_of_three(19, 15, 18) == 15
    assert min_of_three(-10, -20, -30) == -30
    assert min_of_three(5, 5, 5) == 5
    assert min_of_three(0, -1, 1) == -1

def test_minimum():
    assert minimum(1, 2) == 1
    assert minimum(-5, -4) == -5
    assert minimum(0, 0) == 0
    assert minimum(10, -10) == -10
    assert minimum(3.5, 2.5) == 2.5
    assert minimum(-1.1, -1.2) == -1.2

def test_classify_number():
    assert classify_number(5) == "Positive"
    assert classify_number(-10) == "Negative"
    assert classify_number(0) == "Zero"

def test_perimeter_pentagon():
    assert perimeter_pentagon(5) == 25
    assert perimeter_pentagon(10) == 50
    assert perimeter_pentagon(15) == 75
    assert perimeter_pentagon(0.5) == 2.5
    assert perimeter_pentagon(1.2) == 6.0

def test_rectangle_area():
    # Test cases for the rectangle_area function
    assert rectangle_area(10, 20) == 200
    assert rectangle_area(10, 5) == 50
    assert rectangle_area(4, 2) == 8
    assert rectangle_area(1, 1) == 1
    assert rectangle_area(15, 10) == 150

def test_remove_odd_characters():
    assert remove_odd_characters("python") == "pto"
    assert remove_odd_characters("programming") == "pormig"
    assert remove_odd_characters("language") == "lnug"
    assert remove_odd_characters("") == ""
    assert remove_odd_characters("a") == "a"

def test_remove_odd():
    # Test cases
    assert remove_odd([1, 2, 3, 4, 5]) == [2, 4]
    assert remove_odd([10, 15, 20, 25]) == [10, 20]
    assert remove_odd([2, 4, 6]) == [2, 4, 6]
    assert remove_odd([1, 3, 5]) == []
    assert remove_odd([]) == []
    assert remove_odd([0, 1, 2, 3, 4]) == [0, 2, 4]

def test_remove_whitespaces():
    assert remove_whitespaces(" Google    Flutter ") == "GoogleFlutter"
    assert remove_whitespaces(" iOS    Swift ") == "iOSSwift"
    assert remove_whitespaces(" Python  Programming ") == "PythonProgramming"
    assert remove_whitespaces("") == ""
    assert remove_whitespaces("NoSpacesHere") == "NoSpacesHere"

def test_replace_blank():
    assert replace_blank("hello world", "-") == "hello-world"
    assert replace_blank("python programming", "*") == "python*programming"
    assert replace_blank("replace spaces", "_") == "replace_spaces"
    assert replace_blank("no spaces", "#") == "no#spaces"
    assert replace_blank("", "$") == ""  # Test with an empty string

def test_replace_characters():
    assert replace_characters("polygon", 'y', 'l') == "pollgon"
    assert replace_characters("character", 'c', 'a') == "aharaater"
    assert replace_characters("python", 'l', 'a') == "python"
    assert replace_characters("hello world", 'o', 'a') == "hella warld"
    assert replace_characters("test case", 't', 'p') == "pesp case"
    assert replace_characters("example", 'z', 'x') == "example"

def test_replace_last_element():
    assert replace_last_element([1, 2, 3], [4, 5]) == [1, 2, 4, 5]
    assert replace_last_element(['a', 'b', 'c'], ['x', 'y', 'z']) == ['a', 'b', 'x', 'y', 'z']
    assert replace_last_element([10], [20, 30]) == [20, 30]
    assert replace_last_element([], [1, 2]) == [1, 2]
    assert replace_last_element([1, 2, 3], []) == [1, 2]

def test_replace_spaces():
    assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
    assert replace_spaces("I am a Programmer") == 'I%20am%20a%20Programmer'
    assert replace_spaces("I love Coding") == 'I%20love%20Coding'
    assert replace_spaces("") == ''  # Test with an empty string
    assert replace_spaces("NoSpacesHere") == 'NoSpacesHere'  # Test with no spaces
    assert replace_spaces(" ") == '%20'  # Test with a single space

def test_surface_area_of_sphere():
    assert math.isclose(surface_area_of_sphere(10), 1256.6370614359173, rel_tol=0.001)
    assert math.isclose(surface_area_of_sphere(15), 2827.4333882308138, rel_tol=0.001)
    assert math.isclose(surface_area_of_sphere(20), 5026.548245743669, rel_tol=0.001)

def test_volume_of_sphere():
    assert math.isclose(volume_of_sphere(10), 4188.790204786391, rel_tol=0.001)
    assert math.isclose(volume_of_sphere(25), 65449.84694978735, rel_tol=0.001)
    assert math.isclose(volume_of_sphere(20), 33510.32163829113, rel_tol=0.001)

def test_split_two_parts():
    assert split_two_parts([1, 2, 3, 4, 5], 3) == ([1, 2, 3], [4, 5])
    assert split_two_parts(['a', 'b', 'c', 'd'], 2) == (['a', 'b'], ['c', 'd'])
    assert split_two_parts([1, 2, 3], 0) == ([], [1, 2, 3])
    assert split_two_parts([1, 2, 3], 5) == ([1, 2, 3], [])
    assert split_two_parts([], 2) == ([], [])
    assert split_two_parts([1, 2, 3], -1) == ([], [1, 2, 3])

def test_generate_list():
    assert generate_list("34,67,55,33,12,98") == ['34', '67', '55', '33', '12', '98']
    assert generate_list("1,2,3,4,5") == ['1', '2', '3', '4', '5']
    assert generate_list("10,20,30,40,50") == ['10', '20', '30', '40', '50']
    assert generate_list("") == []

def test_split_string():
    # Test cases to validate the solution
    assert split_string("python") == ['p', 'y', 't', 'h', 'o', 'n']
    assert split_string("Name") == ['N', 'a', 'm', 'e']
    assert split_string("program") == ['p', 'r', 'o', 'g', 'r', 'a', 'm']
    assert split_string("") == []  # Test with an empty string
    assert split_string("a") == ['a']  # Test with a single character

def test_square_nums():
    # Test cases to validate the solution
    assert square_nums([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert square_nums([10, 20, 30]) == [100, 400, 900]
    assert square_nums([12, 15]) == [144, 225]
    assert square_nums([]) == []  # Test with an empty list
    assert square_nums([-1, -2, -3]) == [1, 4, 9]  # Test with negative numbers

def test_square_perimeter():
    assert square_perimeter(10) == 40
    assert square_perimeter(5) == 20
    assert square_perimeter(4) == 16
    assert square_perimeter(0.5) == 2.0
    assert square_perimeter(1.25) == 5.0

def test_reverse_string():
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"
    assert reverse_string("Python is awesome") == "emosewa si nohtyP"
    assert reverse_string("No reversal here") == "ereh lasrever oN"
    assert reverse_string("") == ""

def test_string_to_list():
    assert string_to_list("python programming") == ['python', 'programming']
    assert string_to_list("lists tuples strings") == ['lists', 'tuples', 'strings']
    assert string_to_list("write a program") == ['write', 'a', 'program']
    assert string_to_list("") == ['']  # Edge case: empty string
    assert string_to_list("singleword") == ['singleword']  # Edge case: single word

def test_string_to_tuple():
    assert string_to_tuple("hello") == ('h', 'e', 'l', 'l', 'o')
    assert string_to_tuple("123") == ('1', '2', '3')
    assert string_to_tuple("a b") == ('a', ' ', 'b')
    assert string_to_tuple("") == ()
    assert string_to_tuple("!@#") == ('!', '@', '#')

def test_sum_and_average():
    assert sum_and_average(10) == (55, 5.5)
    assert sum_and_average(15) == (120, 8.0)
    assert sum_and_average(20) == (210, 10.5)
    assert sum_and_average(1) == (1, 1.0)
    assert sum_and_average(5) == (15, 3.0)

def test_sum_lists():
    assert sum_lists([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert sum_lists([10, 20, 30], [15, 25, 35]) == [25, 45, 65]
    assert sum_lists([0, 0, 0], [1, 1, 1]) == [1, 1, 1]
    assert sum_lists([-1, -2, -3], [1, 2, 3]) == [0, 0, 0]
    assert sum_lists([100, 200, 300], [400, 500, 600]) == [500, 700, 900]

def test_return_sum():
    assert return_sum({'a': 100, 'b': 200, 'c': 300}) == 600
    assert return_sum({'x': 25, 'y': 18, 'z': 45}) == 88
    assert return_sum({'p': 36, 'q': 39, 'r': 49}) == 124
    assert return_sum({}) == 0  # Test with an empty dictionary
    assert return_sum({'only_key': 42}) == 42  # Test with a single key-value pair

def test_big_sum():
    assert big_sum([1, 2, 3]) == 4
    assert big_sum([-1, 2, 3, 4]) == 3
    assert big_sum([2, 3, 6]) == 8
    assert big_sum([0, 0, 0]) == 0
    assert big_sum([-5, -1, -3]) == -6

def test_sum_negative_numbers():
    assert sum_negative_numbers([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
    assert sum_negative_numbers([10, 15, -14, 13, -18, 12, -20]) == -52
    assert sum_negative_numbers([19, -65, 57, 39, 152, -639, 121, 44, 90, -190]) == -894
    assert sum_negative_numbers([]) == 0
    assert sum_negative_numbers([1, 2, 3, 4, 5]) == 0
    assert sum_negative_numbers([-1, -2, -3, -4, -5]) == -15

def test_sum_of_array():
    assert sum_of_array([1, 2, 3]) == 6
    assert sum_of_array([15, 12, 13, 10]) == 50
    assert sum_of_array([0, 1, 2]) == 3
    assert sum_of_array([]) == 0
    assert sum_of_array([-1, -2, -3]) == -6
    assert sum_of_array([100]) == 100

def test_surface_area_of_cube():
    assert surface_area_of_cube(5) == 150
    assert surface_area_of_cube(3) == 54
    assert surface_area_of_cube(10) == 600
    assert surface_area_of_cube(1) == 6
    assert surface_area_of_cube(0) == 0

def test_swap_first_last():
    assert swap_first_last([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    assert swap_first_last([1, 2, 3]) == [3, 2, 1]
    assert swap_first_last([4]) == [4]
    assert swap_first_last([]) == []
    assert swap_first_last([7, 8]) == [8, 7]

def test_swap_numbers():
    assert swap_numbers(10, 20) == (20, 10)
    assert swap_numbers(15, 17) == (17, 15)
    assert swap_numbers(100, 200) == (200, 100)
    assert swap_numbers(-5, 5) == (5, -5)
    assert swap_numbers(0, 0) == (0, 0)

def test_take():
    assert take(3, [1, 2, 3, 4, 5]) == [1, 2, 3]
    assert take(2, [10, 20, 30, 40, 50]) == [10, 20]
    assert take(5, [1, 2, 3]) == [1, 2, 3]
    assert take(0, [1, 2, 3, 4, 5]) == []
    assert take(4, []) == []

def test_toggle_case():
    assert toggle_case("Python") == "pYTHON"
    assert toggle_case("Pangram") == "pANGRAM"
    assert toggle_case("LIttLE") == "liTTle"
    assert toggle_case("HELLO") == "hello"
    assert toggle_case("world") == "WORLD"

def test_find_volume():
    assert find_volume(10, 8, 6) == 240.0
    assert find_volume(3, 2, 2) == 6.0
    assert find_volume(1, 2, 1) == 1.0
    assert find_volume(0, 5, 10) == 0.0
    assert find_volume(5, 0, 10) == 0.0
    assert find_volume(5, 10, 0) == 0.0

def test_tuple_size():
    assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
    assert tuple_size((1, "Raju", 2, "Nikhil", 3, "Deepanshu")) == sys.getsizeof((1, "Raju", 2, "Nikhil", 3, "Deepanshu"))
    assert tuple_size(((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))) == sys.getsizeof(((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf")))

def test_tuple_to_string():
    assert tuple_to_string(('h', 'e', 'l', 'l', 'o')) == "hello"
    assert tuple_to_string(('P', 'y', 't', 'h', 'o', 'n')) == "Python"
    assert tuple_to_string(('1', '2', '3')) == "123"
    assert tuple_to_string(()) == ""  # Test with an empty tuple
    assert tuple_to_string(('a',)) == "a"  # Test with a single character tuple