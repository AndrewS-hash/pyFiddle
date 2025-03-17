from pyFiddle_Intermediate import *
from imports import *
import pytest


def test_find_hypotenuse():
    assert find_hypotenuse(3, 4) == 5.0
    assert find_hypotenuse(5, 12) == 13.0
    assert find_hypotenuse(8, 15) == 17.0
    assert find_hypotenuse(7, 24) == 25.0
    assert find_hypotenuse(1, 1) == 1.41

def test_Cubes():
    assert cubes(2) == 8
    assert cubes(3) == 27, "Test case cubes(3) failed"
    assert cubes(4) == 64, "Test case cubes(4) failed"
    assert cubes(5) == 125, "Test case cubes(5) failed"
    assert cubes(10) == 1000, "Test case cubes(10) failed"

def test_CalcAge():
    assert calc_age(10) == 3650, "Test case 10 Failed"
    assert calc_age(0) == 0, "Test case 0 failed"
    assert calc_age(73) == 26645, "test case 73 Failed"

def test_HowManySecounds():
    assert how_many_secounds(2) == 7200
    assert how_many_secounds(10) == 36000
    assert how_many_secounds(24) == 86400
    assert how_many_secounds(36) == 129600

def test_FootballPoints():
    assert football_points(1, 2, 3) == 5
    assert football_points(5, 5, 5) == 20
    assert football_points(1, 0, 0) == 3
    assert football_points(0, 7, 0) == 7
    assert football_points(0, 0, 15) == 0

def test_GetFirstValue():
    assert get_first_value([1, 2, 3]) == 1
    assert get_first_value([80, 5, 100]) == 80
    assert get_first_value([-500, 0, 50]) == -500
    assert get_first_value([5, 2, 3]) == 5
    assert get_first_value([75675, 5, 100]) == 75675
    assert get_first_value([-52320, 0, 50]) == -52320

def test_Animals():
    assert animals(5, 2, 8) == 50
    assert animals(3, 4, 7) == 50
    assert animals(1, 2, 3) == 22
    assert animals(3, 5, 2) == 34

def test_ReturnMeSomething():
    assert give_me_something("a") == "something a"
    assert give_me_something("is cooking") == "something is cooking"
    assert give_me_something(" is cooking") == "something  is cooking"

def test_Points():
    assert points(1, 1) == 5
    assert points(1, 2) == 8
    assert points(2, 1) == 7
    assert points(2, 2) == 10
    assert points(69, 420) == 1398

def test_Greeting():
    assert greeting("Matt") == "Hello, Matt!"
    assert greeting("Helen") == "Hello, Helen!"
    assert greeting("Mubashir") == "Hello, my Love!"

def test_FindLargestNum():
    assert findLargestNum([4, 5, 1, 3]) == 5
    assert findLargestNum([13, 27, 18, 26]) == 27
    assert findLargestNum([32, 35, 37, 39]) == 39
    assert findLargestNum([1000, 1001, 857, 1]) == 1001
    assert findLargestNum([27364, 837363, 736736, 73635]) == 837363
    assert findLargestNum([30, 2, 40, 3]) == 40
    assert findLargestNum([0, 1, 0, 0, 1]) == 1

def test_validate_email_address():
    assert validate_email_address("info@example.com") == True
    assert validate_email_address("user@domain") == False
    assert validate_email_address("user@domain.") == False
    assert validate_email_address("user@domain.c") == False
    assert validate_email_address("user@domain.com") == True
    assert validate_email_address("@test.com") == False
    assert validate_email_address("a@test.com") == True
    assert validate_email_address("abc@t.co") == True
    assert validate_email_address("abc@.te") == False
    assert validate_email_address("abc@t.te") == True

def test_calculate_exponential_power():
    assert calculate_exponential_power(5) == 25
    assert calculate_exponential_power(0) == 0
    assert calculate_exponential_power(1) == 1
    assert calculate_exponential_power(10) == 100

def test_extract_nth_element():
    input_list = [
        ('Greyson Fulton', 98, 99),
        ('Brady Kent', 97, 96),
        ('Wyatt Knott', 91, 94),
        ('Beau Turnbull', 94, 98)
    ]
    assert extract_nth_element(input_list, 0) == ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
    assert extract_nth_element(input_list, 2) == [99, 96, 94, 98]
    assert extract_nth_element(input_list, 1) == [98, 97, 91, 94]
    assert extract_nth_element([], 0) == []
    assert extract_nth_element([(1, 2, 3)], 1) == [2]

def test_extract_rear():
    assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
    assert extract_rear(('Avenge', 'for', 'People')) == ['e', 'r', 'e']
    assert extract_rear(('Gotta', 'get', 'go')) == ['a', 't', 'o']
    assert extract_rear(('Python', 'is', 'fun')) == ['n', 's', 'n']
    assert extract_rear(('a', 'b', 'c')) == ['a', 'b', 'c']

def test_extract_values():
    assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
    assert extract_values('"red","blue","green","yellow"') == ['red', 'blue', 'green', 'yellow']
    assert extract_values('"python","program","language"') == ['python', 'program', 'language']
    assert extract_values('No quotes here') == []
    assert extract_values('"single"') == ['single']

def test_extract_string():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 6) == ['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 9) == ['exercises']
    assert extract_string(['a', 'ab', 'abc', 'abcd'], 2) == ['ab']
    assert extract_string([], 3) == []

def test_filter_dict_by_value():
    input_data = {
        'Cierra Vega': 175,
        'Alden Cantrell': 180,
        'Kierra Gentry': 165,
        'Pierre Cox': 190
    }

    assert filter_dict_by_value(input_data, 170) == {
        'Cierra Vega': 175,
        'Alden Cantrell': 180,
        'Pierre Cox': 190
    }

    assert filter_dict_by_value(input_data, 180) == {
        'Alden Cantrell': 180,
        'Pierre Cox': 190
    }

    assert filter_dict_by_value(input_data, 190) == {
        'Pierre Cox': 190
    }

    assert filter_dict_by_value(input_data, 200) == {}

    assert filter_dict_by_value({}, 100) == {}

def test_filter_students():
    students = {
        'Cierra Vega': (6.2, 70),
        'Alden Cantrell': (5.9, 65),
        'Kierra Gentry': (6.0, 68),
        'Pierre Cox': (5.8, 66)
    }
    assert filter_students(students, 6.0, 70) == {'Cierra Vega': (6.2, 70)}
    assert filter_students(students, 5.9, 67) == {'Cierra Vega': (6.2, 70), 'Kierra Gentry': (6.0, 68)}
    assert filter_students(students, 5.7, 64) == {
        'Cierra Vega': (6.2, 70),
        'Alden Cantrell': (5.9, 65),
        'Kierra Gentry': (6.0, 68),
        'Pierre Cox': (5.8, 66)
    }

def test_find_dissimilar():
    assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10) or find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (7, 10, 3, 6)
    assert find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9) or find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (7, 9, 1, 4)
    assert find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (34, 36, 11, 25) or find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (11, 25, 34, 36)

def test_find_adverb_position():
    assert find_adverb_position("clearly!! we can see the sky") == (0, 7, 'clearly')
    assert find_adverb_position("seriously!! there are many roses") == (0, 9, 'seriously')
    assert find_adverb_position("unfortunately!! sita is going to home") == (0, 13, 'unfortunately')
    assert find_adverb_position("no adverbs here") == None
    assert find_adverb_position("happily ever after") == (0, 7, 'happily')
    assert find_adverb_position("sadly, it is true") == (0, 5, 'sadly')

def test_find_first_occurrence():
    assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
    assert find_first_occurrence([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 2
    assert find_first_occurrence([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6) == 4
    assert find_first_occurrence([1, 2, 3, 4, 5], 6) == -1
    assert find_first_occurrence([], 1) == -1
    assert find_first_occurrence([1, 1, 1, 1, 1], 1) == 0
    assert find_first_occurrence([1, 2, 3, 4, 5], 3) == 2

def test_first_odd():
    # Test cases
    assert first_odd([1, 3, 5]) == 1
    assert first_odd([2, 4, 1, 3]) == 1
    assert first_odd([8, 9, 1]) == 9
    assert first_odd([2, 4, 6, 8]) == -1
    assert first_odd([]) == -1
    assert first_odd([0, 2, 4, 6]) == -1
    assert first_odd([7]) == 7
    assert first_odd([2, 4, 6, 7]) == 7

def test_long_words():
    assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
    assert long_words(2, "writing a program") == ['writing', 'program']
    assert long_words(5, "sorting list") == ['sorting']
    assert long_words(4, "this is a test") == []
    assert long_words(0, "every word counts") == ['every', 'word', 'counts']

def test_find_max_length_element():
    assert find_max_length_element([[1], [1, 2], [1, 2, 3]]) == [1, 2, 3]
    assert find_max_length_element([['A'], ['A', 'B'], ['A', 'B', 'C']]) == ['A', 'B', 'C']
    assert find_max_length_element([[1, 1], [1, 2, 3], [1, 5, 6, 1]]) == [1, 5, 6, 1]
    assert find_max_length_element([[1, 2, 3], [1, 2, 3], [1, 2]]) == [1, 2, 3]
    assert find_max_length_element([[1]]) == [1]

def test_max_length():
    assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
    assert max_length([[1], [5, 7], [10, 12, 14, 15]]) == (4, [10, 12, 14, 15])
    assert max_length([[5], [15, 20, 25]]) == (3, [15, 20, 25])
    assert max_length([[1, 2, 3], [4, 5], [6]]) == (3, [1, 2, 3])
    assert max_length([[1], [2], [3]]) == (1, [1])

def test_max_val():
    assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
    assert max_val(['Python', 15, 20, 25]) == 25
    assert max_val(['Python', 30, 20, 40, 50]) == 50
    assert max_val([1, 'a', 2, 'b', 3]) == 3
    assert max_val([100, 'x', 200, 'y', 50]) == 200

def test_max_length_list():
    assert max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
    assert max_length_list([[1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3], [1, 2], [1]]) == (5, [1, 2, 3, 4, 5])
    assert max_length_list([[3, 4, 5], [6, 7, 8, 9], [10, 11, 12]]) == (4, [6, 7, 8, 9])
    assert max_length_list([[1], [2], [3]]) == (1, [1])
    assert max_length_list([]) == (0, None)

def test_min_val():
    assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
    assert min_val(['Python', 15, 20, 25]) == 15
    assert min_val(['Python', 30, 20, 40, 50, 'version']) == 20
    assert min_val([100, 'text', 50, 25, 'another']) == 25
    assert min_val([42]) == 42

def test_min_k():
    assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
    assert min_k([('Sanjeev', 11), ('Angat', 5), ('Akash', 3), ('Nepin', 9)], 3) == [('Akash', 3), ('Angat', 5), ('Nepin', 9)]
    assert min_k([('tanmay', 14), ('Amer', 11), ('Ayesha', 9), ('SKD', 16)], 1) == [('Ayesha', 9)]

def test_find_min_length_sublist():
    assert find_min_length_sublist([[1], [1, 2], [1, 2, 3]]) == [1]
    assert find_min_length_sublist([[1, 1], [1, 1, 1], [1, 2, 7, 8]]) == [1, 1]
    assert find_min_length_sublist([['x'], ['x', 'y'], ['x', 'y', 'z']]) == ['x']
    assert find_min_length_sublist([[1, 2, 3], [1], [1, 2]]) == [1]
    assert find_min_length_sublist([[1, 2], [1, 2], [1]]) == [1]

def test_index_minimum():
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
    assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'
    assert index_minimum([('Alpha', 10), ('Beta', 20), ('Gamma', 5)]) == 'Gamma'
    assert index_minimum([('One', 1)]) == 'One'

def test_find_n_largest():
    assert find_n_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3) == [85, 75, 65]
    assert find_n_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 2) == [85, 75]
    assert find_n_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 5) == [85, 75, 65, 58, 35]
    assert find_n_largest([1, 2, 3, 4, 5], 0) == []
    assert find_n_largest([1, 2, 3, 4, 5], 10) == [5, 4, 3, 2, 1]
    assert find_n_largest([], 3) == []

def test_perfect_squares():
    assert perfect_squares(1, 30) == [1, 4, 9, 16, 25]
    assert perfect_squares(50, 100) == [64, 81, 100]
    assert perfect_squares(100, 200) == [100, 121, 144, 169, 196]
    assert perfect_squares(0, 0) == [0]
    assert perfect_squares(10, 15) == []

def test_find_shared_elements():
    assert set(find_shared_elements([1, 2, 3, 4], [3, 4, 5, 6])) == {3, 4}
    assert set(find_shared_elements(["apple", "banana", "cherry"], ["banana", "cherry", "date"])) == {"banana", "cherry"}
    assert set(find_shared_elements([1, 2, 2, 3], [2, 3, 3, 4])) == {2, 3}
    assert set(find_shared_elements([], [1, 2, 3])) == set()
    assert set(find_shared_elements([1, 2, 3], [])) == set()
    assert set(find_shared_elements([], [])) == set()

def test_find_hypotenuse():
    assert find_hypotenuse(3, 4) == 5.0
    assert find_hypotenuse(5, 12) == 13.0
    assert find_hypotenuse(8, 15) == 17.0
    assert find_hypotenuse(7, 24) == 25.0
    assert find_hypotenuse(1, 1) == 1.41

def test_find_tuples():
    # Test case 1
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
    # Test case 2
    assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == [(5, 25, 30)]
    # Test case 3
    assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == [(8, 16, 4)]
    # Test case 4: Empty list
    assert find_tuples([], 3) == []
    # Test case 5: No tuples match
    assert find_tuples([(1, 2, 3), (4, 5, 6)], 7) == []
    # Test case 6: All tuples match
    assert find_tuples([(6, 12), (18, 24)], 6) == [(6, 12), (18, 24)]

def test_find_words_starting_with_p():
    assert find_words_starting_with_p(["Python PHP", "Java JavaScript", "C C++"]) == ('Python', 'PHP')
    assert find_words_starting_with_p(["Python Programming", "Java Programming"]) == ('Python', 'Programming')
    assert find_words_starting_with_p(["Pqrst Pqr", "qrstuv"]) == ('Pqrst', 'Pqr')
    assert find_words_starting_with_p(["Java JavaScript", "C C++"]) == None
    assert find_words_starting_with_p([]) == None
    assert find_words_starting_with_p(["", ""]) == None

def test_find_char_long():
    assert set(find_char_long("Please move back to stream")) == set(["Please", "move", "back", "stream"])
    assert set(find_char_long("Jing Eco and Tech")) == set(["Jing", "Tech"])
    assert set(find_char_long("Jhingai wulu road Zone 3")) == set(["Jhingai", "wulu", "road", "Zone"])

def test_first_non_repeating_character():
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abc") == "a"
    assert first_non_repeating_character("ababc") == "c"
    assert first_non_repeating_character("") == None
    assert first_non_repeating_character("aabbcc") == None
    assert first_non_repeating_character("aabbccd") == "d"

def test_first_repeated_char():
    assert first_repeated_char("abcabc") == "a"
    assert first_repeated_char("abc") == None
    assert first_repeated_char("123123") == "1"
    assert first_repeated_char("") == None
    assert first_repeated_char("aabbcc") == "a"
    assert first_repeated_char("abcdef") == None

def test_add_to_shopping_list():
    assert sorted(add_to_shopping_list("banana")) == sorted(["banana"])
    assert sorted(add_to_shopping_list("apple")) == sorted(["apple"])
    assert sorted(add_to_shopping_list("apple", ["yogurt"])) == sorted(["yogurt", "apple"])

def test_flatten_to_set():
    assert flatten_to_set([(3, 4, 5), (4, 5, 7), (1, 4)]) == {1, 3, 4, 5, 7}
    assert flatten_to_set([(1, 2, 3), (4, 2, 3), (7, 8)]) == {1, 2, 3, 4, 7, 8}
    assert flatten_to_set([(7, 8, 9), (10, 11, 12), (10, 11)]) == {7, 8, 9, 10, 11, 12}
    assert flatten_to_set([]) == set()
    assert flatten_to_set([(1,), (2,), (3,)]) == {1, 2, 3}

