from imports import *
from pyFiddleAdvanced import *
import pytest

def test_bell_number():
    assert bell_number(0) == 1  # Base case
    assert bell_number(1) == 1  # Single element set
    assert bell_number(2) == 2  # Two elements
    assert bell_number(3) == 5  # Three elements
    assert bell_number(4) == 15  # Four elements
    assert bell_number(5) == 52  # Five elements
    assert bell_number(6) == 203  # Six elements

def test_is_majority():
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 3) == True
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 4) == False
    assert is_majority([1, 1, 1, 2, 2], 1) == True
    assert is_majority([1, 1, 2, 2], 1) == False
    assert is_majority([1, 1, 1, 1, 2, 2, 2], 1) == True
    assert is_majority([1, 1, 1, 1, 2, 2, 2], 2) == False

def test_compose():
    double = lambda x: x * 2
    negate = lambda x: -x
    composed = compose(double, negate)
    assert composed(5) == -10
    assert composed(10) == -20
    assert composed(-3) == 6
    assert composed(0) == 0

def test_count_balanced_binary_sequences():
    assert math.isclose(count_balanced_binary_sequences(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_balanced_binary_sequences(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_balanced_binary_sequences(3), 20.0, rel_tol=0.001)
    assert math.isclose(count_balanced_binary_sequences(4), 70.0, rel_tol=0.001)

def test_read_csv_file(tmp_path):
    file_path = tmp_path / "data.csv"
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
        writer.writeheader()
        writer.writerow({"Name": "John", "Age": "25", "City": "New York"})
        writer.writerow({"Name": "Emma", "Age": "30", "City": "London"})

    data = read_csv_file(file_path, ["Name", "Age", "City"])
    assert data == [{"Name": "John", "Age": "25", "City": "New York"}, {"Name": "Emma", "Age": "30", "City": "London"}]

def test_eulerian_num():
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26
    assert eulerian_num(0, 0) == 0
    assert eulerian_num(1, 0) == 1
    assert eulerian_num(2, 1) == 1

def test_extract_email_addresses():
    assert extract_email_addresses("Contact us at info@example.com or support@example.com for assistance.") == ["info@example.com", "support@example.com"]
    assert extract_email_addresses("Please send your feedback to feedback@example.com") == ["feedback@example.com"]
    assert extract_email_addresses("No email addresses in this string.") == []
    assert extract_email_addresses("") == []

def test_count_no_of_ways():
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228
    assert count_no_of_ways(1, 5) == 5
    assert count_no_of_ways(5, 3) == 180

def test_find_common_elements():
    assert find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [3, 4, 5, 9, 10]) == [4, 5]
    assert find_common_elements([1, 2, 3], [4, 5, 6], [7, 8, 9]) == []
    assert find_common_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert find_common_elements([], [], []) == []

def test_find_element():
    assert find_element([1, 2, 3, 4, 5], [(0, 2), (0, 3)], 2, 1) == 3
    assert find_element([1, 2, 3, 4], [(0, 1), (0, 2)], 1, 2) == 3
    assert find_element([1, 2, 3, 4, 5, 6], [(0, 1), (0, 2)], 1, 1) == 1
    assert find_element([10, 20, 30, 40, 50], [(1, 3), (0, 4)], 2, 0) == 50
    assert find_element([5, 10, 15, 20], [(0, 2), (1, 3)], 1, 3) == 20

def test_flatten():
    assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    assert flatten([10, [20, [30, 40], 50], 60]) == [10, 20, 30, 40, 50, 60]
    assert flatten([0, [0, [0, 0], 0], 0]) == [0, 0, 0, 0, 0, 0]
    assert flatten([1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert flatten([]) == []

def test_find_solution():
    assert find_solution(2, 3, 7) == (2, 1)
    assert find_solution(4, 2, 7) == None
    assert find_solution(1, 13, 17) == (4, 1)
    assert find_solution(3, 5, 11) == (2, 1)
    assert find_solution(6, 9, 1) == None
    assert find_solution(1, 1, 0) == (0, 0)

def test_k_smallest_pairs():
    assert k_smallest_pairs([1, 3, 7], [2, 4, 6], 2) == [[1, 2], [1, 4]]
    assert k_smallest_pairs([1, 3, 7], [2, 4, 6], 1) == [[1, 2]]
    assert k_smallest_pairs([1, 3, 7], [2, 4, 6], 7) == [[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]
    assert k_smallest_pairs([], [2, 4, 6], 3) == []
    assert k_smallest_pairs([1, 3, 7], [], 3) == []
    assert k_smallest_pairs([1, 3, 7], [2, 4, 6], 0) == []

def test_find_kth():
    assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256
    assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8
    assert find_kth([1, 2, 3], [4, 5, 6], 4) == 4
    assert find_kth([1, 3, 5], [2, 4, 6], 3) == 3

def test_largest_subset():
    assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4
    assert largest_subset([1, 2, 4, 8]) == 4
    assert largest_subset([7, 14, 28, 56]) == 4
    assert largest_subset([1]) == 1
    assert largest_subset([2, 3, 5, 7, 11]) == 1

def test_max_sub_array_sum_repeated():
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
    assert max_sub_array_sum_repeated([1, 2, 3], 3, 1) == 6
    assert max_sub_array_sum_repeated([1, -2, 3, -1, 2], 5, 2) == 7

def test_lcs_of_three():
    assert lcs_of_three("AGGT12", "12TXAYB", "12XBA") == 2
    assert lcs_of_three("abcd1e2", "bc12ea", "bd1ea") == 3
    assert lcs_of_three("Reels", "Reelsfor", "ReelsforReels") == 5
    assert lcs_of_three("abc", "def", "ghi") == 0
    assert lcs_of_three("", "", "") == 0

def test_longest_palindromic_subsequence():
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("abcde") == 1
    assert longest_palindromic_subsequence("racecar") == 7
    assert longest_palindromic_subsequence("character") == 5

def test_get_ludic():
    assert get_ludic(10) == [1, 2, 3, 5, 7]
    assert get_ludic(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert get_ludic(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]
    assert get_ludic(1) == [1]
    assert get_ludic(2) == [1, 2]

def test_transpose_matrix():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose_matrix([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert transpose_matrix([[1]]) == [[1]]
    assert transpose_matrix([]) == []

def test_max_sum_bitonic_subsequence():
    assert max_sum_bitonic_subsequence([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum_bitonic_subsequence([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum_bitonic_subsequence([2, 3, 14, 16, 21, 23, 29, 30]) == 138
    assert max_sum_bitonic_subsequence([10, 20, 30, 40]) == 100
    assert max_sum_bitonic_subsequence([10, 5, 1]) == 16

def test_max_average_path():
    assert max_average_path([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert max_average_path([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert max_average_path([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert max_average_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

def test_max_subarray_product():
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80
    assert max_subarray_product([0, 0, 0]) == 0
    assert max_subarray_product([2, 3, -2, 4]) == 6
    assert max_subarray_product([-2, 0, -1]) == 0

def test_get_median():
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0
    assert get_median([1, 3, 5], [2, 4, 6], 3) == 3.5
    assert get_median([10, 20, 30], [15, 25, 35], 3) == 22.5

def test_rearrange_bigger():
    assert rearrange_bigger(12) == 21
    assert rearrange_bigger(10) == False
    assert rearrange_bigger(102) == 120
    assert rearrange_bigger(2017) == 2071
    assert rearrange_bigger(54321) == False
    assert rearrange_bigger(12345) == 12354

def test_bell_number():
    assert bell_number(0) == 1
    assert bell_number(1) == 1
    assert bell_number(2) == 2
    assert bell_number(3) == 5
    assert bell_number(4) == 15
    assert bell_number(5) == 52
    assert bell_number(6) == 203
    assert bell_number(7) == 877
    assert bell_number(8) == 4140
    assert bell_number(9) == 21147
    assert bell_number(10) == 115975

def test_partial():
    add = lambda a, b, c: a + b + c
    partial_add = partial(add, 1, 2)
    assert partial_add(3) == 6
    assert partial_add(4) == 7
    assert partial_add(5) == 8
    multiply = lambda x, y, z: x * y * z
    partial_multiply = partial(multiply, 2)
    assert partial_multiply(3, 4) == 24
    assert partial_multiply(5, 6) == 60
    assert partial_multiply(7, 8) == 112

def test_validate_password():
    assert validate_password("Passw0rd!") == True
    assert validate_password("password123") == False
    assert validate_password("P@ssw0rd") == True
    assert validate_password("12345678") == False
    assert validate_password("!@#$%^&*") == False

def test_extract_even():
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)
    assert extract_even((1, 3, 5)) == ()
    assert extract_even((2, 4, (6, 8, (10, 12)), 14)) == (2, 4, (6, 8, (10, 12)), 14)

def test_sum_amicable_numbers():
    assert sum_amicable_numbers(300) == 504
    assert sum_amicable_numbers(10000) == 31626
    assert sum_amicable_numbers(1000) == 504
    assert sum_amicable_numbers(1) == 0
    assert sum_amicable_numbers(220) == 504

def test_sum_of_binomial_products():
    assert sum_of_binomial_products(3) == 15
    assert sum_of_binomial_products(4) == 56
    assert sum_of_binomial_products(1) == 1
    assert sum_of_binomial_products(0) == 0
    assert sum_of_binomial_products(5) == 210

def test_sum_of_subarray_products():
    assert sum_of_subarray_products([1, 2, 3]) == 20
    assert sum_of_subarray_products([1, 2]) == 5
    assert sum_of_subarray_products([1, 2, 3, 4]) == 84
    assert sum_of_subarray_products([0, 1, 2]) == 5
    assert sum_of_subarray_products([3]) == 3

def test_calculate_sum_tree():
    assert calculate_sum_tree([1, [2, [3, 4], 5], 6]) == 21
    assert calculate_sum_tree([10, [20, [30, 40], 50], 60]) == 210
    assert calculate_sum_tree([0, [0, [0, 0], 0], 0]) == 0
    assert calculate_sum_tree([1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]) == 45

def test_toggle_middle_bits():
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011
    assert toggle_middle_bits(0) == 0
    assert toggle_middle_bits(1) == 1

def test_calculate_depth_tree():
    assert calculate_depth_tree([1, [2, [3, 4], 5], 6]) == 4
    assert calculate_depth_tree([10, [20, [30, 40], 50], 60]) == 4
    assert calculate_depth_tree([0, [0, [0, 0]], 0]) == 4
    assert calculate_depth_tree([1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]) == 9
    assert calculate_depth_tree([]) == 0

def test_find_largest_value_tree():
    assert find_largest_value_tree([1, [2, [3, 4], 5], 6]) == 6
    assert find_largest_value_tree([10, [20, [30, 40], 50], 60]) == 60
    assert find_largest_value_tree([0, [0, [0, 0], 0], 0]) == 0
    assert find_largest_value_tree([1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]) == 9

def test_tuple_intersection():
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)], [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)], [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}
    assert tuple_intersection([], [(1, 2), (2, 3)]) == set()
    assert tuple_intersection([(1, 2), (2, 3)], []) == set()
    assert tuple_intersection([], []) == set()