def test_flatten_list():
    assert flatten_list([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([[10, 20], [30, [40, 50]], 60]) == [10, 20, 30, 40, 50, 60]
    assert flatten_list([]) == []
    assert flatten_list([[[1, 2], 3], 4]) == [1, 2, 3, 4]
    assert flatten_list([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]

def test_frequency_lists():
    assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
    assert frequency_lists([[1, 2], [2, 3], [3, 4]]) == {1: 1, 2: 2, 3: 2, 4: 1}
    assert frequency_lists([[1, 1, 1], [2, 2], [3]]) == {1: 3, 2: 2, 3: 1}
    assert frequency_lists([[], []]) == {}
    assert frequency_lists([[10, 20], [10, 30], [20, 30, 30]]) == {10: 2, 20: 2, 30: 3}

def test_combinations_with_repetition():
    assert combinations_with_repetition(["Red", "Green", "Blue"], 1) == [("Red",), ("Green",), ("Blue",)]
    assert combinations_with_repetition(["Red", "Green", "Blue"], 2) == [
        ("Red", "Red"), ("Red", "Green"), ("Red", "Blue"),
        ("Green", "Green"), ("Green", "Blue"), ("Blue", "Blue")
    ]
    assert combinations_with_repetition(["Red", "Green", "Blue"], 3) == [
        ("Red", "Red", "Red"), ("Red", "Red", "Green"), ("Red", "Red", "Blue"),
        ("Red", "Green", "Green"), ("Red", "Green", "Blue"), ("Red", "Blue", "Blue"),
        ("Green", "Green", "Green"), ("Green", "Green", "Blue"), ("Green", "Blue", "Blue"),
        ("Blue", "Blue", "Blue")
    ]

def test_geometric_sum():
    assert abs(geometric_sum(0) - 1.0) < 1e-6
    assert abs(geometric_sum(1) - 1.5) < 1e-6
    assert abs(geometric_sum(2) - 1.75) < 1e-6
    assert abs(geometric_sum(3) - 1.875) < 1e-6
    assert abs(geometric_sum(5) - 1.96875) < 1e-6
    assert abs(geometric_sum(7) - 1.9921875) < 1e-6

def test_group_by():
    assert group_by(lambda x: x % 2, [1, 2, 3, 4, 5, 6]) == {1: [1, 3, 5], 0: [2, 4, 6]}
    assert group_by(lambda x: len(x), ['apple', 'banana', 'cherry']) == {5: ['apple'], 6: ['banana', 'cherry']}
    assert group_by(lambda x: x.isupper(), ['Hello', 'WORLD', 'Python']) == {True: ['WORLD'], False: ['Hello', 'Python']}
    assert group_by(lambda x: x[0], ['apple', 'banana', 'cherry']) == {'a': ['apple'], 'b': ['banana'], 'c': ['cherry']}
    assert group_by(lambda x: x % 2, []) == {}

def test_harmonic_sum():
    assert math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001)
    assert math.isclose(harmonic_sum(4), 2.083333333333333, rel_tol=0.001)
    assert math.isclose(harmonic_sum(19), 3.547739657143682, rel_tol=0.001)
    assert math.isclose(harmonic_sum(1), 1.0, rel_tol=0.001)

def test_heap_sort():
    assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert heap_sort([25, 35, 22, 85, 14, 65, 75, 25, 58]) == [14, 22, 25, 25, 35, 58, 65, 75, 85]
    assert heap_sort([7, 1, 9, 5]) == [1, 5, 7, 9]
    assert heap_sort([]) == []
    assert heap_sort([42]) == [42]
    assert heap_sort([3, 3, 3]) == [3, 3, 3]

def test_highest_power_of_2():
    assert highest_power_of_2(10) == 8
    assert highest_power_of_2(19) == 16
    assert highest_power_of_2(32) == 32
    assert highest_power_of_2(1) == 1
    assert highest_power_of_2(0) == 0  # Edge case for 0
    assert highest_power_of_2(64) == 64
    assert highest_power_of_2(127) == 64

def test_is_not_prime():
    assert is_not_prime(2) == False  # 2 is a prime number
    assert is_not_prime(10) == True  # 10 is not a prime number
    assert is_not_prime(35) == True  # 35 is not a prime number
    assert is_not_prime(37) == False  # 37 is a prime number
    assert is_not_prime(1) == True  # 1 is not a prime number

def test_add_nested_tuples():
    assert add_nested_tuples(((1, 3), (4, 5)), ((6, 7), (3, 9))) == ((7, 10), (7, 14))
    assert add_nested_tuples(((2, 4), (5, 6)), ((7, 8), (4, 10))) == ((9, 12), (9, 16))
    assert add_nested_tuples(((3, 5), (6, 7)), ((8, 9), (5, 11))) == ((11, 14), (11, 18))
    assert add_nested_tuples(((1, 2, 3),), ((4, 5, 6),)) == ((5, 7, 9),)
    assert add_nested_tuples(((1,), (2,)), ((3,), (4,))) == ((4,), (6,))

def test_insert_element():
    assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert insert_element(['python', 'java'], 'program') == ['program', 'python', 'program', 'java']
    assert insert_element(['happy', 'sad'], 'laugh') == ['laugh', 'happy', 'laugh', 'sad']
    assert insert_element([], 'test') == []
    assert insert_element([1, 2, 3], 0) == [0, 1, 0, 2, 0, 3]

def test_interleave_lists():
    assert interleave_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]) == [1, 4, 7, 2, 5, 8, 3, 6, 9]
    assert interleave_lists(['a', 'b'], ['c', 'd'], ['e', 'f']) == ['a', 'c', 'e', 'b', 'd', 'f']
    assert interleave_lists([10, 20], [15, 25], [5, 10]) == [10, 15, 5, 20, 25, 10]
    assert interleave_lists([], [], []) == []
    assert interleave_lists([1], [2], [3]) == [1, 2, 3]

def test_jacobsthal_num():
    assert jacobsthal_num(0) == 0
    assert jacobsthal_num(1) == 1
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(3) == 3
    assert jacobsthal_num(4) == 5
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(6) == 21
    assert jacobsthal_num(10) == 341
    assert jacobsthal_num(13) == 2731

def test_join_integers():
    assert join_integers([11, 33, 50]) == 113350
    assert join_integers([-1, 2, 3, 4, 5, 6]) == -123456
    assert join_integers([10, 15, 20, 25]) == 10152025
    assert join_integers([0, 0, 0]) == 0
    assert join_integers([123, 456, 789]) == 123456789

def test_kth_element():
    assert kth_element([12, 3, 5, 7, 19], 2) == 5
    assert kth_element([17, 24, 8, 23], 3) == 23
    assert kth_element([16, 21, 25, 36, 4], 4) == 25
    assert kth_element([1, 2, 3, 4, 5], 1) == 1
    assert kth_element([10, 20, 30, 40, 50], 5) == 50

def test_largest_negative():
    assert largest_negative([1, 2, 3, -4, -6]) == -4
    assert largest_negative([1, 2, 3, -8, -9]) == -8
    assert largest_negative([1, 2, 3, 4, -1]) == -1
    assert largest_negative([1, 2, 3, 4]) == None
    assert largest_negative([-10, -20, -30, -5]) == -5
    assert largest_negative([-1]) == -1
    assert largest_negative([0, -1, -2, -3]) == -1

def test_find_largest_number():
    assert find_largest_number([1, 2, 3]) == 321
    assert find_largest_number([4, 5, 6, 1]) == 6541
    assert find_largest_number([1, 2, 3, 9]) == 9321
    assert find_largest_number([0, 0, 1]) == 100
    assert find_largest_number([9, 8, 7, 6, 5]) == 98765
    assert find_largest_number([5]) == 5

def test_large_product():
    assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3) == [60, 54, 50]
    assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 4) == [60, 54, 50, 48]
    assert large_product([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 5) == [60, 54, 50, 48, 45]
    assert large_product([1], [1], 1) == [1]
    assert large_product([1, 2], [3, 4], 2) == [8, 6]

def test_largest_triangle_area():
    assert largest_triangle_area(0) == 0.0
    assert largest_triangle_area(2) == 2.0
    assert largest_triangle_area(5) == 12.5
    assert largest_triangle_area(10) == 50.0
    assert largest_triangle_area(1.5) == 1.125

def test_last_digit_factorial():
    assert last_digit_factorial(0) == 1  # 0! = 1
    assert last_digit_factorial(1) == 1  # 1! = 1
    assert last_digit_factorial(2) == 2  # 2! = 2
    assert last_digit_factorial(3) == 6  # 3! = 6
    assert last_digit_factorial(4) == 4  # 4! = 24
    assert last_digit_factorial(5) == 0  # 5! = 120
    assert last_digit_factorial(10) == 0  # 10! ends with 0
    assert last_digit_factorial(20) == 0  # 20! ends with 0

def test_last_position():
    assert last_position([1, 2, 2, 2, 3], 2) == 3
    assert last_position([1, 2, 3, 4, 5], 6) == -1
    assert last_position([1, 1, 1, 1, 1], 1) == 4
    assert last_position([], 1) == -1
    assert last_position([1, 2, 3, 4, 5], 3) == 2
    assert last_position([1, 2, 2, 2, 2], 2) == 4
    assert last_position([1, 2, 3, 4, 5], 1) == 0

def test_lateral_surface_area_cone():
    assert math.isclose(lateral_surface_area_cone(5, 12), 204.20352248333654, rel_tol=1e-9)
    assert math.isclose(lateral_surface_area_cone(10, 15), 566.3586699569488, rel_tol=1e-9)
    assert math.isclose(lateral_surface_area_cone(19, 17), 1521.8090132193388, rel_tol=1e-9)

def test_lateral_surface_area_cylinder():
    assert math.isclose(lateral_surface_area_cylinder(10, 5), 314.159, rel_tol=0.001)
    assert math.isclose(lateral_surface_area_cylinder(4, 5), 125.664, rel_tol=0.001)
    assert math.isclose(lateral_surface_area_cylinder(4, 10), 251.328, rel_tol=0.001)
    assert math.isclose(lateral_surface_area_cylinder(7, 3), 131.946, rel_tol=0.001)
    assert math.isclose(lateral_surface_area_cylinder(1, 1), 6.283, rel_tol=0.001)

def test_left_insertion():
    assert left_insertion([1, 2, 4, 5], 6) == 4
    assert left_insertion([1, 2, 4, 5], 3) == 2
    assert left_insertion([1, 2, 4, 5], 7) == 4
    assert left_insertion([1, 2, 4, 5], 0) == 0
    assert left_insertion([1, 2, 4, 5], 4) == 2
    assert left_insertion([], 1) == 0
    assert left_insertion([1, 3, 3, 3, 5], 3) == 1

def test_combine_lists():
    assert combine_lists([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]) == [11, 22, 33, 44, 55]
    assert combine_lists([0, 0, 0, 0, 0], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert combine_lists([-1, -2, -3, -4, -5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]
    assert combine_lists([], []) == []

def test_find_common_elements():
    assert find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]) == [4, 5]
    assert find_common_elements([1, 2, 3], [4, 5, 6]) == []
    assert find_common_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert find_common_elements([], []) == []

def test_list_difference():
    assert sorted(list_difference([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 15, 20, 30]
    assert sorted(list_difference([1, 2, 3, 4, 5], [6, 7, 1])) == [2, 3, 4, 5, 6, 7]
    assert sorted(list_difference([1, 2, 3], [6, 7, 1])) == [2, 3, 6, 7]
    assert sorted(list_difference([], [1, 2, 3])) == [1, 2, 3]
    assert sorted(list_difference([1, 2, 3], [])) == [1, 2, 3]
    assert sorted(list_difference([], [])) == []

def test_filter_positive_numbers():
    assert filter_positive_numbers([-2, -1, 0, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert filter_positive_numbers([-1, -2, -3, -4, -5]) == []
    assert filter_positive_numbers([0, 0, 0, 0, 0]) == []
    assert filter_positive_numbers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_filter_lists():
    assert filter_lists(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_lists(lambda x: x > 0, [-2, -1, 0, 1, 2]) == [1, 2]
    assert filter_lists(lambda x: x.isupper(), ["Hello", "WORLD", "Python"]) == ["WORLD"]
    assert filter_lists(lambda x: len(x) > 3, ["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]
    assert filter_lists(lambda x: x.startswith("a"), ["apple", "banana", "cherry"]) == ["apple"]

def test_map_lists():
    assert map_lists(lambda x: x * 2, [1, 2, 3, 4]) == [2, 4, 6, 8]
    assert map_lists(lambda x: x ** 2, [1, 2, 3, 4]) == [1, 4, 9, 16]
    assert map_lists(lambda x: x + 1, [1, 2, 3, 4]) == [2, 3, 4, 5]
    assert map_lists(lambda x: x.upper(), ["hello", "world"]) == ["HELLO", "WORLD"]
    assert map_lists(lambda x: len(x), ["apple", "banana", "cherry"]) == [5, 6, 6]

def test_reduce_lists():
    assert reduce_lists(lambda x, y: x + y, [1, 2, 3, 4]) == 10
    assert reduce_lists(lambda x, y: x * y, [1, 2, 3, 4]) == 24
    assert reduce_lists(lambda x, y: x - y, [10, 5, 2]) == 3
    assert reduce_lists(lambda x, y: x + y, ["hello", " ", "world"]) == "hello world"
    assert reduce_lists(lambda x, y: x + y, ["apple", " ", "banana", " ", "cherry"]) == "apple banana cherry"

def test_sort_students():
    students = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 18},
        {"name": "Charlie", "age": 22}
    ]
    sorted_students = [
        {"name": "Bob", "age": 18},
        {"name": "Alice", "age": 20},
        {"name": "Charlie", "age": 22}
    ]
    assert sort_students(students) == sorted_students

    students = [
        {"name": "John", "age": 25},
        {"name": "Emily", "age": 19},
        {"name": "David", "age": 21}
    ]
    sorted_students = [
        {"name": "Emily", "age": 19},
        {"name": "David", "age": 21},
        {"name": "John", "age": 25}
    ]
    assert sort_students(students) == sorted_students

    students = [
        {"name": "Sarah", "age": 30},
        {"name": "Michael", "age": 27},
        {"name": "Emma", "age": 24}
    ]
    sorted_students = [
        {"name": "Emma", "age": 24},
        {"name": "Michael", "age": 27},
        {"name": "Sarah", "age": 30}
    ]
    assert sort_students(students) == sorted_students

def test_square_even_numbers():
    assert square_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 16, 36, 64, 100]
    assert square_even_numbers([2, 4, 6, 8, 10]) == [4, 16, 36, 64, 100]
    assert square_even_numbers([1, 3, 5, 7, 9]) == []
    assert square_even_numbers([]) == []

def test_find_max_length():
    assert find_max_length([[1], [1, 4], [5, 6, 7, 8]]) == 4
    assert find_max_length([[0, 1], [2, 2], [3, 2, 1]]) == 3
    assert find_max_length([[7], [22, 23], [13, 14, 15], [10, 20, 30, 40, 50]]) == 5
    assert find_max_length([]) == 0
    assert find_max_length([[1, 2, 3], [4, 5], [6]]) == 3
    assert find_max_length([[1], [2], [3], [4]]) == 1

def test_len_longest_word():
    assert len_longest_word(["python", "PHP", "bigdata"]) == 7
    assert len_longest_word(["a", "ab", "abc"]) == 3
    assert len_longest_word(["small", "big", "tall"]) == 5
    assert len_longest_word(["one", "three", "five", "seven"]) == 5
    assert len_longest_word(["short", "longer", "longest"]) == 7

def test_is_magic_square():
    # Test cases for magic square checker
    assert is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True
    assert is_magic_square([[1, 2], [3, 4]]) == False
    assert is_magic_square([[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1]]) == True
    assert is_magic_square([[1]]) == True
    assert is_magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == False
    assert is_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) == True

def test_match_a_followed_by_b():
    assert match_a_followed_by_b("ab") == True
    assert match_a_followed_by_b("a") == False
    assert match_a_followed_by_b("abb") == True
    assert match_a_followed_by_b("b") == False
    assert match_a_followed_by_b("aab") == True
    assert match_a_followed_by_b("ac") == False
    assert match_a_followed_by_b("abbbba") == True
    assert match_a_followed_by_b("dsabbbba") == True
    assert match_a_followed_by_b("asbbbba") == False
    assert match_a_followed_by_b("abaaa") == True

def test_text_match_wordz():
    assert text_match_wordz("The zebra is fast.") == True
    assert text_match_wordz("Hello world!") == False
    assert text_match_wordz("Crazy examples.") == True
    assert text_match_wordz("Zooming past.") == True
    assert text_match_wordz("No match here.") == False
    assert text_match_wordz("Zany antics.") == True
    assert text_match_wordz("Empty string") == False

def test_max_product_tuple():
    # Test cases to validate the solution
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
    assert max_product_tuple([(10, 20), (15, 2), (5, 10)]) == 200
    assert max_product_tuple([(11, 44), (10, 15), (20, 5)]) == 484
    assert max_product_tuple([(-10, -20), (15, -2), (5, 10)]) == 200
    assert max_product_tuple([(0, 0), (0, 1), (1, 0)]) == 0
    assert max_product_tuple([(1, 1)]) == 1

def test_max_aggregate():
    assert max_aggregate([('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]) == ('Juan Whelan', 212)
    assert max_aggregate([('Juan Whelan', 50), ('Sabah Colley', 48), ('Peter Nichols', 37), ('Juan Whelan', 22), ('Sabah Colley', 14)]) == ('Juan Whelan', 72)
    assert max_aggregate([('Juan Whelan', 10), ('Sabah Colley', 20), ('Peter Nichols', 30), ('Juan Whelan', 40), ('Sabah Colley', 50)]) == ('Sabah Colley', 70)
    assert max_aggregate([('Alice', 10), ('Bob', 20), ('Alice', 30), ('Bob', 40)]) == ('Bob', 60)
    assert max_aggregate([('Alice', 100)]) == ('Alice', 100)

def test_max_sub_array_sum():
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert max_sub_array_sum([1, 2, 3, -2, 5]) == 9
    assert max_sub_array_sum([-1, -2, -3, -4]) == 0
    assert max_sub_array_sum([4, -1, 2, 1]) == 6
    assert max_sub_array_sum([0, 0, 0, 0]) == 0
    assert max_sub_array_sum([-2, -3, -1, -4]) == 0

def test_find_max_difference():
    assert find_max_difference("11000010001") == 6
    assert find_max_difference("10111") == 1
    assert find_max_difference("1111") == 0
    assert find_max_difference("0000") == 4
    assert find_max_difference("101010") == 1
    assert find_max_difference("10001") == 3
    assert find_max_difference("") == 0

def test_max_difference():
    # Test cases to validate the solution
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    assert max_difference([(4, 6), (2, 17), (9, 13), (11, 12)]) == 15
    assert max_difference([(12, 35), (21, 27), (13, 23), (41, 22)]) == 23
    assert max_difference([(0, 0), (0, 0)]) == 0
    assert max_difference([(1, -1), (-2, 2), (3, -3)]) == 6

def test_max_occurrences():
    assert max_occurrences([2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]) == 2
    assert max_occurrences([10, 20, 20, 30, 40, 90, 80, 50, 30, 20, 50, 10]) == 20
    assert max_occurrences([1, 1, 2, 2, 3, 3, 3]) == 3
    assert max_occurrences([5]) == 5
    assert max_occurrences([]) == None

def test_max_of_nth():
    # Test cases
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11
    assert max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0) == 7
    assert max_of_nth([[1, 2], [3, 4], [5, 6]], 1) == 6

def test_max_product_pair():
    assert max_product_pair([1, 2, 3, 4, 7, 0, 8, 4]) == (7, 8)
    assert max_product_pair([0, -1, -2, -4, 5, 0, -6]) == (-4, -6)
    assert max_product_pair([1, 2, 3]) == (2, 3)
    assert max_product_pair([5]) == None
    assert max_product_pair([]) == None
    assert max_product_pair([-10, -20, 1, 2]) == (-10, -20)

def test_max_sum_list():
    assert max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]
    assert max_sum_list([[3, 2, 1], [6, 5, 4], [12, 11, 10]]) == [12, 11, 10]
    assert max_sum_list([[2, 3, 1]]) == [2, 3, 1]
    assert max_sum_list([[0, 0, 0], [1, 1, 1], [2, 2, 2]]) == [2, 2, 2]
    assert max_sum_list([[5], [10], [15]]) == [15]

def test_max_run_uppercase():
    assert max_run_uppercase("GeMKSForGERksISBESt") == 5
    assert max_run_uppercase("PrECIOusMOVemENTSYT") == 6
    assert max_run_uppercase("GooGLEFluTTER") == 4
    assert max_run_uppercase("abc") == 0
    assert max_run_uppercase("ABC") == 3
    assert max_run_uppercase("") == 0
    assert max_run_uppercase("aBcDeFgHiJ") == 1

def test_maximize_elements():
    assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
    assert maximize_elements(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((7, 8), (5, 10), (3, 10), (8, 11))
    assert maximize_elements(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((8, 9), (6, 11), (4, 11), (9, 12))

def test_max_abs_diff():
    assert max_abs_diff([2, 1, 5, 3]) == 4
    assert max_abs_diff([9, 3, 2, 5, 1]) == 8
    assert max_abs_diff([3, 2, 1]) == 2
    assert max_abs_diff([10, 10, 10]) == 0
    assert max_abs_diff([-10, 0, 10]) == 20

def test_merge_dictionaries_three():
    # Test case 1: No overlapping keys
    assert merge_dictionaries_three({"a": 1}, {"b": 2}, {"c": 3}) == {"a": 1, "b": 2, "c": 3}

    # Test case 2: Overlapping keys with precedence
    assert merge_dictionaries_three({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"c": 5, "d": 6}) == {"a": 1, "b": 3, "c": 5, "d": 6}

    # Test case 3: Empty dictionaries
    assert merge_dictionaries_three({}, {}, {}) == {}

    # Test case 4: One empty dictionary
    assert merge_dictionaries_three({"a": 1}, {}, {"b": 2}) == {"a": 1, "b": 2}

    # Test case 5: All dictionaries with unique keys
    assert merge_dictionaries_three({"x": "X"}, {"y": "Y"}, {"z": "Z"}) == {"x": "X", "y": "Y", "z": "Z"}

def test_merge_sorted_lists():
    assert merge_sorted_lists([3, 1, 4], [2, 5], [6, 0]) == [0, 1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([10, 20], [15, 25], [5, 30]) == [5, 10, 15, 20, 25, 30]
    assert merge_sorted_lists([], [], []) == []
    assert merge_sorted_lists([1, 2, 3], [], []) == [1, 2, 3]
    assert merge_sorted_lists([], [4, 5, 6], []) == [4, 5, 6]
    assert merge_sorted_lists([], [], [7, 8, 9]) == [7, 8, 9]
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6], [0, 7, 8]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_min_swaps():
    assert min_swaps("1101", "1110") == 1
    assert min_swaps("111", "000") == "Not Possible"
    assert min_swaps("111", "110") == "Not Possible"
    assert min_swaps("1010", "0101") == 2
    assert min_swaps("1111", "1111") == 0
    assert min_swaps("0000", "1111") == "Not Possible"

def test_find_min_diff():
    assert find_min_diff([1, 5, 3, 19, 18, 25]) == 1
    assert find_min_diff([4, 3, 2, 6]) == 1
    assert find_min_diff([30, 5, 20, 9]) == 4
    assert find_min_diff([-10, -20, -30, -40]) == 10
    assert find_min_diff([100, 300, 200, 400]) == 100

def test_min_jumps():
    assert min_jumps((3, 4), 11) == 3
    assert min_jumps((3, 4), 0) == 0
    assert min_jumps((11, 14), 11) == 1
    assert min_jumps((2, 5), 7) == 2
    assert min_jumps((1, 3), 10) == 4
    assert min_jumps((6, 8), 24) == 3
    assert min_jumps((2, 3), 5) == 2

def test_min_product_tuple():
    # Test cases
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
    assert min_product_tuple([(10, 20), (15, 2), (5, 10)]) == 30
    assert min_product_tuple([(11, 44), (10, 15), (20, 5), (12, 9)]) == 100
    assert min_product_tuple([(-2, 7), (2, -6), (-1, 8), (4, -9)]) == -36
    assert min_product_tuple([(0, 7), (2, 6), (1, 8), (4, 9)]) == 0

def test_find_rotations():
    assert find_rotations("aaaa") == 1
    assert find_rotations("ab") == 2
    assert find_rotations("abc") == 3
    assert find_rotations("a") == 1
    assert find_rotations("abab") == 2
    assert find_rotations("abcd") == 4
    assert find_rotations("aaaabaaa") == 8

def test_move_numbers_to_end():
    assert move_numbers_to_end("I1love143you55three3000thousand") == "Iloveyouthreethousand1143553000"
    assert move_numbers_to_end("Avengers124Assemble") == "AvengersAssemble124"
    assert move_numbers_to_end("Its11our12path13to14see15things16do17things") == "Itsourpathtoseethingsdothings11121314151617"
    assert move_numbers_to_end("123abc") == "abc123"
    assert move_numbers_to_end("abc123") == "abc123"
    assert move_numbers_to_end("a1b2c3") == "abc123"

def test_move_zeroes_to_end():
    assert move_zeroes_to_end([1, 0, 2, 0, 3, 4]) == [1, 2, 3, 4, 0, 0]
    assert move_zeroes_to_end([2, 3, 2, 0, 0, 4, 0, 5, 0]) == [2, 3, 2, 4, 5, 0, 0, 0, 0]
    assert move_zeroes_to_end([0, 1, 0, 1, 1]) == [1, 1, 1, 0, 0]
    assert move_zeroes_to_end([0, 0, 0]) == [0, 0, 0]
    assert move_zeroes_to_end([1, 2, 3]) == [1, 2, 3]
    assert move_zeroes_to_end([]) == []

def test_multiply_and_divide():
    assert math.isclose(multiply_and_divide([8, 2, 3, -1, 7]), -67.2, rel_tol=0.001)
    assert math.isclose(multiply_and_divide([-10, -20, -30]), -2000.0, rel_tol=0.001)
    assert math.isclose(multiply_and_divide([19, 15, 18]), 1710.0, rel_tol=0.001)
    assert math.isclose(multiply_and_divide([1]), 1.0, rel_tol=0.001)
    assert math.isclose(multiply_and_divide([0.5, 2, 4]), 1.3333, rel_tol=0.001)

def test_multiply_list_by_index():
    assert multiply_list_by_index([1, 2, 3, 4, 5]) == [0, 2, 6, 12, 20]
    assert multiply_list_by_index([0, 10, 20, 30]) == [0, 10, 40, 90]
    assert multiply_list_by_index([-1, -2, -3, -4]) == [0, -2, -6, -12]
    assert multiply_list_by_index([]) == []

def test_n_largest_items():
    assert n_largest_items([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [100, 90]
    assert n_largest_items([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5) == [100, 90, 80, 70, 60]
    assert n_largest_items([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3) == [100, 90, 80]
    assert n_largest_items([1, 2, 3, 4, 5], 3) == [5, 4, 3]
    assert n_largest_items([5, 5, 5, 5, 5], 2) == [5, 5]

def test_newman_conway():
    assert newman_conway(1) == 1
    assert newman_conway(2) == 1
    assert newman_conway(3) == 2
    assert newman_conway(4) == 2
    assert newman_conway(5) == 3
    assert newman_conway(6) == 4
    assert newman_conway(10) == 6

def test_next_perfect_square():
    assert next_perfect_square(35) == 36
    assert next_perfect_square(6) == 9
    assert next_perfect_square(9) == 16
    assert next_perfect_square(0) == 1
    assert next_perfect_square(15) == 16
    assert next_perfect_square(24) == 25

def test_next_smallest_palindrome():
    assert next_smallest_palindrome(99) == 101
    assert next_smallest_palindrome(1221) == 1331
    assert next_smallest_palindrome(120) == 121
    assert next_smallest_palindrome(1) == 2
    assert next_smallest_palindrome(808) == 818

def test_catalan_number():
    assert catalan_number(0) == 1
    assert catalan_number(1) == 1
    assert catalan_number(2) == 2
    assert catalan_number(3) == 5
    assert catalan_number(4) == 14
    assert catalan_number(5) == 42
    assert catalan_number(6) == 132
    assert catalan_number(7) == 429
    assert catalan_number(8) == 1430
    assert catalan_number(9) == 4862
    assert catalan_number(10) == 16796

def test_centered_hexagonal_number():
    assert centered_hexagonal_number(1) == 1
    assert centered_hexagonal_number(2) == 7
    assert centered_hexagonal_number(3) == 19
    assert centered_hexagonal_number(4) == 37
    assert centered_hexagonal_number(5) == 61
    assert centered_hexagonal_number(10) == 271
    assert centered_hexagonal_number(20) == 1141

def test_nth_decagonal_number():
    assert nth_decagonal_number(1) == 1
    assert nth_decagonal_number(3) == 27
    assert nth_decagonal_number(7) == 175
    assert nth_decagonal_number(10) == 370
    assert nth_decagonal_number(5) == 85

def test_hexagonal_num():
    assert hexagonal_num(1) == 1
    assert hexagonal_num(2) == 6
    assert hexagonal_num(3) == 15
    assert hexagonal_num(4) == 28
    assert hexagonal_num(5) == 45
    assert hexagonal_num(6) == 66
    assert hexagonal_num(7) == 91
    assert hexagonal_num(10) == 190

def test_find_lucas():
    assert find_lucas(0) == 2
    assert find_lucas(1) == 1
    assert find_lucas(2) == 3
    assert find_lucas(3) == 4
    assert find_lucas(4) == 7
    assert find_lucas(5) == 11
    assert find_lucas(6) == 18
    assert find_lucas(7) == 29
    assert find_lucas(8) == 47
    assert find_lucas(9) == 76

def test_nth_octagonal_number():
    assert nth_octagonal_number(1) == 1
    assert nth_octagonal_number(5) == 65
    assert nth_octagonal_number(10) == 280
    assert nth_octagonal_number(15) == 645
    assert nth_octagonal_number(20) == 1160

def test_nth_power():
    # Test cases
    assert nth_power([1, 2, 3, 4], 2) == [1, 4, 9, 16]
    assert nth_power([2, 3, 4], 3) == [8, 27, 64]
    assert nth_power([5, 10], 0) == [1, 1]
    assert nth_power([10, 20, 30], 3) == [1000, 8000, 27000]
    assert nth_power([12, 15], 5) == [248832, 759375]
    assert nth_power([], 2) == []  # Edge case: empty list
    assert nth_power([1, -2, 3], 3) == [1, -8, 27]  # Negative numbers

def test_find_star_num():
    assert find_star_num(3) == 37
    assert find_star_num(4) == 73
    assert find_star_num(5) == 121
    assert find_star_num(1) == 1
    assert find_star_num(2) == 13

def test_tetrahedral_number():
    assert tetrahedral_number(1) == 1
    assert tetrahedral_number(2) == 4
    assert tetrahedral_number(3) == 10
    assert tetrahedral_number(4) == 20
    assert tetrahedral_number(5) == 35
    assert tetrahedral_number(6) == 56
    assert tetrahedral_number(7) == 84
    assert tetrahedral_number(10) == 220

def test_pack_consecutive_duplicates():
    assert pack_consecutive_duplicates([1, 1, 2, 3, 3, 3, 4]) == [[1, 1], [2], [3, 3, 3], [4]]
    assert pack_consecutive_duplicates(['a', 'a', 'b', 'c', 'c', 'd']) == [['a', 'a'], ['b'], ['c', 'c'], ['d']]
    assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    assert pack_consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10]) == [[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    assert pack_consecutive_duplicates([]) == []
    assert pack_consecutive_duplicates([1]) == [[1]]

def test_add_pairwise():
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)
    assert add_pairwise((1,)) == ()
    assert add_pairwise(()) == ()

def test_pancake_sort():
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]
    assert pancake_sort([]) == []
    assert pancake_sort([1]) == [1]
    assert pancake_sort([2, 1]) == [1, 2]

def test_partition():
    assert partition(3, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
    assert partition(2, 3, [10, 20, 30, 40, 50, 60, 70, 80, 90]) == [[10, 20], [40, 50], [70, 80]]
    assert partition(4, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]]
    assert partition(3, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3], [5, 6, 7]]
    assert partition(5, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3, 4, 5]]

def test_extract_phone_numbers():
    # assert extract_phone_numbers("Please contact us at +1 (123) 456-7890 or email support@example.com.") == ["+1 (123) 456-7890"]
    assert extract_phone_numbers("Call us at (555) 123-4567 or (555) 987-6543.") == ["(555) 123-4567", "(555) 987-6543"]
    assert extract_phone_numbers("No phone numbers in this string.") == []
    assert extract_phone_numbers("") == []

def test_polar_to_rectangular():
    assert polar_to_rectangular(5, 0) == (5.0, 0.0)
    assert polar_to_rectangular(3, math.pi) == (-3.0, 0.0)
    assert polar_to_rectangular(2, math.pi / 2) == (0.0, 2.0)
    assert polar_to_rectangular(0, math.pi / 4) == (0.0, 0.0)
    assert polar_to_rectangular(1, math.pi / 4) == (0.71, 0.71)

def test_positive_ratio():
    assert positive_ratio([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
    assert positive_ratio([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]) == 0.69
    assert positive_ratio([2, 4, -6, -9, 11, -12, 14, -5, 17]) == 0.56
    assert positive_ratio([-1, -2, -3, -4, -5]) == 0.0
    assert positive_ratio([1, 2, 3, 4, 5]) == 1.0

def test_mul_even_odd():
    assert mul_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 4
    assert mul_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert mul_even_odd([1, 5, 7, 9, 10]) == 10
    assert mul_even_odd([2, 4, 6, 8]) == -1
    assert mul_even_odd([1, 3, 5, 7]) == -1
    assert mul_even_odd([]) == -1
    assert mul_even_odd([0, 1]) == 0
    assert mul_even_odd([2, 3]) == 6

def test_calculate_product():
    assert calculate_product([2, 3, 4, 5]) == 120
    assert calculate_product([1, 2, 3, 4, 5]) == 120
    assert calculate_product([0, 10, 20, 30]) == 0
    assert calculate_product([]) == 1

def test_re_arrange_array():
    assert re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 2, 4, 5, 6, 8, 9]
    assert re_arrange_array([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert re_arrange_array([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]
    assert re_arrange_array([1, -1, 2, -2, 3, -3], 6) == [-1, -2, -3, 1, 2, 3]
    assert re_arrange_array([0, -1, -2, 3, 4, -5], 6) == [-1, -2, -5, 0, 3, 4]

def test_multiply_int():
    assert multiply_int(10, 20) == 200
    assert multiply_int(-5, 10) == -50
    assert multiply_int(4, -8) == -32
    assert multiply_int(0, 5) == 0
    assert multiply_int(7, 0) == 0
    assert multiply_int(-3, -6) == 18
    assert multiply_int(1, 1) == 1

def test_find_literals():
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)
    assert find_literals('No match here', 'absent') == None
    assert find_literals('123-456-7890', '\\d{3}-\\d{3}-\\d{4}') == ('123-456-7890', 0, 12)

def test_area_polygon():
    assert math.isclose(area_polygon(4, 20), 400.0, rel_tol=0.001)
    assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
    assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)
    assert math.isclose(area_polygon(3, 10), 43.301, rel_tol=0.001)
    assert math.isclose(area_polygon(6, 5), 64.951, rel_tol=0.001)

def test_remove_dirty_chars():
    assert remove_dirty_chars("probasscurve", "pros") == "bacuve"
    assert remove_dirty_chars("digitalindia", "talent") == "digiidi"
    assert remove_dirty_chars("exoticmiles", "toxic") == "emles"
    assert remove_dirty_chars("hello", "world") == "he"
    assert remove_dirty_chars("abcdef", "") == "abcdef"
    assert remove_dirty_chars("", "abc") == ""

def test_consecutive_duplicates():
    assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    assert consecutive_duplicates([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10]) == [10, 15, 19, 18, 17, 26, 17, 18, 10]
    assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd']) == ['a', 'b', 'c', 'd']
    assert consecutive_duplicates(['a', 'a', 'b', 'c', 'd', 'd', 'a', 'a']) == ['a', 'b', 'c', 'd', 'a']
    assert consecutive_duplicates([]) == []
    assert consecutive_duplicates([1, 1, 1, 1, 1]) == [1]

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 1, 1]) == [1]
    assert remove_duplicates([]) == []
    assert remove_duplicates([5, 5, 5, 6, 7, 7, 8]) == [5, 6, 7, 8]

def test_remove_elements():
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]
    assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10]
    assert remove_elements([], [1, 2, 3]) == []
    assert remove_elements([1, 2, 3], []) == [1, 2, 3]
    assert remove_elements([1, 2, 3], [1, 2, 3]) == []

def test_remove_occurrences():
    assert remove_occurrences("hello", "l") == "heo"
    assert remove_occurrences("abcda", "a") == "bcd"
    assert remove_occurrences("PHP", "P") == "H"
    assert remove_occurrences("test", "z") == "test"
    assert remove_occurrences("aaaa", "a") == "aa"
    assert remove_occurrences("", "a") == ""
    assert remove_occurrences("a", "a") == ""
    assert remove_occurrences("ab", "a") == "b"

def test_remove_kth_element():
    # Test cases
    assert remove_kth_element([1, 2, 3, 4, 5], 3) == [1, 2, 4, 5]
    assert remove_kth_element([10, 20, 30], 1) == [20, 30]
    assert remove_kth_element([7, 8, 9], 5) == [7, 8, 9]
    assert remove_kth_element([], 1) == []
    assert remove_kth_element([1], 1) == []
    assert remove_kth_element([1, 2, 3], 0) == [1, 2, 3]
    assert remove_kth_element([1, 2, 3], -1) == [1, 2, 3]

def test_remove_leading_zeroes():
    assert remove_leading_zeroes("216.08.094.196") == "216.8.94.196"
    assert remove_leading_zeroes("12.01.024") == "12.1.24"
    assert remove_leading_zeroes("216.08.094.0196") == "216.8.94.196"
    assert remove_leading_zeroes("001.002.003.004") == "1.2.3.4"
    assert remove_leading_zeroes("0.0.0.0") == "0.0.0.0"

def test_remove_lowercase():
    assert remove_lowercase("PYTHon") == "PYTH"
    assert remove_lowercase("FInD") == "FID"
    assert remove_lowercase("STRinG") == "STRG"
    assert remove_lowercase("abcDEF") == "DEF"
    assert remove_lowercase("XYZ") == "XYZ"  # No lowercase letters to remove
    assert remove_lowercase("abc") == ""  # All lowercase letters removed

def test_remove_nested():
    assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
    assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)
    assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)
    assert remove_nested((3, 7, 9, (6, 8), (5, 12), 12)) == (3, 7, 9, 12)

def test_remove_parentheses():
    assert remove_parentheses("python (chrome)") == "python"
    assert remove_parentheses("string(.abc)") == "string"
    assert remove_parentheses("alpha(num)") == "alpha"
    assert remove_parentheses("test (one) two (three)") == "test two"
    assert remove_parentheses("no parentheses here") == "no parentheses here"
    assert remove_parentheses("(only)") == ""

def test_remove_length():
    assert remove_length("The person is most value tet", 3) == "person is most value"
    assert remove_length("If you told me about this ok", 4) == "If you me about ok"
    assert remove_length("Forces of darkeness is come into the play", 4) == "Forces of darkeness is the"
    assert remove_length("", 5) == ""
    assert remove_length("word", 4) == ""
    assert remove_length("word", 5) == "word"

def test_replace_specialchar():
    assert replace_specialchar("Python language, Programming language.") == "Python:language::Programming:language:"
    assert replace_specialchar("a b c,d e f") == "a:b:c:d:e:f"
    assert replace_specialchar("ram reshma,ram rahim") == "ram:reshma:ram:rahim"
    assert replace_specialchar("no_special_chars_here") == "no_special_chars_here"
    assert replace_specialchar("") == ""

def test_replace_spaces():
    assert replace_spaces("Jumanji The Jungle") == "Jumanji_The_Jungle"
    assert replace_spaces("The_Avengers") == "The Avengers"
    assert replace_spaces("Fast and Furious") == "Fast_and_Furious"
    assert replace_spaces("_Leading") == " Leading"
    assert replace_spaces("Trailing_") == "Trailing "
    assert replace_spaces("Multiple  Spaces") == "Multiple__Spaces"
    assert replace_spaces("NoChange") == "NoChange"

def test_reverse_array_upto_k():
    assert reverse_array_upto_k([1, 2, 3, 4, 5, 6], 4) == [4, 3, 2, 1, 5, 6]
    assert reverse_array_upto_k([4, 5, 6, 7], 2) == [5, 4, 6, 7]
    assert reverse_array_upto_k([9, 8, 7, 6, 5], 3) == [7, 8, 9, 6, 5]
    assert reverse_array_upto_k([1], 1) == [1]
    assert reverse_array_upto_k([1, 2], 2) == [2, 1]

def test_reverse_string_list():
    assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
    assert reverse_string_list(['john', 'amal', 'joel', 'george']) == ['nhoj', 'lama', 'leoj', 'egroeg']
    assert reverse_string_list(['jack', 'john', 'mary']) == ['kcaj', 'nhoj', 'yram']
    assert reverse_string_list([]) == []  # Test with an empty list
    assert reverse_string_list(['a', 'b', 'c']) == ['a', 'b', 'c']  # Test with single-character strings

def test_reverse_vowels():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("Python") == "Python"
    assert reverse_vowels("USA") == "ASU"
    assert reverse_vowels("aeiou") == "uoiea"
    assert reverse_vowels("") == ""
    assert reverse_vowels("bcd") == "bcd"
    assert reverse_vowels("aA") == "Aa"

def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("python programming") == "programming python"
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("one two three four") == "four three two one"
    assert reverse_words("single") == "single"

def test_rgb_to_hsv():
    assert rgb_to_hsv(255, 255, 255) == (0, 0.0, 100.0)
    assert rgb_to_hsv(255, 0, 0) == (0.0, 100.0, 100.0)
    assert rgb_to_hsv(0, 255, 0) == (120.0, 100.0, 100.0)
    assert rgb_to_hsv(0, 0, 255) == (240.0, 100.0, 100.0)
    assert rgb_to_hsv(128, 128, 128) == (0, 0.0, 50.19607843137255)
    assert rgb_to_hsv(0, 215, 0) == (120.0, 100.0, 84.31372549019608)
    assert rgb_to_hsv(10, 215, 110) == (149.26829268292684, 95.34883720930233, 84.31372549019608)

def test_right_insertion():
    assert right_insertion([1, 2, 4, 5], 6) == 4
    assert right_insertion([1, 2, 4, 5], 3) == 2
    assert right_insertion([1, 2, 4, 5], 7) == 4
    assert right_insertion([1, 2, 4, 5], 5) == 4
    assert right_insertion([], 1) == 0
    assert right_insertion([1, 1, 1, 1], 1) == 4

def test_left_rotate():
    assert left_rotate(16, 2) == 64
    assert left_rotate(10, 2) == 40
    assert left_rotate(99, 3) == 792
    assert left_rotate(0b0001, 3) == 0b1000
    assert left_rotate(0b0101, 3) == 0b101000
    assert left_rotate(0b11101, 3) == 0b11101000
    assert left_rotate(0xFFFFFFFF, 4) == 0xFFFFFFFF  # All bits set remains the same

def test_rotate_right():
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_right([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert rotate_right([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert rotate_right([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]
    assert rotate_right([], 3) == []
    assert rotate_right([1], 10) == [1]
    assert rotate_right(["a", "b", "c"], 1) == ["c", "a", "b"]

def test_second_smallest():
    assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2]) == -0.5
    assert second_smallest([2, 2]) == None
    assert second_smallest([2, 2, 2]) == None
    assert second_smallest([]) == None
    assert second_smallest([5]) == None
    assert second_smallest([3, 3, 3, 4]) == 4
    assert second_smallest([-1, -1, -2, -2, -3]) == -2

def test_sector_area():
    assert sector_area(4, 45) == 6.283185307179586
    assert sector_area(9, 45) == 31.808625617596654
    assert sector_area(9, 361) == None
    assert sector_area(0, 45) == 0
    assert sector_area(5, 0) == 0
    assert sector_area(5, 360) == math.pi * 5 ** 2

def test_shell_sort():
    assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
    assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]
    assert shell_sort([1]) == [1]
    assert shell_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_find_min_length():
    assert find_min_length([[1], [1, 2]]) == 1
    assert find_min_length([[1, 2], [1, 2, 3], [1, 2, 3, 4]]) == 2
    assert find_min_length([[3, 3, 3], [4, 4, 4, 4]]) == 3
    assert find_min_length([]) == 0
    assert find_min_length([[1, 2, 3], [1], [1, 2]]) == 1
    assert find_min_length([[1, 2, 3]]) == 3

def test_find_smallest_missing():
    assert find_smallest_missing([0, 1, 2, 3]) == 4
    assert find_smallest_missing([0, 1, 2, 6, 9]) == 3
    assert find_smallest_missing([2, 3, 5, 8, 9]) == 0
    assert find_smallest_missing([]) == 0
    assert find_smallest_missing([0]) == 1
    assert find_smallest_missing([1]) == 0
    assert find_smallest_missing([0, 1, 3, 4, 5]) == 2

def test_next_power_of_2():
    assert next_power_of_2(0) == 1
    assert next_power_of_2(1) == 1
    assert next_power_of_2(2) == 2
    assert next_power_of_2(3) == 4
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32
    assert next_power_of_2(31) == 32
    assert next_power_of_2(32) == 32
    assert next_power_of_2(33) == 64

def test_find_index():
    assert find_index(2) == 4, "Test case 1 failed"
    assert find_index(3) == 14, "Test case 2 failed"
    assert find_index(4) == 45, "Test case 3 failed"
    assert find_index(1) == 1, "Test case 4 failed"
    assert find_index(5) == 141, "Test case 5 failed"

def test_snake_to_camel():
    assert snake_to_camel('android_tv') == 'AndroidTv'
    assert snake_to_camel('google_pixel') == 'GooglePixel'
    assert snake_to_camel('apple_watch') == 'AppleWatch'
    assert snake_to_camel('python_programming') == 'PythonProgramming'
    assert snake_to_camel('unit_test') == 'UnitTest'

def test_sort_dict_by_value():
    assert sort_dict_by_value({'Math': 81, 'Physics': 83, 'Chemistry': 87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
    assert sort_dict_by_value({'A': 1, 'B': 3, 'C': 2}) == [('B', 3), ('C', 2), ('A', 1)]
    assert sort_dict_by_value({'X': 10, 'Y': 5, 'Z': 15}) == [('Z', 15), ('X', 10), ('Y', 5)]
    assert sort_dict_by_value({}) == []

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
    assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]
    assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]
    assert comb_sort([]) == []  # Test empty list
    assert comb_sort([1]) == [1]  # Test single element list
    assert comb_sort([2, 1]) == [1, 2]  # Test two elements list
    assert comb_sort([3, 3, 3]) == [3, 3, 3]  # Test identical elements
    assert comb_sort([5, -1, 0, 3, 2]) == [-1, 0, 2, 3, 5]  # Test with negative numbers

def test_sort_matrix():
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]) == [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5, 8, 9], [6, 4, 3], [2, 1, 4]]) == [[2, 1, 4], [6, 4, 3], [5, 8, 9]]
    assert sort_matrix([[0, 0, 0], [0, 0, 1], [0, 0, -1]]) == [[0, 0, -1], [0, 0, 0], [0, 0, 1]]
    assert sort_matrix([[10], [5], [15]]) == [[5], [10], [15]]

def test_sort_numeric_strings():
    assert sort_numeric_strings(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']) == [-500, -12, 0, 4, 7, 12, 45, 100, 200]
    assert sort_numeric_strings(['2', '3', '8', '4', '7', '9', '8', '2', '6', '5', '1', '6', '1', '2', '3', '4', '6', '9', '1', '2']) == [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9, 9]
    assert sort_numeric_strings(['1', '3', '5', '7', '1', '3', '13', '15', '17', '5', '7', '9', '1', '11']) == [1, 1, 1, 3, 3, 5, 5, 7, 7, 9, 11, 13, 15, 17]

def test_sort_sublists():
    assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']]) == [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    assert sort_sublists([['a', 'b'], ['d', 'c'], ['g', 'h'], ['f', 'e']]) == [['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]

def test_sort_by_second_value():
    assert sort_by_second_value([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]) == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    assert sort_by_second_value([('Telugu', 49), ('Hindi', 54), ('Social', 33)]) == [('Social', 33), ('Telugu', 49), ('Hindi', 54)]
    assert sort_by_second_value([('Physics', 96), ('Chemistry', 97), ('Biology', 45)]) == [('Biology', 45), ('Physics', 96), ('Chemistry', 97)]
    assert sort_by_second_value([]) == []
    assert sort_by_second_value([('Single', 1)]) == [('Single', 1)]

def test_split_and_rearrange():
    assert split_and_rearrange([12, 10, 5, 6, 52, 36], 2) == [5, 6, 52, 36, 12, 10]
    assert split_and_rearrange([1, 2, 3, 4], 1) == [2, 3, 4, 1]
    assert split_and_rearrange([0, 1, 2, 3, 4, 5, 6, 7], 3) == [3, 4, 5, 6, 7, 0, 1, 2]
    assert split_and_rearrange([1], 0) == [1]
    assert split_and_rearrange([1, 2], 1) == [2, 1]

def test_list_split():
    assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3) == [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
    assert list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 3) == [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12]]
    assert list_split(['python', 'java', 'C', 'C++', 'DBMS', 'SQL'], 2) == [['python', 'C', 'DBMS'], ['java', 'C++', 'SQL']]

def test_split_lists():
    assert split_lists([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert split_lists([['a', 'b'], ['c', 'd'], ['e', 'f']]) == [['a', 'c', 'e'], ['b', 'd', 'f']]
    assert split_lists([[10, 20], [30, 40], [50, 60], [70, 80]]) == [[10, 30, 50, 70], [20, 40, 60, 80]]
    assert split_lists([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6]]) == [[1.1, 3.3, 5.5], [2.2, 4.4, 6.6]]

def test_calculate_surface_area():
    # Test cases to validate the surface area calculation
    assert calculate_surface_area(3, 4) == 33
    assert calculate_surface_area(4, 5) == 56
    assert calculate_surface_area(1, 2) == 5
    assert calculate_surface_area(0, 5) == 0  # Base edge is zero
    assert calculate_surface_area(3, 0) == 9  # Slant height is zero

def test_calculate_square_root():
    assert calculate_square_root([4, 9, 16, 25]) == [2.0, 3.0, 4.0, 5.0]
    assert calculate_square_root([1, 2, 3, 4, 5]) == [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]
    assert calculate_square_root([0, 10, 20, 30]) == [0.0, 3.1622776601683795, 4.47213595499958, 5.477225575051661]
    assert calculate_square_root([]) == []

def test_sub():
    assert sub(10, 2, 3, 4) == 1
    assert sub(100, 20, 30, 40) == 10
    assert sub(5.5, 1.2, 0.8, 2.1) == 1.4
    assert sub(0) == 0
    assert sub(-10, -2, -3, -4) == -1

def test_difference():
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6
    assert difference(1) == 0
    assert difference(4) == 90

def test_digit_distance_nums():
    assert digit_distance_nums(123, 256) == 7
    assert digit_distance_nums(1, 2) == 1
    assert digit_distance_nums(23, 56) == 6
    assert digit_distance_nums(1234, 5678) == 16
    assert digit_distance_nums(0, 0) == 0
    assert digit_distance_nums(9, 0) == 9
    assert digit_distance_nums(99, 1) == 17

def test_sum_digits():
    assert sum_digits(345) == 12, "Test case 345 failed"
    assert sum_digits(12) == 3, "Test case 12 failed"
    assert sum_digits(97) == 16, "Test case 97 failed"
    assert sum_digits(0) == 0, "Test case 0 failed"
    assert sum_digits(1001) == 2, "Test case 1001 failed"

def test_sum_of_even_factors():
    assert sum_of_even_factors(18) == 26  # 2 + 6 + 18
    assert sum_of_even_factors(30) == 48  # 2 + 6 + 10 + 30
    assert sum_of_even_factors(6) == 8    # 2 + 6
    assert sum_of_even_factors(1) == 0    # No even factors
    assert sum_of_even_factors(2) == 2    # Only factor is 2

def test_even_binomial_coeff_sum():
    assert even_binomial_coeff_sum(4) == 8
    assert even_binomial_coeff_sum(6) == 32
    assert even_binomial_coeff_sum(2) == 2
    assert even_binomial_coeff_sum(1) == 1
    assert even_binomial_coeff_sum(8) == 128
    assert even_binomial_coeff_sum(10) == 512

def test_sum_even_and_even_index():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12
    assert sum_even_and_even_index([]) == 0
    assert sum_even_and_even_index([2, 3, 4, 5, 6]) == 12
    assert sum_even_and_even_index([1, 3, 5, 7, 9]) == 0

def test_sum_fourth_power_of_odds():
    assert sum_fourth_power_of_odds(1) == 1  # 1^4 = 1
    assert sum_fourth_power_of_odds(2) == 82  # 1^4 + 3^4 = 1 + 81 = 82
    assert sum_fourth_power_of_odds(3) == 707  # 1^4 + 3^4 + 5^4 = 1 + 81 + 625 = 707
    assert sum_fourth_power_of_odds(4) == 3108  # 1^4 + 3^4 + 5^4 + 7^4 = 3108
    assert sum_fourth_power_of_odds(0) == 0  # No numbers to sum

def test_sum_uppercase_names_length():
    assert sum_uppercase_names_length(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16
    assert sum_uppercase_names_length(['php', 'res', 'Python', 'abcd', 'Java', 'aaa']) == 10
    assert sum_uppercase_names_length(['abcd', 'Python', 'abba', 'aba']) == 6
    assert sum_uppercase_names_length([]) == 0
    assert sum_uppercase_names_length(['Alice', 'Bob', 'Charlie']) == 15
    assert sum_uppercase_names_length(['alice', 'bob', 'charlie']) == 0

def test_sum_non_repeated_elements():
    assert sum_non_repeated_elements([1, 2, 2, 3, 4, 4, 5]) == 9
    assert sum_non_repeated_elements([10, 20, 10, 30, 40]) == 90
    assert sum_non_repeated_elements([1, 1, 1, 1]) == 0
    assert sum_non_repeated_elements([]) == 0
    assert sum_non_repeated_elements([7, 8, 9, 10, 7, 8]) == 19

def test_sum_in_range():
    assert sum_in_range(2, 5) == 8, "Test case 1 failed"
    assert sum_in_range(5, 7) == 12, "Test case 2 failed"
    assert sum_in_range(7, 13) == 40, "Test case 3 failed"
    assert sum_in_range(1, 1) == 1, "Test case 4 failed"
    assert sum_in_range(10, 10) == 0, "Test case 5 failed"
    assert sum_in_range(1, 10) == 25, "Test case 6 failed"

def test_sum_of_common_divisors():
    assert sum_of_common_divisors(10, 15) == 6  # Common divisors: 1, 5
    assert sum_of_common_divisors(100, 150) == 93  # Common divisors: 1, 2, 5, 10, 25, 50
    assert sum_of_common_divisors(4, 6) == 3  # Common divisors: 1, 2
    assert sum_of_common_divisors(7, 13) == 1  # Common divisors: 1
    assert sum_of_common_divisors(12, 18) == 12  # Common divisors: 1, 2, 3, 6

def test_sum_of_digits():
    assert sum_of_digits([10, 2, 56]) == 14
    assert sum_of_digits([10, 20, -4, 5, -70]) == 19
    assert sum_of_digits([123, -456, 789]) == 45
    assert sum_of_digits([0, -1, 2, -3]) == 6
    assert sum_of_digits([]) == 0
    assert sum_of_digits([10, 'a', 20.5, -4]) == 5

def test_power_base_sum():
    assert power_base_sum(2, 100) == 115
    assert power_base_sum(8, 10) == 37
    assert power_base_sum(8, 15) == 62
    assert power_base_sum(3, 3) == 9
    assert power_base_sum(5, 5) == 11

def test_are_equivalent():
    assert are_equivalent(36, 57) == False
    assert are_equivalent(2, 4) == False
    assert are_equivalent(23, 47) == True
    assert are_equivalent(6, 28) == False
    assert are_equivalent(12, 18) == False

def test_sum_of_divisors():
    # Test cases to validate the solution
    assert sum_of_divisors(8) == 15  # Divisors: 1, 2, 4, 8
    assert sum_of_divisors(12) == 28 # Divisors: 1, 2, 3, 4, 6, 12
    assert sum_of_divisors(7) == 8   # Divisors: 1, 7
    assert sum_of_divisors(1) == 1   # Divisors: 1
    assert sum_of_divisors(28) == 56 # Divisors: 1, 2, 4, 7, 14, 28

def test_sum_range_list():
    assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 8, 10) == 29
    assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 5, 7) == 16
    assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 7, 10) == 38
    assert sum_range_list([1, 2, 3, 4, 5], 0, 4) == 15
    assert sum_range_list([10, 20, 30, 40, 50], 1, 3) == 90

def test_is_sum_of_powers_of_two():
    assert is_sum_of_powers_of_two(10) == True  # 10 = 2^3 + 2^1
    assert is_sum_of_powers_of_two(7) == True   # 7 = 2^2 + 2^1 + 2^0
    assert is_sum_of_powers_of_two(14) == True  # 14 = 2^3 + 2^2 + 2^1
    assert is_sum_of_powers_of_two(0) == True   # 0 is considered as no powers of 2
    assert is_sum_of_powers_of_two(-1) == False # Negative numbers cannot be represented

def test_sum_of_squares_of_even_numbers():
    assert sum_of_squares_of_even_numbers(0) == 0
    assert sum_of_squares_of_even_numbers(1) == 4
    assert sum_of_squares_of_even_numbers(2) == 20
    assert sum_of_squares_of_even_numbers(3) == 56
    assert sum_of_squares_of_even_numbers(4) == 120
    assert sum_of_squares_of_even_numbers(5) == 220

def test_sum_of_squares_of_odds():
    assert sum_of_squares_of_odds(1) == 1  # 1^2 = 1
    assert sum_of_squares_of_odds(2) == 10  # 1^2 + 3^2 = 1 + 9 = 10
    assert sum_of_squares_of_odds(3) == 35  # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert sum_of_squares_of_odds(4) == 84  # 1^2 + 3^2 + 5^2 + 7^2 = 1 + 9 + 25 + 49 = 84
    assert sum_of_squares_of_odds(5) == 165  # 1^2 + 3^2 + 5^2 + 7^2 + 9^2 = 165

def test_sum_of_xor_pairs():
    assert sum_of_xor_pairs([5, 9, 7, 6]) == 47
    assert sum_of_xor_pairs([7, 3, 5]) == 12
    assert sum_of_xor_pairs([7, 3]) == 4
    assert sum_of_xor_pairs([1, 2, 3]) == 6
    assert sum_of_xor_pairs([0, 0, 0]) == 0

def test_sum_series():
    assert sum_series(6) == 12, "Test case 1 failed"
    assert sum_series(10) == 30, "Test case 2 failed"
    assert sum_series(9) == 25, "Test case 3 failed"
    assert sum_series(0) == 0, "Test case 4 failed"
    assert sum_series(1) == 1, "Test case 5 failed"
    assert sum_series(2) == 2, "Test case 6 failed"
    assert sum_series(7) == 16, "Test case 7 failed"

def test_calculate_sum_of_squares():
    assert calculate_sum_of_squares([2, 3, 4, 5]) == 54
    assert calculate_sum_of_squares([1, 2, 3, 4, 5]) == 55
    assert calculate_sum_of_squares([0, 10, 20, 30]) == 1400
    assert calculate_sum_of_squares([]) == 0

def test_area_tetrahedron():
    assert math.isclose(area_tetrahedron(3), 15.588457268119894, rel_tol=1e-9)
    assert math.isclose(area_tetrahedron(20), 692.8203230275509, rel_tol=1e-9)
    assert math.isclose(area_tetrahedron(10), 173.20508075688772, rel_tol=1e-9)

def test_trim_tuple():
    assert trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 2) == [(2,), (9,), (2,), (2,)]
    assert trim_tuple([(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)], 1) == [(3, 2, 1), (4, 9, 2), (1, 2, 3), (8, 2, 1)]
    assert trim_tuple([(7, 8, 4, 9), (11, 8, 12, 4), (4, 1, 7, 8), (3, 6, 9, 7)], 1) == [(8, 4), (8, 12), (1, 7), (6, 9)]
    assert trim_tuple([(1, 2, 3)], 1) == [(2,)]
    assert trim_tuple([(1, 2, 3)], 2) == [()]

def test_extract_column():
    # Test case 1: Extracting the second column
    assert extract_column([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 1) == [2, 5, 8]
    # Test case 2: Extracting the first column
    assert extract_column([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 0) == [1, 4, 7]
    # Test case 3: Extracting the third column
    assert extract_column([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 2) == [3, 6, 9]
    # Test case 4: Empty list of tuples
    assert extract_column([], 0) == []
    # Test case 5: Single tuple in the list
    assert extract_column([(10, 20, 30)], 1) == [20]

def test_subtract_elements():
    assert subtract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
    assert subtract_elements((11, 2, 3), (24, 45, 16)) == (-13, -43, -13)
    assert subtract_elements((7, 18, 9), (10, 11, 12)) == (-3, 7, -3)
    assert subtract_elements((0, 0, 0), (0, 0, 0)) == (0, 0, 0)
    assert subtract_elements((1.5, 2.5, 3.5), (0.5, 1.5, 2.5)) == (1.0, 1.0, 1.0)

def test_tuple_modulo():
    assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
    assert tuple_modulo((11, 5, 6, 7), (6, 7, 8, 6)) == (5, 5, 6, 1)
    assert tuple_modulo((12, 6, 7, 8), (7, 8, 9, 7)) == (5, 6, 7, 1)
    assert tuple_modulo((15, 20, 25), (10, 15, 20)) == (5, 5, 5)
    assert tuple_modulo((0, 0, 0), (1, 1, 1)) == (0, 0, 0)
    # Test for exception when tuples are of different lengths
    try:
        tuple_modulo((1, 2), (1,))
    except ValueError as e:
        assert str(e) == "Tuples must be of the same length."

def test_count_tuple_occurrences():
    assert count_tuple_occurrences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    assert count_tuple_occurrences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)]) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
    assert count_tuple_occurrences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)]) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}
    assert count_tuple_occurrences([]) == {}
    assert count_tuple_occurrences([(1, 1), (1, 1), (1, 1)]) == {(1, 1): 3}

def test_index_multiplication():
    assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
    assert index_multiplication(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((14, 32), (20, 60), (6, 20), (16, 44))
    assert index_multiplication(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((24, 45), (30, 77), (12, 33), (27, 60))

def test_multiply_elements():
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
    assert multiply_elements((2, 4, 5, 6, 7)) == (8, 20, 30, 42)
    assert multiply_elements((12, 13, 14, 9, 15)) == (156, 182, 126, 135)
    assert multiply_elements((12,)) == ()
    assert multiply_elements((3, 3, 3)) == (9, 9)

def test_find_combinations():
    assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
    assert find_combinations([(3, 5), (7, 8), (6, 2), (7, 11)]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
    assert find_combinations([(4, 6), (8, 9), (7, 3), (8, 12)]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]

def test_tuple_to_dict():
    # Test cases
    assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert tuple_to_dict((2, 4, 6, 8)) == {2: 4, 6: 8}
    assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}
    assert tuple_to_dict((0, 1, 2, 3)) == {0: 1, 2: 3}
    assert tuple_to_dict((10, 20, 30, 40, 50, 60)) == {10: 20, 30: 40, 50: 60}

def test_tuple_to_int():
    assert tuple_to_int((1, 2, 3)) == 123
    assert tuple_to_int((4, 5, 6)) == 456
    assert tuple_to_int((5, 6, 7)) == 567
    assert tuple_to_int((0, 1, 2)) == 12
    assert tuple_to_int((9, 8, 7)) == 987

def test_union_elements():
    assert union_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)
    assert union_elements((1, 2, 3, 4), (3, 4, 5, 6)) == (1, 2, 3, 4, 5, 6)
    assert union_elements((11, 12, 13, 14), (13, 15, 16, 17)) == (11, 12, 13, 14, 15, 16, 17)
    assert union_elements((), ()) == ()
    assert union_elements((1, 2, 3), ()) == (1, 2, 3)
    assert union_elements((), (4, 5, 6)) == (4, 5, 6)

def test_find_unique_element():
    assert find_unique_element([1, 1, 2, 2, 3]) == 3
    assert find_unique_element([1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]) == 8
    assert find_unique_element([1, 2, 2, 3, 3, 4, 4]) == 1
    assert find_unique_element([10]) == 10
    assert find_unique_element([0, 0, 1]) == 1

def test_find_unique_elements():
    assert find_unique_elements([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert find_unique_elements([1, 1, 1, 1, 1]) == [1]
    assert find_unique_elements([]) == []
    assert sorted(find_unique_elements(["apple", "banana", "apple", "banana", "cherry"])) == ["apple", "banana", "cherry"]

def test_unique_product():
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
    assert unique_product([1, 2, 3, 1]) == 6
    assert unique_product([7, 8, 9, 0, 1, 1]) == 0
    assert unique_product([5, 5, 5, 5]) == 5
    assert unique_product([]) == 1

def test_find_unique_characters():
    assert sorted(find_unique_characters("hello")) == sorted("helo")
    assert sorted(find_unique_characters("mississippi")) == sorted("misp")
    assert sorted(find_unique_characters("abcde")) == sorted("abcde")
    assert find_unique_characters("") == ""

def test_count_unique_tuples():
    assert count_unique_tuples([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
    assert count_unique_tuples([(4, 15), (2, 3), (5, 4), (6, 7)]) == 4
    assert count_unique_tuples([(5, 16), (2, 3), (6, 5), (6, 9)]) == 4
    assert count_unique_tuples([]) == 0
    assert count_unique_tuples([(1, 1), (1, 1), (1, 1)]) == 1
    assert count_unique_tuples([(1, 2), (2, 1), (1, 2)]) == 1

def test_is_decimal():
    assert is_decimal("123.11") == True
    assert is_decimal("e666.86") == False
    assert is_decimal("3.124587") == False
    assert is_decimal("1.11") == True
    assert is_decimal("1.1.11") == False
    assert is_decimal("123") == True
    assert is_decimal("123.") == False
    assert is_decimal(".12") == False
    assert is_decimal("123.1") == True
    assert is_decimal("123.123") == False

def test_text_lowercase_underscore():
    assert text_lowercase_underscore("aab_cbbbc") == True
    assert text_lowercase_underscore("aab_Abbbc") == False
    assert text_lowercase_underscore("Aaab_abbbc") == False
    assert text_lowercase_underscore("abc_def_ghi") == False
    assert text_lowercase_underscore("abc_def") == True
    assert text_lowercase_underscore("abc") == False
    assert text_lowercase_underscore("abc_def_") == False

def test_count_word_frequency(tmp_path):
    file_path = tmp_path / "sample.txt"
    with open(file_path, "w") as file:
        file.write("Hello world! Hello Python Python Python")

    word_frequency = count_word_frequency(file_path)
    assert word_frequency == {"Hello": 2, "world!": 1, "Python": 3}

    # Additional test cases
    with open(file_path, "w") as file:
        file.write("Hello Hello Hello")
    word_frequency = count_word_frequency(file_path)
    assert word_frequency == {"Hello": 3}

    with open(file_path, "w") as file:
        file.write("Python python PYTHON")
    word_frequency = count_word_frequency(file_path)
    assert word_frequency == {"Python": 1, "python": 1, "PYTHON": 1}

    with open(file_path, "w") as file:
        file.write("")
    word_frequency = count_word_frequency(file_path)
    assert word_frequency == {}

def test_zero_to_nonzero_ratio():
    assert math.isclose(zero_to_nonzero_ratio([0, 1, 2, 0, 3]), 0.6666666666666666, rel_tol=1e-9)
    assert math.isclose(zero_to_nonzero_ratio([1, 2, 3]), 0.0, rel_tol=1e-9)
    assert zero_to_nonzero_ratio([0, 0, 0]) == float('inf')
    assert math.isclose(zero_to_nonzero_ratio([0, 1, 0, 1, 0, 1]), 1.0, rel_tol=1e-9)
    assert math.isclose(zero_to_nonzero_ratio([0, 0, 1, 1, 1, 1]), 0.5, rel_tol=1e-9)

def test_create_dictionary():
    assert create_dictionary(["a", "b", "c"], [1, 2, 3]) == {"a": 1, "b": 2, "c": 3}
    assert create_dictionary(["x", "y", "z"], [10, 20, 30]) == {"x": 10, "y": 20, "z": 30}
    assert create_dictionary([], []) == {}
    assert create_dictionary(["key"], [100]) == {"key": 100}

def test_myzip():
    assert myzip([1, 2, 3], ['a', 'b', 'c'], [True, False, True]) == [[1, 'a', True], [2, 'b', False], [3, 'c', True]]
    assert myzip([1, 2], ['a', 'b'], [True, False], [10, 20]) == [[1, 'a', True, 10], [2, 'b', False, 20]]
    assert myzip([1, 2, 3], []) == []
    assert myzip([], [1, 2, 3]) == []
    assert myzip([], [], []) == []

def test_zipwith():
    assert zipwith(lambda x, y: x + y, [1, 2, 3], [10, 20, 30]) == [11, 22, 33]
    assert zipwith(lambda x, y: x * y, [1, 2, 3], [10, 20, 30]) == [10, 40, 90]
    assert zipwith(lambda x, y: x - y, [10, 20, 30], [1, 2, 3]) == [9, 18, 27]
    assert zipwith(lambda x, y: x + y, [], []) == []
    assert zipwith(lambda x, y: x * y, [1, 2, 3], [4, 5, 6]) == [4, 10, 18]

def test_add():
    assert add(1, 2, 3, 4, 5) == 15
    assert add(10, 20, 30) == 60
    assert add(2.5, 3.7, 1.8) == 8.0
    assert add(0) == 0
    assert add(-1, -2, -3, -4, -5) == -15

def test_add_dict_to_tuple():
    assert add_dict_to_tuple((4, 5, 6), {"MSAM": 1, "is": 2, "best": 3}) == (4, 5, 6, {"MSAM": 1, "is": 2, "best": 3})
    assert add_dict_to_tuple((1, 2, 3), {"UTS": 2, "is": 3, "Worst": 4}) == (1, 2, 3, {"UTS": 2, "is": 3, "Worst": 4})
    assert add_dict_to_tuple((8, 9, 10), {"POS": 3, "is": 4, "Okay": 5}) == (8, 9, 10, {"POS": 3, "is": 4, "Okay": 5})

def test_capital_words_spaces():
    assert capital_words_spaces("Python") == "Python"
    assert capital_words_spaces("PythonProgrammingExamples") == "Python Programming Examples"
    assert capital_words_spaces("GetReadyToBeCodingFreak") == "Get Ready To Be Coding Freak"
    assert capital_words_spaces("HelloWorld") == "Hello World"
    assert capital_words_spaces("ThisIsATest") == "This Is A Test"

def test_get_adjacent_coordinates():
    assert sorted(get_adjacent_coordinates((3, 4))) == sorted([
        (2, 3), (2, 4), (2, 5),
        (3, 3),         (3, 5),
        (4, 3), (4, 4), (4, 5)
    ])
    assert sorted(get_adjacent_coordinates((0, 0))) == sorted([
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),         ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ])
    assert sorted(get_adjacent_coordinates((1, 1))) == sorted([
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2)
    ])

def test_angle_of_complex():
    assert math.isclose(angle_of_complex(1, 1), 0.7853981633974483, rel_tol=1e-9)
    assert math.isclose(angle_of_complex(0, 1), 1.5707963267948966, rel_tol=1e-9)
    assert math.isclose(angle_of_complex(-1, -1), -2.356194490192345, rel_tol=1e-9)
    assert math.isclose(angle_of_complex(1, 0), 0.0, rel_tol=1e-9)
    assert math.isclose(angle_of_complex(0, -1), -1.5707963267948966, rel_tol=1e-9)

def test_add_lists():
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)
    assert add_lists([], (1, 2, 3)) == (1, 2, 3)
    assert add_lists([1, 2, 3], ()) == (1, 2, 3)

def test_apply_format_to_list():
    # Test with integers
    assert apply_format_to_list([1, 2, 3], "Item: {}") == ["Item: 1", "Item: 2", "Item: 3"]
    # Test with strings
    assert apply_format_to_list(["a", "b", "c"], "Letter: {}") == ["Letter: a", "Letter: b", "Letter: c"]
    # Test with mixed types
    assert apply_format_to_list([1, "b", 3.5], "Value: {}") == ["Value: 1", "Value: b", "Value: 3.5"]
    # Test with an empty list
    assert apply_format_to_list([], "Empty: {}") == []
    # Test with a custom format string
    assert apply_format_to_list(["x", "y"], "Coord: {}") == ["Coord: x", "Coord: y"]

def test_is_armstrong_number():
    # Test cases for Armstrong numbers
    assert is_armstrong_number(153) == True  # 1^3 + 5^3 + 3^3 = 153
    assert is_armstrong_number(9474) == True # 9^4 + 4^4 + 7^4 + 4^4 = 9474
    assert is_armstrong_number(9475) == False # Not an Armstrong number
    assert is_armstrong_number(0) == True    # 0 is an Armstrong number
    assert is_armstrong_number(1) == True    # 1 is an Armstrong number
    assert is_armstrong_number(10) == False  # 1^2 + 0^2 != 10
    assert is_armstrong_number(370) == True  # 3^3 + 7^3 + 0^3 = 370

def test_intersection_array():
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [3, 5, 7, 9]) == [3, 5, 7, 9]
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [10, 20, 30, 40]) == [10]
    assert intersection_array([], [1, 2, 3]) == []
    assert intersection_array([1, 2, 3], []) == []
    assert intersection_array([], []) == []

def test_average_tuple():
    assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))) == [30.5, 34.25, 27.0, 23.25]
    assert average_tuple(((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))) == [25.5, -18.0, 3.75]
    assert average_tuple(((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40))) == [305.0, 342.5, 270.0, 232.5]

def test_babylonian_squareroot():
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=1e-6)
    assert math.isclose(babylonian_squareroot(2), 1.414213562373095, rel_tol=1e-6)
    assert math.isclose(babylonian_squareroot(9), 3.0, rel_tol=1e-6)
    assert math.isclose(babylonian_squareroot(0), 0.0, rel_tol=1e-6)
    assert math.isclose(babylonian_squareroot(1), 1.0, rel_tol=1e-6)
    assert math.isclose(babylonian_squareroot(100), 10.0, rel_tol=1e-6)

def test_bitwise_xor():
    # Test cases
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)
    assert bitwise_xor((0, 0, 0), (0, 0, 0)) == (0, 0, 0)
    assert bitwise_xor((1, 2, 3), (4, 5, 6)) == (5, 7, 5)

def test_power():
    assert power(3, 4) == 81  # 3^4 = 81
    assert power(2, 3) == 8   # 2^3 = 8
    assert power(5, 5) == 3125  # 5^5 = 3125
    assert power(0, 5) == 0   # 0^5 = 0
    assert power(7, 0) == 1   # 7^0 = 1
    assert power(0, 0) == 1   # 0^0 is conventionally 1

def test_wind_chill():
    # Test cases for the wind_chill function
    assert wind_chill(120, 35) == 40, "Test case 1 failed"
    assert wind_chill(40, 20) == 19, "Test case 2 failed"
    assert wind_chill(10, 8) == 6, "Test case 3 failed"
    assert wind_chill(0, 0) == 13, "Test case 4 failed"
    assert wind_chill(5, -5) == -7, "Test case 5 failed"

def test_contains_a_followed_by_bbs():
    assert contains_a_followed_by_bbs("ac") == False
    assert contains_a_followed_by_bbs("abb") == True
    assert contains_a_followed_by_bbs("abbbb") == False
    assert contains_a_followed_by_bbs("abbb") == True
    assert contains_a_followed_by_bbs("a") == False
    assert contains_a_followed_by_bbs("bbb") == False
    assert contains_a_followed_by_bbs("ab") == False
    assert contains_a_followed_by_bbs("abbbc") == True

def test_check_expression():
    assert check_expression("{()}[{}]") == True
    assert check_expression("{()}[{]") == False
    assert check_expression("{()}[{}][]({})") == True
    assert check_expression("[({})]") == True
    assert check_expression("[({})") == False
    assert check_expression("") == True
    assert check_expression("(((((((((())))))))))") == True
    assert check_expression("(((((((((()))))))))") == False

def test_all_bits_unset_in_range():
    assert all_bits_unset_in_range(4, 1, 2) == True, "Test case 1 failed"
    assert all_bits_unset_in_range(17, 2, 4) == True, "Test case 2 failed"
    assert all_bits_unset_in_range(39, 4, 6) == False, "Test case 3 failed"
    assert all_bits_unset_in_range(0, 1, 5) == True, "Test case 4 failed"
    assert all_bits_unset_in_range(255, 1, 8) == False, "Test case 5 failed"

def test_check_consecutive():
    assert check_consecutive([1, 2, 3, 4, 5]) == True
    assert check_consecutive([1, 2, 4, 5]) == False
    assert check_consecutive([3, 2, 1]) == True
    assert check_consecutive([1, 1, 2]) == False
    assert check_consecutive([10, 11, 12, 13]) == True
    assert check_consecutive([10, 12, 13]) == False

def test_check_value():
    # Test cases
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10) == False
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 12) == True
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 5) == False
    assert check_value({}, 1) == True  # Empty dictionary case
    assert check_value({'a': 1, 'b': 1, 'c': 1}, 1) == True
    assert check_value({'a': 1, 'b': 2, 'c': 1}, 1) == False

def test_contains_duplicates():
    assert contains_duplicates([1, 2, 3, 4, 5]) == False
    assert contains_duplicates([1, 2, 3, 4, 4]) == True
    assert contains_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5]) == True
    assert contains_duplicates([]) == False
    assert contains_duplicates([42]) == False
    assert contains_duplicates([42, 42]) == True

def test_check_equal_tuple_lengths():
    assert check_equal_tuple_lengths([(1, 2, 3), (4, 5, 6)]) == True
    assert check_equal_tuple_lengths([(1, 2), (3, 4, 5)]) == False
    assert check_equal_tuple_lengths([]) == True
    assert check_equal_tuple_lengths([(1,), (2,), (3,)]) == True
    assert check_equal_tuple_lengths([(1, 2), (3, 4), (5, 6)]) == True
    assert check_equal_tuple_lengths([(1, 2), (3, 4), (5,)]) == False

def test_has_even_divisors_count():
    assert has_even_divisors_count(10) == True  # Divisors: 1, 2, 5, 10 (4 divisors)
    assert has_even_divisors_count(100) == False  # Divisors: 1, 2, 4, 5, 10, 20, 25, 50, 100 (9 divisors)
    assert has_even_divisors_count(125) == True  # Divisors: 1, 5, 25, 125 (4 divisors)
    assert has_even_divisors_count(1) == False  # Divisors: 1 (1 divisor)
    assert has_even_divisors_count(36) == False  # Divisors: 1, 2, 3, 4, 6, 9, 12, 18, 36 (9 divisors)

def test_even_position():
    # Test cases
    assert even_position([2, 3, 4, 5]) == True  # Even indices: 2, 4 (both even)
    assert even_position([1, 2, 3, 4]) == False  # Even indices: 1, 3 (1 is odd)
    assert even_position([0, 1, 2, 3]) == True  # Even indices: 0, 2 (both even)
    assert even_position([]) == True  # Empty list, no indices to check
    assert even_position([2]) == True  # Single element at index 0, which is even
    assert even_position([1]) == False  # Single element at index 0, which is odd
    assert even_position([2, 3, 6, 7, 8]) == True  # Even indices: 2, 6, 8 (all even)
    assert even_position([2, 3, 6, 7, 9]) == False  # Even indices: 2, 6, 9 (9 is odd)

def test_check_integer():
    assert check_integer("123") == True
    assert check_integer("-456") == True
    assert check_integer("+789") == True
    assert check_integer("12.3") == False
    assert check_integer("abc") == False
    assert check_integer("") == False
    assert check_integer("  42  ") == True
    assert check_integer("+0") == True
    assert check_integer("-0") == True
    assert check_integer("--123") == False
    assert check_integer("++123") == False

def test_check_min_heap():
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False
    assert check_min_heap([10]) == True
    assert check_min_heap([1, 3, 2, 7, 6, 4, 5]) == True
    assert check_min_heap([1, 3, 2, 7, 6, 4, 0]) == False

def test_is_monotonic():
    # Test cases for monotonic arrays
    assert is_monotonic([6, 5, 4, 4]) == True
    assert is_monotonic([1, 2, 2, 3]) == True
    assert is_monotonic([1, 3, 2]) == False
    assert is_monotonic([1, 1, 1]) == True
    assert is_monotonic([]) == True  # Empty array is monotonic
    assert is_monotonic([10]) == True  # Single element array is monotonic
    assert is_monotonic([1, 2, 3, 4, 5]) == True  # Strictly increasing
    assert is_monotonic([5, 4, 3, 2, 1]) == True  # Strictly decreasing
    assert is_monotonic([1, 2, 3, 2, 1]) == False  # Not monotonic

def test_check_greater():
    assert check_greater([1, 2, 3, 4, 5], 4) == False
    assert check_greater([2, 3, 4, 5, 6], 8) == True
    assert check_greater([9, 7, 4, 8, 6, 1], 11) == True
    assert check_greater([10, 20, 30], 5) == False
    assert check_greater([], 10) == True  # Edge case: empty array

def test_find_parity():
    assert find_parity(12) == False  # binary: 1100, even number of 1s
    assert find_parity(7) == True   # binary: 0111, odd number of 1s
    assert find_parity(10) == False # binary: 1010, even number of 1s
    assert find_parity(0) == False  # binary: 0000, even number of 1s
    assert find_parity(1) == True   # binary: 0001, odd number of 1s

def test_check_number_relation():
    assert check_number_relation(73) == True  # 73 is one less than twice its reverse (37)
    assert check_number_relation(23) == False  # 23 is not one less than twice its reverse (32)
    assert check_number_relation(70) == False  # 70 is not one less than twice its reverse (7)
    assert check_number_relation(0) == False  # Edge case: 0 is not one less than twice its reverse (0)
    assert check_number_relation(1) == True  # Edge case: 1 is one less than twice its reverse (1)

def test_odd_position():
    # Test cases
    assert odd_position([2, 1, 4, 3, 6, 7, 6, 3]) == True, "Test case 1 failed"
    assert odd_position([4, 1, 2]) == True, "Test case 2 failed"
    assert odd_position([1, 2, 3]) == False, "Test case 3 failed"
    assert odd_position([]) == True, "Test case 4 failed (empty list)"
    assert odd_position([2, 2, 4, 4]) == False, "Test case 5 failed"
    assert odd_position([1, 3, 5, 7, 9]) == True, "Test case 6 failed"
    print("All test cases passed!")

def test_differ_at_one_bit():
    assert differ_at_one_bit(13, 9) == True  # Binary: 1101 vs 1001
    assert differ_at_one_bit(15, 8) == False # Binary: 1111 vs 1000
    assert differ_at_one_bit(2, 4) == False  # Binary: 0010 vs 0100
    assert differ_at_one_bit(2, 3) == True   # Binary: 0010 vs 0011
    assert differ_at_one_bit(5, 1) == True   # Binary: 0101 vs 0001
    assert differ_at_one_bit(1, 5) == True   # Binary: 0001 vs 0101

def test_opposite_signs():
    assert opposite_signs(1, -2) == True
    assert opposite_signs(3, 2) == False
    assert opposite_signs(-10, -10) == False
    assert opposite_signs(-2, 2) == True
    assert opposite_signs(0, 5) == False
    assert opposite_signs(0, -5) == False

def test_overlapping():
    # Test cases for overlapping function
    assert overlapping([1, 2, 3, 4, 5], [6, 7, 8, 9]) == False
    assert overlapping([1, 2, 3], [3, 4, 5]) == True
    assert overlapping(['a', 'b'], ['c', 'd', 'a']) == True
    assert overlapping([], [1, 2, 3]) == False
    assert overlapping([1, 2, 3], []) == False
    assert overlapping([], []) == False
    assert overlapping([1, 2, 3], [4, 5, 6]) == False
    assert overlapping([1, 2, 3], [3, 2, 1]) == True

def test_is_samepatterns():
    assert is_samepatterns(["red", "green", "green"], ["a", "b", "b"]) == True
    assert is_samepatterns(["red", "green", "blue"], ["a", "b", "b"]) == False
    assert is_samepatterns(["red", "green"], ["a", "b", "b"]) == False
    assert is_samepatterns(["red", "red", "red"], ["a", "a", "a"]) == True
    assert is_samepatterns(["red", "green", "red"], ["a", "b", "a"]) == True
    assert is_samepatterns(["red", "green", "red"], ["a", "b", "b"]) == False

def test_is_perfect_square():
    assert is_perfect_square(16) == True
    assert is_perfect_square(14) == False
    assert is_perfect_square(1) == True
    assert is_perfect_square(0) == True
    assert is_perfect_square(25) == True
    assert is_perfect_square(26) == False
    assert is_perfect_square(100) == True
    assert is_perfect_square(101) == False

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(13) == True
    assert is_prime(1) == False
    assert is_prime(-5) == False
    assert is_prime(29) == True
    assert is_prime(30) == False

def test_is_product_even():
    # Test cases for the function
    assert is_product_even([1, 2, 3]) == True  # Contains an even number
    assert is_product_even([1, 1, 1]) == False  # All numbers are odd
    assert is_product_even([2, 4, 6]) == True  # All numbers are even
    assert is_product_even([]) == False  # Empty list
    assert is_product_even([1, 3, 5, 7]) == False  # All numbers are odd
    assert is_product_even([1, 3, 5, 8]) == True  # Contains an even number

def test_check_char():
    assert check_char("abba") == "Valid"
    assert check_char("a") == "Valid"
    assert check_char("abcd") == "Invalid"
    assert check_char("xyzx") == "Valid"
    assert check_char("xyzy") == "Invalid"

def test_check_str():
    # Test cases for strings starting with vowels
    assert check_str("annie") == True
    assert check_str("Else") == True
    assert check_str("umbrella") == True
    # Test cases for strings not starting with vowels
    assert check_str("dawood") == False
    assert check_str("Python") == False
    assert check_str("123abc") == False
    # Edge cases
    assert check_str("") == False  # Empty string
    assert check_str("A") == True  # Single character vowel
    assert check_str("b") == False  # Single character non-vowel

def test_is_sublist():
    assert is_sublist([1, 2, 3, 4], [2, 3]) == True
    assert is_sublist([1, 2, 3, 4], [3, 2]) == False
    assert is_sublist([1, 2, 3, 4], [5]) == False
    assert is_sublist([1, 2, 3, 4], []) == True
    assert is_sublist([], [1]) == False
    assert is_sublist([1, 2, 3], [1, 2, 3]) == True
    assert is_sublist([1, 2, 3], [2, 3, 4]) == False

def test_find_substring():
    assert find_substring(["red", "black", "white", "green", "orange"], "ack") == True
    assert find_substring(["red", "black", "white", "green", "orange"], "abc") == False
    assert find_substring(["red", "black", "white", "green", "orange"], "ange") == True
    assert find_substring([], "test") == False
    assert find_substring(["hello", "world"], "") == True  # Empty substring is always found

def test_check_smaller():
    # Test cases to validate the solution
    assert check_smaller((1, 2, 3), (0, 1, 2)) == True, "Test case 1 failed"
    assert check_smaller((4, 5, 6), (4, 5, 6)) == False, "Test case 2 failed"
    assert check_smaller((10, 20, 30), (5, 15, 25)) == True, "Test case 3 failed"
    assert check_smaller((7, 8, 9), (7, 7, 7)) == False, "Test case 4 failed"
    assert check_smaller((100, 200, 300), (99, 199, 299)) == True, "Test case 5 failed"

def test_check_type():
    # Test cases
    assert check_type((5, 6, 7, 3, 5, 6)) == True, "Test case 1 failed"
    assert check_type((1, 2, "4")) == False, "Test case 2 failed"
    assert check_type((3, 2, 1, 4, 5)) == True, "Test case 3 failed"
    assert check_type(()) == True, "Test case 4 failed (empty tuple)"
    assert check_type(("a", "b", "c")) == True, "Test case 5 failed"
    assert check_type((1, 2.0, 3)) == False, "Test case 6 failed"

def test_is_undulating():
    assert is_undulating(1212121) == True, "Test case 1212121 failed"
    assert is_undulating(1991) == False, "Test case 1991 failed"
    assert is_undulating(121) == True, "Test case 121 failed"
    assert is_undulating(1) == False, "Test case 1 failed"
    assert is_undulating(123123) == False, "Test case 123123 failed"
    assert is_undulating(101010) == True, "Test case 101010 failed"
    assert is_undulating(2020202) == True, "Test case 2020202 failed"
    assert is_undulating(333) == False, "Test case 333 failed"

def test_is_woodall():
    assert is_woodall(7) == True  # 7 = 1 * 2^3 - 1
    assert is_woodall(23) == True  # 23 = 3 * 2^3 - 1
    assert is_woodall(10) == False  # 10 is not a Woodall number
    assert is_woodall(1) == True  # 1 = 1 * 2^1 - 1
    assert is_woodall(63) == True  # 63 = 3 * 2^4 - 1
    assert is_woodall(100) == False  # 100 is not a Woodall number

def test_common_element():
    assert common_element([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]) == True
    assert common_element([1, 2, 3, 4, 5], [6, 7, 8, 9]) == False
    assert common_element(['a', 'b', 'c'], ['d', 'b', 'e']) == True
    assert common_element([], [1, 2, 3]) == False
    assert common_element([1, 2, 3], []) == False
    assert common_element([], []) == False
    assert common_element([1, 2, 3], [3, 4, 5]) == True

def test_common_in_nested_lists():
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])) == {12, 18}
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]])) == {5, 23}
    assert set(common_in_nested_lists([[2, 3, 4, 1], [4, 5], [6, 4, 8], [4, 5], [6, 8, 4]])) == {4}
    assert common_in_nested_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == []
    assert common_in_nested_lists([]) == []
    assert common_in_nested_lists([[1, 2, 3]]) == [1, 2, 3]

def test_concatenate_tuple():
    assert concatenate_tuple(("ID", "is", 4, "UTS")) == 'ID-is-4-UTS'
    assert concatenate_tuple(("QWE", "is", 4, "RTY")) == 'QWE-is-4-RTY'
    assert concatenate_tuple(("ZEN", "is", 4, "OP")) == 'ZEN-is-4-OP'
    assert concatenate_tuple(("A", "B", "C")) == 'A-B-C'
    assert concatenate_tuple((1, 2, 3)) == '1-2-3'

def test_volume_of_cone():
    assert math.isclose(volume_of_cone(5, 12), 314.1592653589793, rel_tol=1e-9)
    assert math.isclose(volume_of_cone(10, 15), 1570.7963267948965, rel_tol=1e-9)
    assert math.isclose(volume_of_cone(19, 17), 6426.651371693521, rel_tol=1e-9)

def test_pair_wise():
    assert pair_wise([1, 1, 2, 3, 3, 4, 4, 5]) == [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
    assert pair_wise([1, 5, 7, 9, 10]) == [(1, 5), (5, 7), (7, 9), (9, 10)]
    assert pair_wise([5, 1, 9, 7, 10]) == [(5, 1), (1, 9), (9, 7), (7, 10)]
    assert pair_wise([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
    assert pair_wise([]) == []
    assert pair_wise([42]) == []

def test_convert_to_polar():
    assert convert_to_polar(1 + 1j) == (1.4142135623730951, 0.7853981633974483)
    assert convert_to_polar(-1 - 1j) == (1.4142135623730951, -2.356194490192345)
    assert convert_to_polar(0 + 0j) == (0.0, 0.0)
    assert convert_to_polar(1 + 0j) == (1.0, 0.0)
    assert convert_to_polar(0 + 1j) == (1.0, 1.5707963267948966)

def test_change_date_format():
    assert change_date_format("2026-01-02") == "02-01-2026"
    assert change_date_format("2020-11-13") == "13-11-2020"
    assert change_date_format("2021-04-26") == "26-04-2021"
    assert change_date_format("1999-12-31") == "31-12-1999"
    assert change_date_format("2000-01-01") == "01-01-2000"

def test_convert_to_floats():
    assert convert_to_floats([["3", "4.5", "hello"], ["1.2", "world", "7"]]) == [[3.0, 4.5, "hello"], [1.2, "world", 7.0]]
    assert convert_to_floats([["10", "20.5"], ["abc", "30"]]) == [[10.0, 20.5], ["abc", 30.0]]
    assert convert_to_floats([["0", "-1.1", "test"], ["5.5", "6"]]) == [[0.0, -1.1, "test"], [5.5, 6.0]]
    assert convert_to_floats([[]]) == [[]]
    assert convert_to_floats([["not", "convertible"]]) == [["not", "convertible"]]

def test_convert_list_dictionary():
    assert convert_list_dictionary(["S001", "S002", "S003", "S004"],
                                    ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],
                                    [85, 98, 89, 92]) == [
        {'S001': {'Adina Park': 85}},
        {'S002': {'Leyton Marsh': 98}},
        {'S003': {'Duncan Boyle': 89}},
        {'S004': {'Saim Richards': 92}}
    ]

    assert convert_list_dictionary(["abc", "def", "ghi", "jkl"],
                                    ["python", "program", "language", "programs"],
                                    [100, 200, 300, 400]) == [
        {'abc': {'python': 100}},
        {'def': {'program': 200}},
        {'ghi': {'language': 300}},
        {'jkl': {'programs': 400}}
    ]

    assert convert_list_dictionary(["A1", "A2", "A3", "A4"],
                                    ["java", "C", "C++", "DBMS"],
                                    [10, 20, 30, 40]) == [
        {'A1': {'java': 10}},
        {'A2': {'C': 20}},
        {'A3': {'C++': 30}},
        {'A4': {'DBMS': 40}}
    ]

def test_tuple_str_to_int():
    assert tuple_str_to_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_to_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_to_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_to_int("(7, 81, 19)") == (7, 81, 19)

def test_count_inversions():
    assert count_inversions([1, 20, 6, 4, 5]) == 5
    assert count_inversions([1, 2, 1]) == 1
    assert count_inversions([1, 2, 5, 6, 1]) == 3
    assert count_inversions([]) == 0
    assert count_inversions([1]) == 0
    assert count_inversions([1, 2, 3, 4, 5]) == 0
    assert count_inversions([5, 4, 3, 2, 1]) == 10

def test_is_sorted():
    assert is_sorted([1, 2, 3]) == True
    assert is_sorted([3, 2, 1]) == False
    assert is_sorted([]) == True

def test_count_rotations():
    assert count_rotations([3, 2, 1]) == 1
    assert count_rotations([4, 5, 1, 2, 3]) == 2
    assert count_rotations([7, 8, 9, 1, 2, 3]) == 3
    assert count_rotations([1, 2, 3]) == 0
    assert count_rotations([1, 3, 2]) == 2

def test_count_char_position():
    assert count_char_position("xbcefg") == 2
    assert count_char_position("ABcED") == 3
    assert count_char_position("AbgdeF") == 5
    assert count_char_position("a") == 1
    assert count_char_position("z") == 0
    assert count_char_position("abcdefghijklmnopqrstuvwxyz") == 26
    assert count_char_position("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
    assert count_char_position("") == 0

def test_count_vowel_neighbors():
    assert count_vowel_neighbors("bestinstareels") == 7
    assert count_vowel_neighbors("amazonprime") == 5
    assert count_vowel_neighbors("partofthejourneyistheend") == 12
    assert count_vowel_neighbors("a") == 0
    assert count_vowel_neighbors("aeiou") == 0
    assert count_vowel_neighbors("b") == 0
    assert count_vowel_neighbors("bca") == 1
    assert count_vowel_neighbors("abc") == 1

def test_count_divisors():
    assert count_divisors(15) == 4  # Divisors: 1, 3, 5, 15
    assert count_divisors(12) == 6  # Divisors: 1, 2, 3, 4, 6, 12
    assert count_divisors(9) == 3   # Divisors: 1, 3, 9
    assert count_divisors(1) == 1   # Divisors: 1
    assert count_divisors(7) == 2   # Divisors: 1, 7

def test_count_element_frequency():
    assert count_element_frequency([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == {1: 1, 2: 2, 3: 3, 4: 4}
    assert count_element_frequency([1, 1, 1, 1, 1]) == {1: 5}
    assert count_element_frequency([]) == {}
    assert count_element_frequency(["apple", "banana", "apple", "banana", "cherry"]) == {"apple": 2, "banana": 2, "cherry": 1}

def test_count_first_elements():
    assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
    assert count_first_elements((2, 9, (5, 7), 11)) == 2
    assert count_first_elements((11, 15, 5, 8, (2, 3), 8)) == 4
    assert count_first_elements((1, 2, 3, 4)) == 4
    assert count_first_elements(()) == 0
    assert count_first_elements(((1, 2), 3, 4)) == 0

def test_count_occurrences():
    assert count_occurrences(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3
    assert count_occurrences((1, 2, 3, 1, 4, 6, 7, 1, 4), [1, 4, 7]) == 6
    assert count_occurrences((1, 2, 3, 4, 5, 6), [1, 2]) == 2
    assert count_occurrences((), [1, 2]) == 0
    assert count_occurrences((1, 2, 3), []) == 0

def test_count_samepair():
    assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]) == 3
    assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 8], [2, 1, 3, 1, 2, 6, 7, 8]) == 4
    assert count_samepair([1, 2, 3, 4, 2, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 8], [2, 1, 3, 1, 2, 6, 7, 8]) == 5
    assert count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]) == 3
    assert count_samepair([1, 2, 3], [4, 5, 6], [7, 8, 9]) == 0

def test_count_list_occurrences():
    assert count_list_occurrences([[1, 2], [3, 4], [1, 2], [5, 6]]) == {(1, 2): 2, (3, 4): 1, (5, 6): 1}
    assert count_list_occurrences([['a', 'b'], ['c'], ['a', 'b'], ['a', 'b']]) == {('a', 'b'): 3, ('c',): 1}
    assert count_list_occurrences([[1, 2], [3, 4], [4, 5], [6, 7]]) == {(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}
    assert count_list_occurrences([]) == {}
    assert count_list_occurrences([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == {(1, 2, 3): 3}

def test_count_lists_in_tuple():
    # Test cases
    assert count_lists_in_tuple(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
    assert count_lists_in_tuple(([1, 2], [3, 4], [5, 6])) == 3
    assert count_lists_in_tuple(([9, 8, 7, 6, 5, 4, 3, 2, 1],)) == 1
    assert count_lists_in_tuple((1, 2, 3, 4, 5)) == 0
    assert count_lists_in_tuple(([], [1], [2, 3], "string", 42)) == 3

def test_count_same_pair():
    assert count_same_pair([1, 2, 3, 4], [1, 2, 0, 4]) == 3
    assert count_same_pair([5, 6, 7], [5, 0, 7]) == 2
    assert count_same_pair([1, 2, 3], [4, 5, 6]) == 0
    assert count_same_pair([0, 1, 1, 2], [0, 1, 2, 2]) == 3
    assert count_same_pair([], []) == 0

def test_number_of_substrings():
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("a") == 1
    assert number_of_substrings("ab") == 3
    assert number_of_substrings("") == 0  # Edge case: empty string
    assert number_of_substrings("aaaa") == 10  # All characters the same

def test_count_odd_binary_rotations():
    assert count_odd_binary_rotations("1011", 4) == 3
    assert count_odd_binary_rotations("1100", 4) == 2
    assert count_odd_binary_rotations("0000", 4) == 0
    assert count_odd_binary_rotations("1111", 4) == 4
    assert count_odd_binary_rotations("1001", 4) == 2

def test_count_odd_xor_pairs():
    assert count_odd_xor_pairs([5, 4, 7, 2, 1]) == 6
    assert count_odd_xor_pairs([7, 2, 8, 1, 0, 5, 11]) == 12
    assert count_odd_xor_pairs([1, 2, 3]) == 2
    assert count_odd_xor_pairs([]) == 0
    assert count_odd_xor_pairs([1]) == 0
    assert count_odd_xor_pairs([2]) == 0
    assert count_odd_xor_pairs([1, 3, 5]) == 0
    assert count_odd_xor_pairs([2, 4, 6]) == 0

def test_get_pairs_count():
    assert get_pairs_count([1, 1, 1, 1], 2) == 6
    assert get_pairs_count([1, 5, 7, -1, 5], 6) == 3
    assert get_pairs_count([1, -2, 3], 1) == 1
    assert get_pairs_count([-1, -2, 3], -3) == 1
    assert get_pairs_count([], 5) == 0
    assert get_pairs_count([1, 2, 3, 4, 5], 10) == 0

def test_count_primes():
    assert count_primes(5) == 2  # Primes are 2, 3
    assert count_primes(10) == 4  # Primes are 2, 3, 5, 7
    assert count_primes(0) == 0  # No primes less than 0
    assert count_primes(1) == 0  # No primes less than 1
    assert count_primes(2) == 0  # No primes less than 2
    assert count_primes(20) == 8  # Primes are 2, 3, 5, 7, 11, 13, 17, 19
    assert count_primes(100) == 25  # 25 primes less than 100

def test_count_set_bits():
    assert count_set_bits(2) == 1  # Binary: 10
    assert count_set_bits(4) == 1  # Binary: 100
    assert count_set_bits(6) == 2  # Binary: 110
    assert count_set_bits(0) == 0  # Binary: 0
    assert count_set_bits(15) == 4  # Binary: 1111
    assert count_set_bits(31) == 5  # Binary: 11111

def test_count_element_in_list():
    # Test cases
    assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'A') == 3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'E') == 1
    assert count_element_in_list([], 'A') == 0
    assert count_element_in_list([[], [], []], 'A') == 0
    assert count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10) == 0
    assert count_element_in_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == 1

def test_count_unequal_pairs():
    assert count_unequal_pairs([1, 2, 1]) == 2
    assert count_unequal_pairs([1, 1, 1, 1]) == 0
    assert count_unequal_pairs([1, 2, 3, 4, 5]) == 10
    assert count_unequal_pairs([1, 2, 3, 1, 2]) == 8
    assert count_unequal_pairs([1, 2]) == 1

def test_find_even_pair():
    assert find_even_pair([5, 4, 7, 2, 1]) == 4
    assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
    assert find_even_pair([1, 2, 3]) == 1
    assert find_even_pair([2, 4, 6, 8]) == 6
    assert find_even_pair([1, 3, 5, 7]) == 6
    assert find_even_pair([0, 0, 0]) == 3

def test_cube_sum_of_evens():
    assert cube_sum_of_evens(2) == 72
    assert cube_sum_of_evens(3) == 288
    assert cube_sum_of_evens(4) == 800
    assert cube_sum_of_evens(1) == 8
    assert cube_sum_of_evens(0) == 0

def test_cumulative_sum():
    assert cumulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert cumulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert cumulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44
    assert cumulative_sum([]) == 0
    assert cumulative_sum([(0,), (0, 0), (0, 0, 0)]) == 0

def test_surface_area_cylinder():
    # Test cases for the surface_area_cylinder function
    assert abs(surface_area_cylinder(10, 5) - 942.4777960769379) < 1e-6
    assert abs(surface_area_cylinder(4, 5) - 226.1946710584651) < 1e-6
    assert abs(surface_area_cylinder(4, 10) - 351.8583772020568) < 1e-6
    assert abs(surface_area_cylinder(0, 10) - 0) < 1e-6
    assert abs(surface_area_cylinder(5, 0) - 157.07963267948966) < 1e-6

def test_filter_even_values():
    assert filter_even_values({"a": 2, "b": 3, "c": 4, "d": 5}) == {"a": 2, "c": 4}
    assert filter_even_values({"x": 0, "y": 1, "z": 2}) == {"x": 0, "z": 2}
    assert filter_even_values({}) == {}
    assert filter_even_values({"p": 5, "q": 6, "r": 7}) == {"q": 6}

def test_square_dict_values():
    assert square_dict_values({"a": 2, "b": 3, "c": 4}) == {"a": 4, "b": 9, "c": 16}
    assert square_dict_values({"x": 0, "y": 1, "z": 2}) == {"x": 0, "y": 1, "z": 4}
    assert square_dict_values({}) == {}
    assert square_dict_values({"p": 5, "q": 6, "r": 7}) == {"p": 25, "q": 36, "r": 49}

def test_dict_depth():
    assert dict_depth({'a': 1, 'b': {'c': {'d': {}}}}) == 4
    assert dict_depth({'a': 1, 'b': {'c': 'python'}}) == 2
    assert dict_depth({1: 'Sun', 2: {3: {4: 'Mon'}}}) == 3
    assert dict_depth({}) == 1
    assert dict_depth({'key': {}}) == 2

def test_diff_even_odd():
    assert diff_even_odd([1, 3, 5, 7, 4, 1, 6, 8]) == 3
    assert diff_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert diff_even_odd([1, 5, 7, 9, 10]) == 9
    assert diff_even_odd([2, 4, 6, 8]) == None
    assert diff_even_odd([1, 3, 5, 7]) == None
    assert diff_even_odd([10, 15, 20]) == -5
    assert diff_even_odd([15, 10, 20]) == -5
    assert diff_even_odd([10]) == None
    assert diff_even_odd([15]) == None

def test_isOdd():
    assert isOdd(1) == True
    assert isOdd(2) == False
def test_isEven():
    assert isEven(1) == False
    assert isEven(2) == True

def test_can_be_difference_of_squares():
    assert can_be_difference_of_squares(5) == True  # 5 = 3^2 - 2^2
    assert can_be_difference_of_squares(10) == False  # 10 cannot be expressed as such
    assert can_be_difference_of_squares(15) == True  # 15 = 8^2 - 7^2
    assert can_be_difference_of_squares(2) == False  # 2 cannot be expressed as such
    assert can_be_difference_of_squares(0) == True  # 0 = 1^2 - 1^2
    assert can_be_difference_of_squares(-1) == True  # -1 = 0^2 - 1^2

def test_validate():
    assert validate(1234) == True  # No digit appears more times than its value
    assert validate(51241) == False  # Digit '1' appears twice, which is more than its value
    assert validate(321) == True  # All digits satisfy the condition
    assert validate(-1234) == True  # Negative numbers should be treated the same as positive
    assert validate(0) == True  # Single digit 0 satisfies the condition
    assert validate(111) == False  # Digit '1' appears three times, which is more than its value

def test_divisible_by_digits():
    # Test cases
    assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1, 15) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20, 25) == [22, 24]
    assert divisible_by_digits(10, 10) == []
    assert divisible_by_digits(100, 105) == []

def test_freq_count():
    assert freq_count([10, 10, 20, 20, 20, 30]) == {10: 2, 20: 3, 30: 1}
    assert freq_count(['a', 'b', 'a', 'c', 'b', 'a']) == {'a': 3, 'b': 2, 'c': 1}
    assert freq_count([]) == {}
    assert freq_count([1, 2, 3, 1, 2, 1]) == {1: 3, 2: 2, 3: 1}
    assert freq_count(['x', 'y', 'z', 'x', 'x', 'y']) == {'x': 3, 'y': 2, 'z': 1}

def test_element_search():
    # Test cases for element_search
    assert element_search([1, 2, 3, 4, 5], 3) == (True, 2)
    assert element_search([1, 2, 3, 4, 5], 6) == (False, -1)
    assert element_search([], 1) == (False, -1)
    assert element_search(['a', 'b', 'c'], 'b') == (True, 1)
    assert element_search(['a', 'b', 'c'], 'd') == (False, -1)

def test_div_list():
    assert div_list([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]
    assert div_list([3, 2], [1, 4]) == [3.0, 0.5]
    assert div_list([90, 120], [50, 70]) == [1.8, 1.7142857142857142]

    with pytest.raises(ValueError):
        div_list([1, 2, 3], [4, 5])

    with pytest.raises(ZeroDivisionError):
        div_list([1, 2, 3], [0, 1, 2])

def test_division_elements():
    assert division_elements((10, 4, 6, 9), (5, 2, 3, 3)) == (2, 2, 2, 3)
    assert division_elements((12, 6, 8, 16), (6, 3, 4, 4)) == (2, 2, 2, 4)
    assert division_elements((20, 14, 36, 18), (5, 7, 6, 9)) == (4, 2, 6, 2)

def test_and_tuples():
    # Test cases to validate the solution
    assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    assert and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
    assert and_tuples((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)
    assert and_tuples((0, 0, 0), (1, 2, 3)) == (0, 0, 0)
    assert and_tuples((255, 255, 255), (1, 2, 4)) == (1, 2, 4)

def test_sub_list():
    # Test cases for the sub_list function
    assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert sub_list([10, 20, 30], [5, 15, 25]) == [5, 5, 5]
    assert sub_list([100, 200], [50, 100]) == [50, 100]
    assert sub_list([], []) == []  # Test with empty lists
    assert sub_list([0, 0, 0], [0, 0, 0]) == [0, 0, 0]  # Test with zeros