from imports import *

# Take the base and Height of a triangle and return area size
def rightTriangleArea(base: int, height: int) -> float:
    return ((base * height) / 2)

def cubes(num: int) -> int:
    return (num ** 3)

#Takes the age in years, returns age in days
def calc_age(age: int) -> int:
    return (age * 365)

# Convert hours to secounds
def how_many_secounds(hours: int) -> int:
    return (hours * 60 * 60)

# Win = 3 points, draw = 1 point, loss = 0 points
def football_points(wins: int, draws: int, losses: int) -> int:
    return ((wins * 3) + (draws * 1) + (losses * 0))

def get_first_value(values: list) -> int:
    return (values[0])

def animals(chickens: int, cows: int, pigs: int) -> int:
    chickenLegs = 2
    cowLegs = 4
    pigLegs = 4
    return ((chickens * chickenLegs) + (cows * cowLegs) + (pigs * pigLegs))

def give_me_something(string: str) -> str:
    return ("something " + string)

def points(twos: int, threes: int) -> int:
    return ((threes * 3) + (twos * 2))

def greeting(name):
    if name == "Mubashir":
        return "Hello, my Love!"
    else:
        return "Hello, " + name + "!"

def findLargestNum(values: list) -> int:
    largest = values[0]
    for i in values:
        if i > largest:
            largest = i
    return largest

"""validate email address as a string. Each must have
- Start with one or more alphanumeric characters
- contain an @symbol
- Followed by one ore more alphanumeric characters
- Followed by a period
- Followed by two more more alphanumeric characters"""
def validate_email_address(email: str) -> bool:
    if re.search("[a-zA-Z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z0-9][a-zA-Z0-9]+", email) != None:
        return True
    return False

# Given an integer, return the reult of that to the power of 2. Use a for loop with the Math Library
def calculate_exponential_power(num: int) -> int:
    return (num * num)

def extract_nth_element(list_of_tuples: tuple, n: int) -> list:
    """
    Extract the nth element from each tuple in the list.

    Args:
        list_of_tuples (list): A list of tuples.
        n (int): The index of the element to extract from each tuple.

    Returns:
        list: A list containing the nth element from each tuple.
    """
    values = []
    for i in list_of_tuples:
        values.append(i[n])
    return values

def extract_rear(test_tuple: tuple) -> list:
    """
    Extract the last character of each string in the given tuple.

    Args:
    test_tuple (tuple): A tuple of strings.

    Returns:
    list: A list containing the last character of each string in the tuple.
    """
    # Placeholder for the solution
    values = []
    for i in test_tuple:
        values.append(i[-1])
    return values

def extract_values(text: str) -> list:
    """
    Extracts all values enclosed in double quotation marks from the input string.

    Args:
        text (str): The input string containing quoted values.

    Returns:
        list: A list of values found within double quotation marks.
    """
    # Implement the function logic here
    values = re.findall("\"[a-zA-Z0-9]+\"", text)
    for i in range(len(values)):
        values[i] = values[i][1:-1]
    return values

def extract_string(strings: list, length: int) -> list:
    """
    Extract strings of a specified length from a list of strings.

    Args:
        strings (list): A list of string values.
        length (int): The desired length of strings to extract.

    Returns:
        list: A list of strings with the specified length.
    """
    # Implement the function logic here
    values = []
    for i in strings:
        if len(i) == length:
            values.append(i)
    return values

def filter_dict_by_value(data: dict, n: int) -> dict:
    """
    Filters a dictionary to include only entries with values greater than or equal to n.

    Args:
        data (dict): The input dictionary with string keys and integer values.
        n (int): The threshold value.

    Returns:
        dict: A dictionary containing only the key-value pairs where the value is >= n.
    """
    # ChatGPT Solution
    # return {key: value for key, value in data.items() if value >= n}
    values = {}
    for i in data.items():
        if i[1] >= n:
            values.update({i[0]: i[1]})
    return values

def filter_students(students, min_height, min_weight):
    """
    Filters students based on minimum height and weight.

    Args:
        students (dict): A dictionary with student names as keys and (height, weight) tuples as values.
        min_height (float): The minimum height requirement.
        min_weight (float): The minimum weight requirement.

    Returns:
        dict: A dictionary of students meeting the height and weight criteria.
    """
    # Initialize the result dictionary
    return {key: value for key, value in students.items() if ((value[0]) >= min_height and (value[1]) >= min_weight)}

def find_dissimilar(tuple1: tuple, tuple2: tuple) -> tuple:
    return subDissimilar(tuple1, tuple2) + subDissimilar(tuple2, tuple1)

def subDissimilar(tuple1: tuple, tuple2: tuple) -> tuple:
    values = ()
    for i in tuple1:
        valid = True
        for j in tuple2:
            if i == j:
                valid = False
        if valid:
            values = values + (i,)
    return values

def find_adverb_position(text):
    """
    Find the first adverb in the text and return its position and value.

    Args:
        text (str): The input text to search.

    Returns:
        tuple or None: A tuple (start, end, adverb) if an adverb is found, otherwise None.
    """
    # Use a regular expression to find words ending with 'ly'.
    # Return the first match's start, end, and the word itself.
    search = re.search("[a-zA-Z]*ly", text)
    if search != None:
        start = search.span()[0]
        end = search.span()[1]
        value = (start, end, text[start:end])
    else:
        value = None
    return value

def find_first_occurrence(A: list, x: int) -> int:
    """
    Find the index of the first occurrence of x in the sorted list A.

    Args:
    A (list): A sorted list of integers.
    x (int): The target integer to find.

    Returns:
    int: The index of the first occurrence of x, or -1 if not found.
    """
    # Initialize the search bounds
    count = 0
    for i in A:
        if i == x:
            return count
        count += 1
    return -1

def first_odd(nums):
    """
    Find the first odd number in the list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The first odd number in the list, or -1 if no odd number exists.
    """
    # Your code here
    for i in nums:
        if i % 2 == 1:
            return i
    return -1

def long_words(n: int, sentence: str) -> list:
    """
    Return a list of words from the sentence that are longer than n characters.

    Args:
    n (int): The minimum length of words to include.
    sentence (str): The input sentence.

    Returns:
    list: A list of words longer than n characters.
    """
    # Split the sentence into words
    words = sentence.split()
    result = []
    # Placeholder for the result
    for i in words:
        if len(i) > n:
            result.append(i)
    # Iterate through words and filter based on length
    # Add your implementation here
    return result

def find_max_length_element(lst: list) -> list:
    """
    Find the sublist with the maximum length in a list of lists.

    Args:
        lst (list of lists): A list containing sublists.

    Returns:
        list: The sublist with the maximum length.
    """
    # Your code here
    longest = 0
    value = []
    for i in lst:
        if len(i) > longest:
            value = i
            longest = len(i)
    return value

def max_length(list_of_lists):
    """
    Find the longest list in a list of lists and return its length and the list itself.

    Args:
        list_of_lists (list of list): A list containing sublists.

    Returns:
        tuple: A tuple containing the length of the longest list and the list itself.
    """
    # Placeholder for the solution
    value = find_max_length_element(list_of_lists)
    return (len(value), value)

def max_val(listval):
    """
    Find the maximum integer value in a heterogeneous list.

    Args:
        listval (list): A list containing elements of various data types.

    Returns:
        int: The maximum integer value in the list.
    """
    # Filter the integers and find the maximum value
    largest = 0
    for i in listval:
        if type(i) == int:
            if i > largest:
                largest = i
    return largest

def max_length_list(input_list):
    """
    Find the list with the maximum length in a list of lists.

    Args:
        input_list (list of lists): A list containing sublists.

    Returns:
        tuple: A tuple containing the maximum length and the list with the maximum length.
    """
    # Placeholder for the solution
    largest = 0
    value = (0, None)
    for i in input_list:
        if len(i) > largest:
            largest = len(i)
            value = (largest, i)
    return value

def min_val(listval):
    """
    Find the maximum integer value in a heterogeneous list.

    Args:
        listval (list): A list containing elements of various data types.

    Returns:
        int: The maximum integer value in the list.
    """
    # Filter the integers and find the maximum value
    smallest = max_val(listval)
    for i in listval:
        if type(i) == int:
            if i < smallest:
                smallest = i
    return smallest

def min_k(test_list, K):
    """
    Find the minimum K records from a list of tuples based on the second element of each tuple.

    Args:
    test_list (list): A list of tuples where each tuple contains a string and an integer.
    K (int): The number of minimum records to return.

    Returns:
    list: A list of K tuples with the smallest integer values.
    """
    # Sort the list based on the second element of the tuples
    sorted_list = sorted(test_list, key=lambda x: x[1])
    
    # Return the first K elements of the sorted list
    return sorted_list[:K]

def find_min_length_sublist(lst):
    """
    Find the sublist with the minimum length in a list of lists.

    Args:
        lst (list of lists): A list containing sublists.

    Returns:
        list: The sublist with the minimum length.
    """
    # Your code here
    return min(lst, key=len)


def index_minimum(tuples_list: List[Tuple[str, int]]) -> str:
    """
    Given a list of tuples, return the first value of the tuple with the smallest second value.

    Args:
    tuples_list (List[Tuple[str, int]]): A list of tuples where each tuple contains a string and an integer.

    Returns:
    str: The first element of the tuple with the smallest second value.
    """
    # Your code here
        # Find the tuple with the minimum second value
    min_tuple = min(tuples_list, key=lambda x: x[1])
    
    # Return the first element (string) of the tuple
    return min_tuple[0]


def find_n_largest(nums: List[int], n: int) -> List[int]:
    """
    Returns the n largest integers from the list nums in descending order.

    Args:
    nums (List[int]): The list of integers.
    n (int): The number of largest integers to return.

    Returns:
    List[int]: A list of the n largest integers in descending order.
    """
    # Sort the list of nums
    lst = sorted(nums, reverse=True)
    return lst[:n]

def perfect_squares(a: int, b: int) -> list:
    """
    Find all perfect squares between two numbers a and b (inclusive).

    Args:
        a (int): The starting number.
        b (int): The ending number.

    Returns:
        list: A list of perfect squares between a and b.
    """
    # Placeholder for the solution
    num = 0
    square = num * num
    values = []
    while square <= b:
        if square >= a:
            values.append(square)
        num += 1
        square = num * num
    return values

def find_shared_elements(list1, list2):
    """
    Find the shared elements between two lists.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        list: A list of unique elements that are common to both input lists.
    """
    # Your code here
    values = []
    for i in list1:
        if i in list2:
            values.append(i)
    return values
            
def find_hypotenuse(a: float, b: float) -> float:
    """
    Calculate the hypotenuse of a right-angled triangle given the other two sides.

    Args:
        a (float): Length of one side.
        b (float): Length of the other side.

    Returns:
        float: Length of the hypotenuse.
    """
    # Implement the Pythagorean theorem here
    return round(math.sqrt(math.pow(a, 2) + math.pow(b, 2)), 2)


def find_tuples(test_list, k):
    """
    Filters tuples from the list where all elements are divisible by k.

    Args:
    test_list (list of tuples): The list of tuples to filter.
    k (int): The divisor.

    Returns:
    list of tuples: A list containing tuples where all elements are divisible by k.
    """
    # Placeholder for the solution
    values = []
    for i in test_list:
        div = True
        for j in i:
            if j % k != 0:
                div = False
        if div:
            values.append(i)
    return values

def find_words_starting_with_p(words):
    """
    Finds the first two words starting with 'P' from the first string in the list.

    Args:
        words (list of str): A list of strings containing words.

    Returns:
        tuple or None: A tuple of the first two words starting with 'P', or None if not found.
    """
    # Iterate through the list of strings
    for string in words:
        # Split the string into words
        word_list = string.split()
        # Filter words starting with 'P'
        p_words = [word for word in word_list if word.startswith('P')]
        # Check if there are at least two such words
        if len(p_words) >= 2:
            return (p_words[0], p_words[1])
    # Return None if no such pair is found
    return None

def find_char_long(text: str) -> list:
    """
    Find all words in the input string that are at least 4 characters long.

    Args:
        text (str): The input string.

    Returns:
        list: A list of words that are at least 4 characters long.
    """
    # Use a regular expression to find words of at least 4 characters.
    lst = text.split(" ")
    values = []
    for i in lst:
        if len(i) >= 4:
            values.append(i)
    return values

def first_non_repeating_character(input_string):
    """
    Find the first non-repeated character in the given string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        str or None: The first non-repeated character, or None if all characters are repeated.
    """
    # Initialize data structures to track character counts and order
    # Implement the logic to find the first non-repeated character
    # Create a dictionary to store the frequency of each character
    char_count = {}

    # Count the frequency of each character in the input string
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with a count of 1
    for char in input_string:
        if char_count[char] == 1:
            return char

    # Return None if no non-repeating character is found
    return None

def first_repeated_char(input_string):
    """
    Find the first repeated character in the given string.

    Args:
        input_string (str): The string to search for repeated characters.

    Returns:
        str or None: The first repeated character, or None if no character is repeated.
    """
    # Placeholder for the solution
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first character with a count of 1
    for char in input_string:
        if char_count[char] > 1:
            return char

def add_to_shopping_list(item, current_list=None):
    """
    Adds an item to the shopping list.

    Args:
    item (str): Item to be added
    current_list (list): (optional), the current list of items; assume empty if not provided

    Returns:
    list: List of items in the shopping list
    """
    if current_list is None:
        current_list = []
    
    current_list.append(item)
    return current_list

def flatten_to_set(list_of_lists: list) -> set:
    """
    Flattens a list of lists or tuples into a single set of unique numbers.

    Args:
        list_of_lists (list): A list containing lists or tuples of numbers.

    Returns:
        set: A set containing all unique numbers from the input.
    """
    # Placeholder for the solution
    values = set()
    for i in list_of_lists:
        for j in i:
            if j not in values:
                values.add(j)
    return values

def flatten_list(nested_list: list) -> list:
    """
    Flattens a nested list into a single list.

    Args:
        nested_list (list): A list that may contain other lists as elements.

    Returns:
        list: A flattened list containing all elements from the nested structure.
    """
    # Placeholder for the solution
    values = []
    for i in nested_list:
        if type(i) == list:
            temp = (flatten_list(i))
            for j in temp:
                values.append(j)
        else:
            values.append(i)
    return values

def frequency_lists(list_of_lists):
    """
    Calculate the frequency of each element in a flattened list of lists.

    Args:
        list_of_lists (list of list of int): A list containing sublists of integers.

    Returns:
        dict: A dictionary with elements as keys and their frequencies as values.
    """
    # Flatten the list of lists into a single list
    # Count the frequency of each element
    # Return the frequency dictionary
    lst = flatten_list(list_of_lists)
    
    # Count the frequency of each element
    values = {}
    for i in lst:
        values[i] = values.get(i, 0) + 1  # Increment the frequency of each element
    
    return values

def combinations_with_repetition(lst: List[str], n: int) -> List[Tuple[str, ...]]:
    """
    Generate all combinations with repetition of the elements in the list.

    Args:
        lst (List[str]): The list of elements.
        n (int): The length of each combination.

    Returns:
        List[Tuple[str, ...]]: A list of tuples representing the combinations.
    """
    def generate_combinations(start: int, current_combination: List[str]):
        if len(current_combination) == n:
            result.append(tuple(current_combination))
            return
        for i in range(start, len(lst)):
            current_combination.append(lst[i])
            generate_combinations(i, current_combination)  # allow repetition by not moving 'start'
            current_combination.pop()  # backtrack

    result = []
    generate_combinations(0, [])
    return result

def geometric_sum(n: int) -> float:
    """
    Calculate the geometric sum of n-1 using recursion.

    Args:
        n (int): The input non-negative integer.

    Returns:
        float: The geometric sum.
    """
    # Base case: when n is 0
    # Recursive case: calculate the sum for n-1
    # S(n) = SUM from 0->n of 1/(2^i)
    if n == 0:
        return 1
    elif n > 0:
        return ((1 / (pow(2, n))) + geometric_sum(n-1))
    else:
        print("error, negative number provided")
        return -1

def group_by(func, seq: List) -> dict:
    """
    Groups the elements of the sequence based on the result of applying the function to each element.

    Args:
    func: The function to apply.
    seq: The input sequence.

    Returns:
    dict: The dictionary with grouped elements.
    """
    result = {}
    for item in seq:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result

def harmonic_sum(n: int) -> float:
    """
    Calculate the harmonic sum of the first n terms.

    Args:
        n (int): The number of terms to include in the harmonic sum.

    Returns:
        float: The harmonic sum of the first n terms.
    """
    # Base case: if n is 1, return 1
    # Recursive case: add 1/n to the harmonic sum of (n-1)
    if n == 1:
        return 1
    elif n > 1:
        return (harmonic_sum(n-1) + (1/n))
    else:
        print("invalid input provided")

def heap_sort(iterable):
    """
    Sorts a list of integers using the heap sort algorithm.

    Args:
        iterable (list): A list of integers to be sorted.

    Returns:
        list: A new list containing the sorted integers.
    """
    # Create a heap from the iterable (in-place)
    hq.heapify(iterable)
    
    # Extract the elements from the heap, which will be in sorted order
    sorted_list = []
    while iterable:
        sorted_list.append(hq.heappop(iterable))
    
    return sorted_list

def highest_power_of_2(n):
    """
    Find the highest power of 2 less than or equal to n.

    Args:
        n (int): The input number.

    Returns:
        int: The highest power of 2 less than or equal to n.
    """
    if n <= 0:
        return 0  # There's no power of 2 less than or equal to 0 or negative numbers

    # Bit manipulation: find the highest power of 2 <= n
    return 1 << (n.bit_length() - 1)

def is_not_prime(n: int) -> bool:
    """
    Determine if a number is not a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is not prime, False otherwise.
    """
    # Placeholder for the solution
    if n == 1:
        return True
    for i in range(2, n):
        if n%i == 0:
            return True
    return False

def add_nested_tuples(tuple1, tuple2):
    """
    Perform index-wise addition of elements in two nested tuples.

    Args:
        tuple1 (tuple): The first nested tuple.
        tuple2 (tuple): The second nested tuple.

    Returns:
        tuple: A new nested tuple with index-wise added elements.
    """
    # Placeholder for the solution
    return tuple(
        tuple(a + b for a, b in zip(inner1, inner2))
        for inner1, inner2 in zip(tuple1, tuple2)
    )

def insert_element(lst: list, element: any) -> list:
    """
    Inserts the given element before each element in the list.

    Args:
        lst (list): The original list.
        element (any): The element to insert before each item in the list.

    Returns:
        list: The modified list with the element inserted before each item.
    """
    # Your code here
    values = []
    for i in lst:
        values.append(element)
        values.append(i)
    return values

def interleave_lists(list1: list, list2: list, list3: list) -> list:
    """
    Interleave three lists of the same length into a single flat list.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        list: A new list with elements interleaved from the input lists.
    """
    # Implement the interleaving logic here
    values = []
    for i in range(len(list1)):
        values.append(list1[i])
        values.append(list2[i])
        values.append(list3[i])
    return values

def jacobsthal_num(n):
    """
    Calculate the nth Jacobsthal number.

    Args:
        n (int): The index of the Jacobsthal number to compute.

    Returns:
        int: The nth Jacobsthal number.
    """
    # Implement the function logic here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return (jacobsthal_num(n - 1) + (2 * jacobsthal_num(n - 2)))

def join_integers(numbers: list) -> int:
    """
    Joins a list of integers into a single integer.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: A single integer formed by concatenating the input integers.
    """
    # Placeholder for the solution
    value = ""
    for i in numbers:
        value = value + str(i)
    return int(value)

def kth_element(arr: list, k: int) -> int:
    """
    Find the kth smallest element in the array using 1-based indexing.

    Args:
        arr (list): A list of distinct integers.
        k (int): The 1-based index of the element to find.

    Returns:
        int: The kth smallest element in the array.
    """
    # Sort the array in ascending order
    # Return the element at the (k-1)th index
    return sorted(arr)[k-1]

def largest_negative(numbers: list) -> int:
    """
    Find the largest negative number in the list.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The largest negative number, or None if no negative numbers exist.
    """
    # Placeholder for the solution
    value = None
    for i in numbers:
        if i < 0:
            if value == None: 
                value = i
            elif i > value:
                value = i
    return value

def find_largest_number(digits: list) -> int:
    """
    Given a list of single-digit integers, return the largest number that can be formed by arranging them.

    Args:
    digits (list): A list of single-digit integers.

    Returns:
    int: The largest number that can be formed.
    """
    # Sort the digits in descending order
    # Combine the sorted digits into a single number
    return join_integers(sorted(digits, reverse=True))

def large_product(nums1, nums2, N):
    """
    Find the N largest products from two lists.

    Args:
    nums1 (list): First list of integers.
    nums2 (list): Second list of integers.
    N (int): Number of largest products to return.

    Returns:
    list: A list of the N largest products.
    """
    # Placeholder for the solution
    bigNums = []
    for i in nums1:
        for j in nums2:
            bigNums.append(i * j)
    return (sorted(bigNums, reverse=True)[:N])

def largest_triangle_area(radius: float) -> float:
    """
    Calculate the area of the largest triangle that can be inscribed in a semicircle.

    Args:
    radius (float): The radius of the semicircle.

    Returns:
    float: The area of the largest inscribed triangle.
    """
    # Placeholder for the solution
    return (0.5 * radius * radius)

def last_digit_factorial(n: int) -> int:
    """
    Calculate the last digit of the factorial of a given number.

    Args:
    n (int): A non-negative integer.

    Returns:
    int: The last digit of the factorial of n.
    """
    # Placeholder for the solution
    return math.factorial(n)%10

def last_position(arr: list, x: int) -> int:
    """
    Find the last position of x in a sorted array arr.

    Parameters:
    arr (list): A sorted list of integers.
    x (int): The target integer to find.

    Returns:
    int: The last position of x in arr, or -1 if x is not found.
    """
    # Implement the function using binary search
    pos = -1
    for i in range(len(arr)):
        if arr[i] == x:
            pos = i
    return pos

def lateral_surface_area_cone(r: float, h: float) -> float:
    """
    Calculate the lateral surface area of a cone given its radius and height.

    Parameters:
    r (float): The radius of the cone's base.
    h (float): The height of the cone.

    Returns:
    float: The lateral surface area of the cone.
    """
    # Calculate the slant height
    # Calculate the lateral surface area
    # Return the result
    slantHeight = math.sqrt(pow(r, 2) + pow(h, 2))
    return math.pi * r * slantHeight

def lateral_surface_area_cylinder(radius: float, height: float) -> float:
    """
    Calculate the lateral surface area of a cylinder.

    Args:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.

    Returns:
        float: The lateral surface area of the cylinder.
    """
    # Placeholder for the solution
    return (2 * math.pi * radius * height)

def left_insertion(a: list, x: any) -> int:
    """
    Find the left insertion point for x in sorted list a.

    Parameters:
    a (list): A sorted list of elements.
    x (any): The value to find the insertion point for.

    Returns:
    int: The index where x should be inserted.
    """
    # Your code here
    for i in range(len(a)):
        if a[i] == x:
            return i
        elif a[i] > x:
            return i
    return len(a)

def combine_lists(list1: list, list2: list) -> list:
    """
    Combines two lists by summing corresponding elements.

    Args:
        list1 (list): The first input list of integers.
        list2 (list): The second input list of integers.

    Returns:
        list: A new list with the sum of corresponding elements.
    """
    # TODO: Implement the combine_lists function
    return [a + b for a, b in zip(list1, list2)]

def find_common_elements(list1, list2):
    """
    Finds the common elements between two lists.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A new list with the common elements.
    """
    # TODO: Implement the find_common_elements function
    return list(set(list1) & set(list2))

def list_difference(list1: list, list2: list) -> list:
    """
    Returns the symmetric difference of two lists.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list containing elements that are in either of the lists but not in both.
    """
    # Implement the function logic here
    commons = find_common_elements(list1, list2)
    values = list1 + list2
    for i in commons:
        while values.count(i) > 0:
            values.remove(i)
    return values

def filter_positive_numbers(numbers: list) -> list:
    """
    Filters a list to include only the positive numbers.

    Args:
        numbers (list): The input list of integers.

    Returns:
        list: A new list with the positive numbers.
    """
    # TODO: Implement the filter_positive_numbers function
    return [a for a in numbers if a > 0]

def filter_lists(func, lst: list) -> list:
    """
    Applies a function to each element in a list and returns a new list containing only the elements for which the function returns True.

    Args:
    func (function): The function to apply to each element.
    lst (list): The input list.

    Returns:
    list: The new list containing the filtered elements.
    """
    # TODO: Implement the filter_lists function
    return [a for a in lst if func(a)]

def map_lists(func, lst):
    """
    Applies a function to each element in a list and returns a new list containing the results.

    Args:
    func (function): The function to apply to each element.
    lst (list): The input list.

    Returns:
    list: The new list containing the results of applying the function to each element.
    """
    # TODO: Implement the map_lists function
    return [func(a) for a in lst]

def reduce_lists(func, lst):
    """
    Applies a function to the elements of a list in a cumulative way and returns the result.

    Args:
    func (function): The function to apply to the elements.
    lst (list): The input list.

    Returns:
    Any: The result of applying the function to the entire list.
    """
    # TODO: Implement the reduce_lists function
    value = lst.pop(0)
    while len(lst) > 0:
        value = func(value, lst.pop(0))
    return value

def sort_students(students: list) -> list:
    """
    Sorts the given list of student dictionaries in ascending order based on their age.

    Args:
        students (list): The input list of student dictionaries.

    Returns:
        list: A new list with the students sorted based on their age.
    """
    # TODO: Implement the sort_students function
    return sorted(students, key=lambda student: student["age"])

def square_even_numbers(numbers: list) -> list:
    """
    Creates a new list containing the squares of the even numbers in the input list.

    Args:
        numbers (list): The input list of integers.

    Returns:
        list: A new list with the squared even numbers.
    """
    # TODO: Implement the square_even_numbers function
    return [pow(a, 2) for a in numbers if (a%2 == 0)]

def find_max_length(lst: list) -> int:
    """
    Find the length of the longest sublist in a list of lists.

    Args:
        lst (list of lists): A list containing sublists.

    Returns:
        int: The length of the longest sublist.
    """
    # Implement the function logic here
    mlen = 0
    for i in lst:
        if len(i) > mlen: mlen = len(i)
    return mlen

def len_longest_word(words: list) -> int:
    """
    Find the length of the longest word in the list.

    Args:
        words (list of str): A list of strings.

    Returns:
        int: The length of the longest word.
    """
    # Placeholder for the solution
    mlen = 0
    for i in words:
        if len(i) > mlen: mlen = len(i)
    return mlen

def is_magic_square(matrix: list[list[int]]) -> bool:
    """
    Determine if the given square matrix is a magic square.

    Args:
        matrix (list[list[int]]): A square matrix of integers.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    # Ensure matrix is not empty and all rows are equal in length
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        return False
    
    # Calculate the reference sum from the first row
    reference_sum = sum(matrix[0])
    
    # Check if the sum of each row is equal to the reference sum
    for row in matrix:
        if sum(row) != reference_sum:
            return False
    
    # Check if the sum of each column is equal to the reference sum
    for col in range(n):
        column_sum = sum(matrix[row][col] for row in range(n))
        if column_sum != reference_sum:
            return False
    
    # Check the main diagonal
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    if main_diag_sum != reference_sum:
        return False

    # Check the anti-diagonal
    anti_diag_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if anti_diag_sum != reference_sum:
        return False

    # If all checks passed, it's a magic square
    return True

def match_a_followed_by_b(text):
    """
    Check if the input string contains an 'a' followed by one or more 'b's.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the pattern is found, False otherwise.
    """
    # Define the regular expression pattern
    pattern = 'ab' 
    return bool(re.search(pattern, text))

def text_match_wordz(text):
    """
    Check if the given text contains a word with the letter 'z'.

    Args:
        text (str): The input string.

    Returns:
        bool: True if a word with 'z' is found, False otherwise.
    """
    # TODO: Implement this function
    fil = '[zZ]'
    if re.search(fil, text) != None:
        return True
    else:
        return False

def max_product_tuple(list_of_tuples: list) -> int:
    """
    Calculate the maximum absolute product of two integers in any tuple from the list.

    Args:
    list_of_tuples (list of tuple): A list of tuples, each containing two integers.

    Returns:
    int: The maximum absolute product.
    """
    # Placeholder for the solution
    return max(abs(x[0] * x[1]) for x in list_of_tuples)

def max_aggregate(stdata: list) -> tuple:
    """
    Calculate the maximum aggregate score from a list of tuples.

    Args:
        stdata (list): A list of tuples where each tuple contains a name (str) and a score (int).

    Returns:
        tuple: A tuple containing the name with the highest aggregate score and the score itself.
    """
    # Placeholder for the solution
    dic = {}
    
    # Aggregate the scores for each name
    for name, score in stdata:
        dic[name] = dic.get(name, 0) + score

    # Find the name with the highest aggregate score
    max_name = max(dic, key=dic.get)
    max_score = dic[max_name]

    return (max_name, max_score)

def max_sub_array_sum(arr: list) -> int:
    """
    Find the sum of the largest contiguous sublist in the given list.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The sum of the largest contiguous sublist.
    """
    # Initialize variables to track the maximum sum and current sum
    # Implement the logic to find the maximum sum of a contiguous sublist
    maxSum = 0
    currentSum = 0
    start = 0
    end = 0
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            currentSum += arr[j]
            if currentSum > maxSum:
                maxSum = currentSum
        currentSum = 0
    return maxSum

def find_max_difference(binary_string: str) -> int:
    """
    Calculate the maximum difference between the number of 0s and 1s in any substring.

    Args:
        binary_string (str): A string consisting of '0's and '1's.

    Returns:
        int: The maximum difference between the count of '0's and '1's in any substring.
    """
    # Edge case: if the string is empty, the difference is 0
    if not binary_string:
        return 0

    # Initialize variables for Kadane's algorithm
    max_diff = 0  # We start from 0, as the best case when no difference can be negative is 0
    current_diff = 0  # This will store the current difference as we iterate through the string

    # Traverse through the binary string
    for char in binary_string:
        # Update the difference: +1 for '0', -1 for '1'
        current_diff += 1 if char == '0' else -1

        # Update the max_diff with the largest difference encountered
        max_diff = max(max_diff, current_diff)

        # If current_diff goes negative, reset it to 0 (start a new subarray)
        if current_diff < 0:
            current_diff = 0

    return max_diff

def max_difference(tuple_list):
    """
    Calculate the maximum absolute difference between pairs in a list of tuples.

    Args:
        tuple_list (list of tuple): A list of tuples, each containing two integers.

    Returns:
        int: The maximum absolute difference between the integers in the tuples.
    """
    # Placeholder for the solution
    maxNum = 0
    for i in tuple_list:
        difference = abs(i[0] - i[1]) 
        if (difference) > maxNum: maxNum = difference
    return maxNum

def max_occurrences(nums):
    """
    Find the item with the maximum frequency in the list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The integer with the highest frequency, or None if the list is empty.
    """
    # Initialize a dictionary to count occurrences
    frequency = defaultdict(int)

    # Count the occurrences of each number
    for num in nums:
        frequency[num] += 1

    # Placeholder for the solution
    if not nums:
        return None
    
    max_freq_num = max(frequency, key=frequency.get)
    return max_freq_num
    
def max_of_nth(matrix: list, n: int) -> int:
    """
    Returns the maximum value in the nth column of the given matrix.

    Args:
        matrix (list of list of int): The input matrix.
        n (int): The column index to find the maximum value for.

    Returns:
        int: The maximum value in the nth column.
    """
    # Placeholder for the solution
    maxNum = 0
    for i in matrix:
        if i[n] > maxNum: maxNum = i[n]
    return maxNum

def max_product_pair(arr: list) -> tuple:
    """
    Find the pair of integers in the list that have the highest product.

    Args:
        arr (list): A list of integers.

    Returns:
        tuple: A tuple containing the pair of integers with the highest product, or None if not possible.
    """
    # Check if the list has fewer than two elements
    if len(arr) < 2:
        return None

    # Placeholder for the solution
    arr.sort()

    prod1 = arr[0] * arr[1]
    prod2 = arr[-1] * arr[-2]

    if (prod1 > prod2): return (arr[1], arr[0])
    else: return (arr[-2], arr[-1])

def max_sum_list(lists: list) -> list:
    """
    Returns the list in a list of lists whose sum of elements is the highest.

    Args:
        lists (list of list of int): A list containing lists of integers.

    Returns:
        list of int: The list with the highest sum of elements.
    """
    # Your code here
    maxsum = sum(lists[0])
    maxList = lists[0]
    for i in lists:
        if sum(i) > maxsum: 
            maxsum = sum(i)
            maxList = i
    return maxList

def max_run_uppercase(test_str):
    """
    Find the maximum run of consecutive uppercase characters in the given string.

    Args:
    test_str (str): The input string.

    Returns:
    int: The length of the longest run of uppercase characters.
    """
    # Initialize variables to track the current and maximum runs
    # Placeholder for the solution
    return (len(max(re.findall("[A-Z]*", test_str), key=lambda x: len(x))))

def maximize_elements(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Given two tuples of tuples, return a new tuple of tuples where each inner tuple
    contains the element-wise maximum of the corresponding inner tuples from the inputs.

    Args:
    tuple1 (tuple of tuples): The first input tuple of tuples.
    tuple2 (tuple of tuples): The second input tuple of tuples.

    Returns:
    tuple of tuples: A new tuple of tuples with element-wise maximum values.
    """
    # Initialize the result tuple
    result = tuple(
        tuple(max(a, b) for a, b in zip(t1, t2))  # Find element-wise max for each pair of inner tuples
        for t1, t2 in zip(tuple1, tuple2)
    )
    
    return result

def max_abs_diff(arr):
    """
    Calculate the maximum absolute difference between any two elements in the array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum absolute difference between any two elements.
    """
    # Placeholder for the solution
    arr.sort()
    return abs(arr[0] - arr[-1])

def merge_dictionaries_three(dict1, dict2, dict3):
    """
    Merges three dictionaries into one. If keys overlap, the value from the later dictionary takes precedence.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
        dict3 (dict): The third dictionary.

    Returns:
        dict: The merged dictionary.
    """
    # Placeholder for the solution
    return {**dict1, **dict2, **dict3}

def combineLists(a: list, b: list) -> list:
    for i in b:
        a.append(i)
    return a

def merge_sorted_lists(list1: List[int], list2: List[int], list3: List[int]) -> List[int]:
    """
    Merge three lists into a single sorted list.

    Args:
        list1 (List[int]): The first list of integers.
        list2 (List[int]): The second list of integers.
        list3 (List[int]): The third list of integers.

    Returns:
        List[int]: A sorted list containing all integers from the three input lists.
    """
    # Your code here
    value = combineLists(list1, list2)
    value = combineLists(value, list3)
    return sorted(value)

def min_swaps(str1: str, str2: str) -> int:
    """
    Calculate the minimum number of swaps required to convert one binary string to another.

    Args:
    str1 (str): The initial binary string.
    str2 (str): The target binary string.

    Returns:
    int: The minimum number of swaps required, or "Not Possible" if conversion is not feasible.
    """
    # If the lengths of the two strings are different, return "Not Possible"
    if len(str1) != len(str2):
        return "Not Possible"
    
    # Initialize counters for mismatched '1's and '0's
    ones_in_str1 = ones_in_str2 = 0
    zeros_in_str1 = zeros_in_str2 = 0
    
    # Count the number of mismatches between '1' and '0' in both strings
    for a, b in zip(str1, str2):
        if a == '1' and b == '0':
            ones_in_str1 += 1
        elif a == '0' and b == '1':
            ones_in_str2 += 1
    
    # If the mismatches of '1' and '0' are not equal, it's not possible to convert
    if ones_in_str1 != ones_in_str2:
        return "Not Possible"
    
    # The minimum swaps needed is equal to the number of mismatches
    return ones_in_str1

def find_min_diff(arr: list) -> int:
    """
    Find the minimum difference between any two elements in the array.

    Args:
    arr (list): A list of integers.

    Returns:
    int: The minimum difference between any two elements.
    """
    # Sort the array to bring closer elements together
    # Initialize the minimum difference to a large value
    # Iterate through the sorted array to find the minimum difference
    arr.sort()
    minDistance = arr[-1] - arr[0]
    for i in range(0, len(arr)-1):
        if minDistance > arr[i+1] - arr[i]: minDistance = arr[i+1] - arr[i]
    return minDistance

def min_jumps(steps: Tuple[int, int], d: int) -> int:
    """
    Calculate the minimum number of jumps required to reach the point (d, 0).

    Args:
    steps (Tuple[int, int]): A tuple containing two possible jump lengths.
    d (int): The x-coordinate of the target point.

    Returns:
    int: The minimum number of jumps required, or -1 if it is not possible.
    """
    step1, step2 = sorted(steps, reverse=True)  # Ensure step1 is the larger step
    
    # Try different combinations of jumps of step1 and step2
    min_jumps_required = float('inf')  # Start with an infinite number of jumps
    
    for i in range(d // step1 + 1):  # Try from 0 to max possible jumps of step1
        remaining_distance = d - i * step1  # Remaining distance after taking i jumps of step1
        
        # If remaining distance can be exactly divided by step2, it's a valid combination
        if remaining_distance % step2 == 0:
            # Calculate total jumps: i jumps of step1 + the number of jumps of step2
            total_jumps = i + (remaining_distance // step2)
            # Update the minimum jumps if this combination is better
            min_jumps_required = min(min_jumps_required, total_jumps)
    
    # If no valid combination is found, return -1 (not possible)
    return min_jumps_required if min_jumps_required != float('inf') else -1

def mul(iterable):
    prod = iterable[0]
    for i in iterable[1:]:
        prod = prod * i
    return prod
 
def min_product_tuple(list_of_tuples):
    """
    Calculate the minimum product from pairs of tuples in a list.

    Args:
        list_of_tuples (list): A list of tuples, where each tuple contains two integers.

    Returns:
        int: The smallest product among all tuple pairs.
    """
    # Placeholder for the solution
    smallest = mul(list_of_tuples[0])
    for i in list_of_tuples:
        if mul(i) < smallest: smallest = mul(i)
    return smallest

def find_rotations(s: str) -> int:
    """
    Determine the minimum number of rotations required to return the string to its original form.

    Args:
    s (str): The input string.

    Returns:
    int: The minimum number of rotations.
    """
    # Length of the string
    n = len(s)
    
    # Loop through all possible rotations
    for i in range(1, n + 1):
        # Rotate the string by moving the first i characters to the end
        rotated = s[i:] + s[:i]
        
        # Check if the rotated string is the same as the original
        if rotated == s:
            return i
    
    # If no rotation matches, it means the string never returns to its original form
    return n

def move_numbers_to_end(s: str) -> str:
    """
    Move all numeric characters in the string to the end while preserving the order of other characters.

    Args:
        s (str): The input string.

    Returns:
        str: The modified string with numbers moved to the end.
    """
    # Initialize variables to store non-numeric and numeric characters
    non_numeric = []
    numeric = []

    # Iterate through each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Append to numeric list
            numeric.append(char)
        else:
            # Append to non-numeric list
            non_numeric.append(char)

    # Combine non-numeric and numeric characters
    return ''.join(non_numeric) + ''.join(numeric)

def move_zeroes_to_end(lst: list) -> list:
    """
    Moves all zeroes in the list to the end while maintaining the order of non-zero elements.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new list with zeroes moved to the end.
    """
    # Placeholder for the solution
    zeros = 0
    for i in lst:
        if i == 0:
            lst.pop(lst.index(i))
            zeros += 1
    while zeros > 0:
        lst.append(0)
        zeros -= 1
    return lst

def multiply_and_divide(numbers):
    """
    Multiplies all numbers in the list and divides the result by the length of the list.

    Args:
        numbers (list): A list of numbers (int or float).

    Returns:
        float: The result of the operation.
    """
    # Initialize the total product to 1
    total_product = 1
    # Iterate through the list and multiply the numbers
    for num in numbers:
        total_product *= num
    # Divide the total product by the length of the list
    result = total_product / len(numbers)
    return result

def multiply_list_by_index(numbers: list) -> list:
    """
    Multiplies each element in the given list by its index.

    Args:
        numbers (list): The input list of numbers.

    Returns:
        list: A new list with each element multiplied by its index.
    """
    # TODO: Implement the multiply_list_by_index function
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * i
    return numbers

def n_largest_items(lst: List[int], n: int) -> List[int]:
    """
    Returns the n largest items from the list in descending order.

    Args:
    lst (List[int]): The input list of integers.
    n (int): The number of largest items to return.

    Returns:
    List[int]: A list containing the n largest items in descending order.
    """
    # Placeholder for the solution
    lst.sort(reverse=True)
    return lst[:n]

def newman_conway(n: int) -> int:
    """
    Compute the nth number in the Newman-Conway sequence.

    Args:
        n (int): The position in the sequence (1-indexed).

    Returns:
        int: The nth number in the Newman-Conway sequence.
    """
    # Base cases
    if n == 1 or n == 2:
        return 1

    # Recursive case
    # Placeholder for the actual implementation
     # Recursive case: P(n) = P(P(n-1)) + P(n - P(n-1))
    p = [0] * (n + 1)  # Initialize a list to store computed values (1-indexed)
    
    # Base values
    p[1] = 1
    p[2] = 1
    
    # Compute values from 3 to n
    for i in range(3, n + 1):
        p[i] = p[p[i-1]] + p[i - p[i-1]]
    
    return p[n]

def next_perfect_square(n: int) -> int:
    """
    Find the next perfect square greater than the given number.

    Args:
        n (int): The input number.

    Returns:
        int: The next perfect square greater than n.
    """
    # Placeholder for the solution
    perfectSquare = 1
    count = 1
    while perfectSquare <= n:
        count += 1
        perfectSquare = count * count
    return perfectSquare

def next_smallest_palindrome(num: int) -> int:
    """
    Find the next smallest palindrome greater than the given number.
    
    Args:
        num (int): The input number.
    
    Returns:
        int: The next smallest palindrome.
    """
    # A helper function to check if a number is a palindrome
    def is_palindrome(n: int) -> bool:
        return str(n) == str(n)[::-1]
    
    # Start from the next number
    num += 1
    
    # Keep incrementing until a palindrome is found
    while not is_palindrome(num):
        num += 1
    
    return num

def catalan_number(n: int) -> int:
    """
    Compute the nth Catalan number using recursion.
    
    Args:
        n (int): The index of the Catalan number to compute.
    
    Returns:
        int: The nth Catalan number.
    """
    # Base case
    if n == 0:
        return 1

    # Recursive case: C(n) = sum(C(i) * C(n-i-1)) for i = 0 to n-1
    result = 0
    for i in range(n):
        result += catalan_number(i) * catalan_number(n - i - 1)
    
    return result

def centered_hexagonal_number(n: int) -> int:
    """
    Calculate the nth centered hexagonal number.

    Args:
        n (int): The position of the centered hexagonal number to calculate.

    Returns:
        int: The nth centered hexagonal number.
    """
    # Implement the formula for centered hexagonal numbers
    return (3 * n * (n-1) + 1)

def nth_decagonal_number(n):
    """
    Calculate the nth decagonal number.

    Args:
        n (int): The position of the decagonal number to calculate.

    Returns:
        int: The nth decagonal number.
    """
    # Implement the formula for the nth decagonal number
    return (4 * pow(n, 2) - 3 * n)

def hexagonal_num(n: int) -> int:
    """
    Calculate the nth hexagonal number.

    Args:
        n (int): The position of the hexagonal number to calculate.

    Returns:
        int: The nth hexagonal number.
    """
    # Implement the formula for the nth hexagonal number
    return (n * ((2 * n) - 1))

def find_lucas(n: int) -> int:
    """
    Compute the n-th Lucas number using recursion.

    Args:
        n (int): The index of the Lucas number to compute.

    Returns:
        int: The n-th Lucas number.
    """
    # Base cases
    # Add recursive logic here
    sequence = [2, 1]
    while len(sequence) <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[n]

def nth_octagonal_number(n: int) -> int:
    """
    Calculate the nth octagonal number.

    Args:
    n (int): The position of the octagonal number to calculate.

    Returns:
    int: The nth octagonal number.
    """
    # Implement the formula for the nth octagonal number
    return (3 * pow(n, 2) - 2 * n)

def nth_power(nums: list, n: int) -> list:
    """
    Compute the n-th power of each number in the list.

    Args:
        nums (list): A list of integers.
        n (int): The power to which each number should be raised.

    Returns:
        list: A list of integers where each element is raised to the n-th power.
    """
    # Replace the following line with your implementation
    return [pow(x, n) for x in nums]

def find_star_num(n: int) -> int:
    """
    Calculate the N'th star number.

    Args:
        n (int): The position of the star number to calculate.

    Returns:
        int: The N'th star number.
    """
    # Implement the formula for the N'th star number
    return (6 * n * (n-1) + 1)

def tetrahedral_number(n: int) -> int:
    """
    Calculate the nth tetrahedral number.

    Args:
        n (int): The position of the tetrahedral number to calculate.

    Returns:
        int: The nth tetrahedral number.
    """
    # Implement the formula for the nth tetrahedral number
    return ((n * (n+1) * (n+2)) / 6)

def pack_consecutive_duplicates(input_list: list) -> list:
    """
    Groups consecutive duplicate elements in the input list into sublists.
    
    Args:
        input_list (list): The list of elements to process.
    
    Returns:
        list: A list of sublists, where each sublist contains consecutive duplicates.
    """
    if not input_list:
        return []

    # Initialize the result list and a temporary sublist
    result = []
    current_sublist = [input_list[0]]
    
    # Loop through the input list starting from the second element
    for i in range(1, len(input_list)):
        if input_list[i] == input_list[i - 1]:
            # If the current element is the same as the previous one, append it to the sublist
            current_sublist.append(input_list[i])
        else:
            # If different, add the current sublist to the result and start a new sublist
            result.append(current_sublist)
            current_sublist = [input_list[i]]
    
    # Add the last sublist after the loop
    result.append(current_sublist)
    
    return result

def add_pairwise(test_tup: tuple) -> tuple:
    """
    Compute the pairwise addition of neighboring elements in the tuple.

    Args:
        test_tup (tuple): A tuple of integers.

    Returns:
        tuple: A tuple containing the pairwise sums of neighboring elements.
    """
    # Placeholder for the solution
    pairwise_sums = []
    
    # Iterate through the tuple to compute the pairwise sums
    for i in range(len(test_tup) - 1):
        pairwise_sums.append(test_tup[i] + test_tup[i + 1])
    
    # Return the result as a tuple
    return tuple(pairwise_sums)

def flip(nums, k):
    """
    Reverses the first k elements of the list.
    
    Args:
        nums (list): The list of integers.
        k (int): The index up to which to flip (1-based).
    
    Returns:
        list: The list after flipping the first k elements.
    """
    nums[:k] = nums[:k][::-1]
    return nums

def pancake_sort(nums):
    """
    Sorts a list of integers using the pancake sorting algorithm.
    
    Args:
        nums (list): A list of integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    """
    n = len(nums)
    
    # Perform the pancake sort
    for size in range(n, 1, -1):
        # Find the index of the maximum element in the unsorted portion
        max_idx = nums.index(max(nums[:size]))
        
        # If the max element is not already in the correct position
        if max_idx != size - 1:
            # Flip the max element to the front if it's not already at the front
            if max_idx != 0:
                flip(nums, max_idx + 1)
            
            # Flip the max element to its correct position
            flip(nums, size)
    
    return nums

def partition(n, step, seq):
    """
    Partitions the sequence into sublists of n elements, stepping forward step steps each time.

    Args:
    n: The number of elements in each sublist.
    step: The number of steps to move forward each time.
    seq: The input sequence.

    Returns:
    list: The list of sublists.
    """
    # TODO: Implement the partition function
    values = []
    start = 0
    while start+n <= len(seq):
        values.append(seq[start:start+n])
        start += step
    return values

def extract_phone_numbers(str) -> list:
    """
    Extracts phone numbers from a given string using regex.

    Args:
        string (str): The input string.

    Returns:
        list: A new list with the extracted phone numbers.
    """
    # TODO: Implement the extract_phone_numbers function
    numFilter = r"\+?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}"
    return re.findall(numFilter, str)


def polar_to_rectangular(r, theta):
    """
    Convert polar coordinates to rectangular coordinates.

    Parameters:
        r (float): Radial distance.
        theta (float): Angle in radians.

    Returns:
        tuple: Rectangular coordinates (x, y).
    """
    # Calculate x and y using trigonometric functions
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    x = round(x, 2)
    y = round(y, 2)

    return (x, y)

def positive_ratio(nums: list) -> float:
    """
    Calculate the ratio of positive numbers in the list.

    Args:
        nums (list): A list of integers.

    Returns:
        float: The ratio of positive numbers rounded to two decimal places.
    """
    # Placeholder for the solution
    pos = 0
    for i in nums:
        if i > 0:
            pos += 1
    return round(pos/len(nums), 2)

def mul_even_odd(numbers: list) -> int:
    """
    Returns the product of the first even and first odd number in the list.
    If either is not found, returns -1.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The product of the first even and first odd number, or -1.
    """
    # Placeholder for the solution
    value = -1
    firstOdd = firstEven = 0
    oddPresent = evenPresent = False
    for i in numbers:
        if i % 2 == 0 and firstEven == 0:
            firstEven = i
            evenPresent = True
        elif i % 2 == 1 and firstOdd == 0:
            firstOdd = i
            oddPresent = True
    if evenPresent and oddPresent:
        value = firstEven * firstOdd
    return value

def calculate_product(numbers):
    """
    Calculates the product of all elements in the given list.

    Args:
        numbers (list): The input list of numbers.

    Returns:
        int: The product of all elements.
    """
    # TODO: Implement the calculate_product function
    value = 1
    for x in numbers:
        value = value * x
    return value

def re_arrange_array(arr, n):
    """
    Re-arranges the first n elements of the array so that all negative elements
    appear before positive ones, preserving their relative order.

    Parameters:
    arr (list): The input array of integers.
    n (int): The number of elements to consider for re-arrangement.

    Returns:
    list: The modified array with the first n elements re-arranged.
    """
    temp_negatives = []
    positives = []
    
    # Separate the first n elements into negatives and positives
    for i in range(n):
        if arr[i] < 0:
            temp_negatives.append(arr[i])
        else:
            positives.append(arr[i])

    # Concatenate the negative elements followed by the positive elements
    arr[:n] = temp_negatives + positives

    return arr

def multiply_int(x: int, y: int) -> int:
    """
    Recursively multiply two integers without using the multiplication operator.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The product of x and y.
    """
    # Base cases and recursive logic to be implemented
    if y == 0:
        return 0
    
    elif y > 0:
        return x + multiply_int(x, y-1)
    elif y < 0:
        return -x + multiply_int(x, y+1)
    

def find_literals(text: str, pattern: str) -> tuple:
    """
    Searches for a regex pattern in a given string and returns the match details.

    Args:
        text (str): The string to search within.
        pattern (str): The regex pattern to search for.

    Returns:
        tuple: A tuple containing the matching substring, start index, and end index.
    """
    # Perform regex search
    matches = re.search(pattern, text)
    
    # If there's no match, return None
    if matches is None:
        return None
    
    # Return the matching substring and its start and end indices
    return (text[matches.span()[0]:matches.span()[1]], matches.span()[0], matches.span()[1])

def area_polygon(sides: int, length: float) -> float:
    """
    Calculate the area of a regular polygon.

    Args:
        sides (int): The number of sides of the polygon.
        length (float): The length of each side.

    Returns:
        float: The area of the polygon.
    """
    # Placeholder for the solution
    return ((sides * math.pow(length, 2)) / (4 * math.tan(math.pi / sides)))

def remove_dirty_chars(string1: str, string2: str) -> str:
    """
    Remove all characters from string1 that are present in string2.

    Args:
        string1 (str): The original string.
        string2 (str): The string containing characters to remove from string1.

    Returns:
        str: The modified string after removing characters.
    """
    return ''.join([char for char in string1 if char not in string2])

def consecutive_duplicates(nums: list) -> list:
    """
    Remove consecutive duplicate elements from the list.

    Args:
        nums (list): The input list containing elements.

    Returns:
        list: A new list with consecutive duplicates removed.
    """
    # Placeholder for the solution
    if not nums:
        return []
    values = [nums[0]]
    for i in nums[1:]:
        if i != values[-1]:
            values.append(i)
    return values

def remove_duplicates(nums: list) -> list:
    """
    Remove duplicate numbers from the given list, preserving the order of first occurrences.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list with duplicates removed.
    """
    # Placeholder for the solution
    value = []
    for i in nums:
        if i not in value:
            value.append(i)
    return value

def remove_elements(list1: list, list2: list) -> list:
    """
    Removes all elements from list1 that are present in list2.

    Args:
        list1 (list): The list to filter.
        list2 (list): The list containing elements to remove from list1.

    Returns:
        list: A new list with elements from list1 not in list2.
    """
    # Write your code here
    return [nums for nums in list1 if nums not in list2]

def remove_occurrences(s: str, ch: str) -> str:
    """
    Removes the first and last occurrence of the character `ch` from the string `s`.

    Args:
        s (str): The input string.
        ch (str): The character to remove.

    Returns:
        str: The modified string with the first and last occurrence of `ch` removed.
    """
    # Implement the function logic here
        # Find the index of the first occurrence of the character `ch`
    first_index = s.find(ch)
    
    # Find the index of the last occurrence of the character `ch`
    last_index = s.rfind(ch)
    
    # If either the first or last occurrence is not found, return the original string
    if first_index == -1 or last_index == -1:
        return s
    
    # Remove the first and last occurrence by slicing the string
    return s[:first_index] + s[first_index+1:last_index] + s[last_index+1:]


def remove_kth_element(lst: list, k: int) -> list:
    """
    Remove the k'th element from the list.

    Args:
        lst (list): The input list.
        k (int): The 1-based index of the element to remove.

    Returns:
        list: A new list with the k'th element removed.
    """
    # Check if k is within the valid range
    # Implement the logic to remove the k'th element
    if len(lst) < k or k <= 0:
        return lst
    else:
        lst.pop(k-1)
        return lst

def remove_leading_zeroes(ip: str) -> str:
    """
    Removes leading zeroes from each segment of an IP address.

    Args:
        ip (str): The input IP address as a string.

    Returns:
        str: The IP address with leading zeroes removed.
    """
    # Replace this with the implementation
    arr = ip.split('.')
    for i in range(len(arr)):
        arr[i] = arr[i].strip('0')
        if arr[i] == '':
            arr[i] = '0'
    return '.'.join(arr)

def remove_lowercase(input_string: str) -> str:
    """
    Removes all lowercase alphabetic characters from the input string.

    Args:
        input_string (str): The string to process.

    Returns:
        str: The string with lowercase characters removed.
    """
    # Replace this comment with your implementation
    return ''.join([char for char in re.findall("[A-Z]", input_string)])

def remove_nested(input_tuple):
    """
    Remove all nested tuples from the given tuple.

    Args:
        input_tuple (tuple): The input tuple containing elements.

    Returns:
        tuple: A new tuple with all nested tuples removed.
    """
    # Initialize an empty tuple to store the result
    result = ()
    # Iterate through each element in the input tuple
    for element in input_tuple:
        # Check if the element is not a tuple
        if not isinstance(element, tuple):
            # Add the element to the result tuple
            result += (element,)
    # Return the result tuple
    return result

def remove_parentheses(text):
    """
    Remove all parentheses and their contents from the given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with parentheses and their contents removed.
    """
    # Use regex to replace anything inside parentheses (including the parentheses themselves) with an empty string
    return re.sub("  ", " ", re.sub(r'\([^)]*\)', '', text).strip())

def remove_length(input_string: str, k: int) -> str:
    """
    Remove all words of length k from the input string.

    Args:
    input_string (str): The input string containing words.
    k (int): The length of words to remove.

    Returns:
    str: The modified string with specified words removed.
    """

    return ' '.join([word for word in input_string.split(" ") if len(word) != k])

def replace_specialchar(text: str) -> str:
    """
    Replace all occurrences of spaces, commas, or dots in the input text with a colon.

    Args:
        text (str): The input string.

    Returns:
        str: The modified string with specified characters replaced by colons.
    """
    # Use a regular expression to find and replace the specified characters
    return re.sub("[., ]", ":", text)

def replace_spaces(text: str) -> str:
    """
    Replace whitespaces with underscores and underscores with whitespaces in the given string.

    Args:
        text (str): The input string.

    Returns:
        str: The modified string with whitespaces and underscores swapped.
    """
    # Initialize an empty list to store the modified characters
    result = []

    # Iterate through each character in the input string
    for char in text:
        if char == " ":
            result.append("_")  # Replace space with underscore
        elif char == "_":
            result.append(" ")  # Replace underscore with space
        else:
            result.append(char)  # Keep other characters as is

    # Join the list back into a string and return it
    return ''.join(result)


def reverse_array_upto_k(arr, k):
    """
    Reverse the first k elements of the array.

    Args:
        arr (list): The input list of elements.
        k (int): The number of elements to reverse from the start.

    Returns:
        list: A new list with the first k elements reversed.
    """
    # Placeholder for the solution
    for i in range(int(k/2)):
        temp = arr[i]
        arr[i] = arr[k-i-1]
        arr[k-i-1] = temp
    return arr

def reverse_string(string1: str) -> str:
    return string1[::-1]

def reverse_string_list(stringlist):
    """
    Reverses each string in the given list of strings.

    Args:
        stringlist (list of str): A list of strings to be reversed.

    Returns:
        list of str: A new list with each string reversed.
    """
    reverseList = []
    for i in stringlist:
        reverseList.append(reverse_string(i))
    return reverseList

def reverse_vowels(s: str) -> str:
    """
    Reverse only the vowels in the input string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with vowels reversed.
    """
    # Define vowels
    vowels = "aeiouAEIOU"
    # Placeholder for solution
    vowel_positions = [i for i, char in enumerate(s) if char in vowels]
    vowel_chars = [s[i] for i in vowel_positions]
    
    # Reverse the list of vowels
    vowel_chars.reverse()
    
    # Convert the string to a list (since strings are immutable)
    s_list = list(s)
    
    # Replace the vowels in the original string with the reversed vowels
    for i, pos in enumerate(vowel_positions):
        s_list[pos] = vowel_chars[i]
    
    # Join the list back into a string
    return ''.join(s_list)

def reverse_words(s: str) -> str:
    """
    Reverse the order of words in the input string.

    Args:
    s (str): The input string containing words separated by spaces.

    Returns:
    str: A new string with the words in reversed order.
    """
    # Split the string into words, reverse the list of words, and join them back.
    temp = s.split(" ")
    value = ""
    for i in reversed(temp):
        value = value + i + " "
    return value.strip()

def rgb_to_hsv(r, g, b):
    """
    Convert RGB color values to HSV.

    Parameters:
    r (int): Red component (0-255)
    g (int): Green component (0-255)
    b (int): Blue component (0-255)

    Returns:
    tuple: (h, s, v) where h is hue (0-360), s is saturation (0-100), and v is value (0-100).
    """
    # Normalize RGB values to the range 0-1
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Find the maximum and minimum values of r, g, b
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val

    # Calculate Hue (H)
    if delta == 0:
        h = 0  # If no difference, it's a shade of gray
    elif max_val == r:
        h = (60 * ((g - b) / delta) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    else:
        h = (60 * ((r - g) / delta) + 240) % 360

    # Calculate Saturation (S)
    if max_val == 0:
        s = 0  # If max_val is 0, saturation is 0
    else:
        s = (delta / max_val) * 100

    # Calculate Value (V)
    v = max_val * 100

    return (h, s, v)

def right_insertion(a: list, x: any) -> int:
    """
    Determine the right insertion point for x in the sorted list a.

    Args:
        a (list): A sorted list of elements.
        x (any): The value to find the insertion point for.

    Returns:
        int: The index where x should be inserted to maintain sorted order.
    """
    # Use the bisect module to find the right insertion point
    return bisect.bisect_right(a, x)
    
def left_rotate(n, d):
    """
    Rotate the bits of a 32-bit integer n to the left by d positions.

    Args:
    n (int): The number to rotate.
    d (int): The number of positions to rotate.

    Returns:
    int: The result of the left rotation.
    """
    # Define the number of bits in the integer
    INT_BITS = 32
    
    # Normalize d to be within the 32-bit range
    d = d % INT_BITS

    # Perform the left rotation
    rotated = ((n << d) & 0xFFFFFFFF) | (n >> (INT_BITS - d))

    return rotated

def rotate_right(lst, m):
    """
    Rotates the list `lst` to the right by `m` positions.

    Args:
        lst (list): The list to rotate.
        m (int): The number of positions to rotate.

    Returns:
        list: The rotated list.
    """
    # Handle the case when the list is empty or m is 0
    if not lst or m == 0:
        return lst
    
    # Normalize m to be within the length of the list
    m = m % len(lst)
    
    # Rotate the list by slicing
    return lst[-m:] + lst[:-m]

def second_smallest(numbers):
    """
    Find the second smallest unique number in a list.

    Args:
        numbers (list): A list of numbers (integers or floats).

    Returns:
        float or int or None: The second smallest unique number, or None if not applicable.
    """
    # Remove duplicates and sort the list
    # Check if there are at least two unique numbers
    # Return the second smallest unique number or None
    numbers.sort()
    numbers = remove_duplicates(numbers)
    if len(numbers) < 2:
        return None
    else:
        return numbers[1]

def sector_area(radius: float, angle: float) -> float|None:
    """
    Calculate the area of a sector of a circle.

    Parameters:
    radius (float): The radius of the circle.
    angle (float): The angle of the sector in degrees.

    Returns:
    float or None: The area of the sector, or None if the angle is invalid.
    """
    # Check if the angle is valid
    if angle > 360:
        return None
    # Placeholder for the calculation
    area = math.pi * pow(radius, 2)
    return (area * (angle / 360))

def shell_sort(my_list: list[int]) -> list[int]:
    """
    Sorts a list of integers in ascending order using the Shell Sort algorithm.

    Args:
        my_list (list[int]): The list of integers to sort.

    Returns:
        list[int]: The sorted list.
    """
    n = len(my_list)
    gap = n // 2  # Initial gap size

    while gap > 0:
        # Perform a gapped insertion sort
        for i in range(gap, n):
            temp = my_list[i]
            j = i
            # Shift elements of my_list[0..i-gap], that are greater than temp, to one position ahead
            while j >= gap and my_list[j - gap] > temp:
                my_list[j] = my_list[j - gap]
                j -= gap
            my_list[j] = temp
        
        gap //= 2  # Reduce the gap size

    return my_list

def find_min_length(lst: list[list]) -> int:
    """
    Find the length of the smallest list in a list of lists.

    Args:
        lst (list of lists): A list containing sublists.

    Returns:
        int: The length of the smallest sublist, or 0 if the input list is empty.
    """
    # Check if the input list is empty
    if not lst:
        return 0

    # Placeholder for the solution
    smallest = len(lst[0])
    for i in lst[1:]:
        if len(i) < smallest:
            smallest = len(i)
    return smallest

def find_smallest_missing(arr: list) -> int:
    """
    Find the smallest missing number in a sorted list of natural numbers.

    Args:
        arr (list): A sorted list of non-negative integers.

    Returns:
        int: The smallest missing number.
    """
    # Implement the binary search logic here
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return len(arr)

def next_power_of_2(n):
    """
    Find the smallest power of 2 greater than or equal to n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The smallest power of 2 greater than or equal to n.
    """
    if n == 0:
        return 1
    
    # If n is already a power of 2, return it
    if (n & (n - 1)) == 0:
        return n
    
    # Find the next power of 2 greater than n using bit manipulation
    return 1 << (n.bit_length())

def find_index(n):
    """
    Find the index of the smallest triangular number with exactly n digits.

    Args:
        n (int): The number of digits.

    Returns:
        int: The index of the smallest triangular number with n digits.
    """
    index = 1
    while True:
        # Calculate the triangular number T_index
        triangular_number = index * (index + 1) // 2
        
        # Check if the number of digits of triangular_number is equal to n
        if len(str(triangular_number)) == n:
            return index
        
        index += 1

def snake_to_camel(snake_str: str) -> str:
    """
    Convert a snake_case string to CamelCase.

    Args:
        snake_str (str): The input string in snake_case format.

    Returns:
        str: The converted string in CamelCase format.
    """
    # Split the string by underscores and capitalize each part
    # Join the parts together to form the CamelCase string
    temp = snake_str.split("_")
    camel_str = ""
    for i in temp:
        camel_str += i[0].capitalize() + i[1:]
    return camel_str

def sort_dict_by_value(input_dict: dict[str, int]) -> List[Tuple[str, int]]:
    """
    Sorts a dictionary by its values in descending order.

    Args:
        input_dict (dict[str, int]): The dictionary to sort.

    Returns:
        List[Tuple[str, int]]: A list of tuples sorted by values in descending order.
    """
    # Sort the dictionary items by value in descending order
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_items

def comb_sort(nums: list) -> list:
    """
    Sorts a list of elements using the Comb Sort algorithm.

    Args:
        nums (list): A list of comparable elements.

    Returns:
        list: The sorted list in ascending order.
    """
    # Placeholder for the implementation of the Comb Sort algorithm
    n = len(nums)
    gap = n
    shrink_factor = 1.3  # Shrinking factor
    sorted_flag = False

    while not sorted_flag:
        # Calculate the next gap
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        # Perform a pass with the current gap
        for i in range(n - gap):
            j = i + gap
            if nums[i] > nums[j]:
                # Swap the elements
                nums[i], nums[j] = nums[j], nums[i]
                sorted_flag = False  # We made a swap, so it's not fully sorted yet

    return nums

def sort_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Sorts a matrix in ascending order based on the sum of its rows.

    Args:
        matrix (list of list of int): The input 2D list.

    Returns:
        list of list of int: The sorted matrix.
    """
    # Sort the matrix based on the sum of each row
    return sorted(matrix, key=sum)

def sort_numeric_strings(nums_str: list[str]) -> list[int]:
    """
    Sort a list of numeric strings numerically.

    Args:
        nums_str (list of str): A list of strings representing numbers.

    Returns:
        list of int: A list of integers sorted numerically.
    """
    # Convert strings to integers, sort them, and return the sorted list
    return sorted([int(x) for x in nums_str])

def sort_sublists(list_of_lists: list[list[str]]) -> list[list[str]]:
    """
    Sort each sublist of strings in a given list of lists.

    Args:
        list_of_lists (list of list of str): A list containing sublists of strings.

    Returns:
        list of list of str: A new list with each sublist sorted.
    """
    # Implement the function here
    return ([sorted(x) for x in list_of_lists])

def sort_by_second_value(data: list[tuple]) -> list[tuple]:
    """
    Sort a list of tuples based on the second value of each tuple.

    Args:
        data (list of tuple): A list of tuples to be sorted.

    Returns:
        list of tuple: A new list of tuples sorted by the second value.
    """
    # Implement the sorting logic here
    return sorted(data, key=lambda x: x[1])

def split_and_rearrange(lst: list, n: int) -> list:
    """
    Splits the list at the nth index and rearranges it such that the first part is moved to the end.

    Args:
        lst (list): The input list to be rearranged.
        n (int): The index at which to split the list.

    Returns:
        list: The rearranged list.
    """
    # Implement the function logic here
    return (lst[n:] + lst[:n])

def list_split(S: list, step: int) -> list[list]:
    """
    Splits the list S into sublists, where each sublist contains every step-th element.

    Args:
        S (list): The input list to be split.
        step (int): The step value for splitting.

    Returns:
        list: A list of sublists.
    """
    # Initialize a list of empty sublists
    result = [[] for _ in range(step)]
    
    # Distribute elements from the original list into the sublists
    for i, element in enumerate(S):
        result[i % step].append(element)
    
    return result

def split_lists(lst: list[list]) -> list[list]:
    """
    Splits a list of sublists into two separate lists.

    Args:
        lst (list): A list of sublists, where each sublist contains exactly two elements.

    Returns:
        list: A list containing two lists, one with the first elements and one with the second elements.
    """
    # Your code here
    return [[x[0] for x in lst], [x[1] for x in lst]]

def calculate_surface_area(base_edge: float, slant_height: float) -> float:
    """
    Calculate the surface area of a square pyramid.

    Args:
        base_edge (float): The length of the base edge of the pyramid.
        slant_height (float): The slant height of the pyramid.

    Returns:
        float: The surface area of the square pyramid.
    """
    # Implement the formula for the surface area of a square pyramid
    return (pow(base_edge, 2) + (2 * base_edge * slant_height))

def calculate_square_root(numbers: list) -> list:
    """
    Calculates the square root of each element in the given list.

    Args:
        numbers (list): The input list of numbers.

    Returns:
        list: A new list with the square root of each element.
    """
    # TODO: Implement the calculate_square_root function
    return [math.sqrt(x) for x in numbers]

def sub(first, *args):
    """
    Subtracts all the arguments (except the first one) from the first argument and returns the result.

    Args:
    first: The first argument.
    *args: The additional arguments.

    Returns:
    int or float: The result of the subtraction.
    """
    # TODO: Implement the sub function
    total = first
    for i in args:
        total = total - i
    return total

def difference(n: int) -> int:
    """
    Calculate the difference between the sum of the cubes of the first n natural numbers
    and the sum of the first n natural numbers.

    Args:
    n (int): A positive integer.

    Returns:
    int: The calculated difference.
    """
    # Placeholder for the solution
    if n == 0:
        return 0
    else:
        return (difference(n-1) + (pow(n, 3) - n))

def digit_distance_nums(n1, n2):
    """
    Calculate the sum of the absolute differences of corresponding digits between two integers.

    Args:
        n1 (int): The first integer.
        n2 (int): The second integer.

    Returns:
        int: The sum of the absolute differences of corresponding digits.
    """
    # Convert both numbers to strings
    str_n1 = str(n1)
    str_n2 = str(n2)
    
    # Pad the shorter string with leading zeros
    max_len = max(len(str_n1), len(str_n2))
    str_n1 = str_n1.zfill(max_len)
    str_n2 = str_n2.zfill(max_len)
    
    # Calculate the sum of absolute differences of corresponding digits
    total_difference = sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str_n1, str_n2))
    
    return total_difference

def sum_digits(n: int) -> int:
    """
    Calculate the sum of the digits of a non-negative integer using recursion.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The sum of the digits of the input integer.
    """
    # Base case: If n is 0, return 0
    # Recursive case: Add the last digit to the sum of the digits of the rest of the number
    str_n = str(n)
    total = 0
    for i in str_n:
        total += int(i)
    return total

def sum_of_even_factors(n: int) -> int:
    """
    Calculate the sum of all even factors of a given number.

    Args:
    n (int): The number to find even factors for.

    Returns:
    int: The sum of all even factors of n.
    """
    # Placeholder for the solution
    even_sum = 0
    
    # Loop through possible divisors from 1 to sqrt(n)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            # i is a divisor, check if it's even
            if i % 2 == 0:
                even_sum += i
            # Check the corresponding divisor n // i (if it's different from i)
            if i != n // i:
                if (n // i) % 2 == 0:
                    even_sum += n // i
    
    return even_sum

def even_binomial_coeff_sum(n: int) -> int:
    """
    Calculate the sum of binomial coefficients at even indices for (x + y)^n.

    Args:
    n (int): A positive integer.

    Returns:
    int: The sum of the binomial coefficients at even indices.
    """
    total = 0
    
    # Iterate over even indices: 0, 2, 4, ..., up to n
    for i in range(0, n + 1, 2):
        # Binomial coefficient C(n, i) = n! / (i! * (n-i)!)
        total += math.comb(n, i)  # math.comb efficiently computes C(n, i)
    
    return total

def sum_even_and_even_index(arr: list[int]) -> int:
    """
    Calculate the sum of even numbers at even indices in the list.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The sum of even numbers at even indices.
    """
    # Initialize the sum to 0
    total = 0
    # Iterate through the list
    for i in range(0, len(arr), 2):
        if (arr[i]) % 2 == 0:
            total += arr[i]
    # Placeholder for the solution
    return total

def sum_fourth_power_of_odds(n: int) -> int:
    """
    Calculate the sum of the fourth powers of the first n odd natural numbers.

    Args:
        n (int): The number of odd natural numbers to consider.

    Returns:
        int: The sum of the fourth powers of the first n odd natural numbers.
    """
    # Initialize the sum
    total = 0
    # Iterate over the first n odd numbers
    for i in range(1, n + 1):
        # Placeholder for the logic to calculate the fourth power and add to total
        total += pow(((i*2) - 1), 4)
    return total

def sum_uppercase_names_length(names: list[str]) -> int:
    """
    Calculate the sum of the lengths of names starting with an uppercase letter.

    Args:
        names (list): A list of strings representing names.

    Returns:
        int: The sum of the lengths of valid names.
    """
    # Filter the names to include only those starting with an uppercase letter
    # Calculate the sum of the lengths of the filtered names
    return sum([len(x) for x in names if x[0].isupper()])

def sum_non_repeated_elements(nums: list) -> int:
    """
    Calculate the sum of all non-repeated elements in the list.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The sum of all non-repeated elements.
    """
    # Placeholder for the implementation
    badValues = []
    values = []
    for i in nums:
        if i not in values:
            values.append(i)
        else:
            badValues.append(i)
    return sum([x for x in values if x not in badValues])

def sum_in_range(l: int, r: int) -> int:
    """
    Calculate the sum of all odd natural numbers within the inclusive range [l, r].

    Args:
    l (int): The lower bound of the range.
    r (int): The upper bound of the range.

    Returns:
    int: The sum of all odd natural numbers within the range.
    """
    # Placeholder for the solution
    return sum([x for x in range(l, r+1) if x%2 == 1])

def get_divisors(n: int) -> list[int]:
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def sum_of_common_divisors(a, b):
    """
    Calculate the sum of all common divisors of two given positive integers a and b.

    Args:
    a (int): The first positive integer.
    b (int): The second positive integer.

    Returns:
    int: The sum of all common divisors of a and b.
    """

    # Placeholder for the solution
    return sum([x for x in get_divisors(a) if x in get_divisors(b)])

def sum_of_digits(nums: list) -> int:
    """
    Calculate the sum of digits of all numbers in the given list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of all digits in the list.
    """
    # Initialize the sum
    total_sum = 0
    # Iterate through the list
    for num in nums:
        if type(num) == int:
            temp = str(abs(num))
            for i in range(len(temp)):
                total_sum += int(temp[i])
    return total_sum

def power_base_sum(base: int, power: int) -> int:
    """
    Calculate the sum of all digits of the number obtained by raising `base` to the power of `power`.

    Args:
        base (int): The base number.
        power (int): The exponent.

    Returns:
        int: The sum of the digits of the result.
    """
    # Calculate the power result
    # Convert the result to a string and iterate through its digits
    # Sum the digits and return the result
    return sum_of_digits([pow(base, power)])

def div_sum(n: int) -> int:
    """
    Calculate the sum of divisors of a given number, excluding the number itself.
    
    Args:
        n (int): The number to calculate divisors for.
    
    Returns:
        int: The sum of divisors of the number, excluding the number itself.
    """
    divisors = []
    for i in range(1, abs(n)):  # Now we exclude the number itself
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def are_equivalent(num1: int, num2: int) -> bool:
    """
    Determine if the sum of divisors of two numbers are equivalent.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
    
    Returns:
        bool: True if the sum of divisors of num1 and num2 are equivalent, False otherwise.
    """
    return div_sum(num1) == div_sum(num2)

def sum_of_divisors(n: int) -> int:
    """
    Calculate the sum of all divisors of a given positive integer n.

    Args:
    n (int): A positive integer.

    Returns:
    int: The sum of all divisors of n.
    """
    # Placeholder for the solution
    return (div_sum(n) + n)

def sum_range_list(lst: list, start: int, end: int) -> int:
    """
    Calculate the sum of elements in a list within a specified range.

    Args:
        lst (list): The list of integers.
        start (int): The starting index (inclusive).
        end (int): The ending index (inclusive).

    Returns:
        int: The sum of the elements in the specified range.
    """
    # Placeholder for the solution
    return sum([x for x in lst[start:end+1]])

def is_sum_of_powers_of_two(n: int) -> bool:
    """
    Determine if the given number can be represented as a sum of distinct non-zero powers of 2.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number can be represented as a sum of distinct non-zero powers of 2, False otherwise.
    """
    # Placeholder for the solution
    return n >= 0

def sum_of_squares_of_even_numbers(n: int) -> int:
    """
    Calculate the sum of squares of the first n even natural numbers.

    Args:
        n (int): The number of even natural numbers to consider.

    Returns:
        int: The sum of squares of the first n even natural numbers.
    """
    # Placeholder for the solution
    return sum([pow(2 * i, 2) for i in range(1, n + 1)])

def sum_of_squares_of_odds(n: int) -> int:
    """
    Calculate the sum of the squares of the first n odd natural numbers.

    Args:
        n (int): The number of odd natural numbers to consider.

    Returns:
        int: The sum of the squares of the first n odd natural numbers.
    """
    return sum([pow((x * 2) - 1, 2) for x in range(1, n+1)])

def sum_of_xor_pairs(numbers: List[int]) -> int:
    """
    Calculate the sum of XOR of all unique pairs in the list.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The sum of XOR of all unique pairs.
    """
    result = 0
    # Loop through each unique pair in the list
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            result += numbers[i] ^ numbers[j]
    
    return result

def sum_series(n: int) -> int:
    """
    Calculate the sum of the series n + (n-2) + (n-4) + ... until the term is <= 0.

    Args:
    n (int): The starting number of the series.

    Returns:
    int: The sum of the series.
    """
    if n <= 0:
        return 0
    else:
        return (n + sum_series(n-2))

def calculate_sum_of_squares(numbers: list) -> int:
    """
    Calculates the sum of squares of all elements in the given list.

    Args:
        numbers (list): The input list of numbers.

    Returns:
        int: The sum of squares of all elements.
    """
    # TODO: Implement the calculate_sum_of_squares function
    return sum([pow(x, 2) for x in numbers])

def area_tetrahedron(side: float) -> float:
    """
    Calculate the surface area of a regular tetrahedron given the side length.

    Args:
        side (float): The length of a side of the tetrahedron.

    Returns:
        float: The surface area of the tetrahedron.
    """
    # Placeholder for the implementation
    return (math.sqrt(3) * pow(side, 2))

def trim_tuple(tuple_list: list[tuple], k: int) -> list[tuple]:
    """
    Trims each tuple in the list by removing k elements from both ends.

    Args:
    tuple_list (list of tuples): The list of tuples to be trimmed.
    k (int): The number of elements to remove from both ends.

    Returns:
    list of tuples: A new list with trimmed tuples.
    """
    # Initialize the result list
    result = []
    # Iterate over each tuple in the list
    for t in tuple_list:
        # Trim the tuple by removing k elements from both ends
        trimmed_tuple = t[k:-k] if len(t) > 2 * k else ()  # Avoid empty tuples if not enough elements
        result.append(trimmed_tuple)
    # Return the result list
    return result

def extract_column(tuples: list[tuple], index: int) -> list:
    """
    Extract a specific column from a list of tuples.

    Args:
        tuples (list of tuple): The input list of tuples.
        index (int): The index of the column to extract.

    Returns:
        list: A list containing the elements at the specified index from each tuple.
    """
    # Placeholder for the solution
    return [t[index] for t in tuples if index < len(t)]

def subtract_elements(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Subtracts corresponding elements of two tuples.

    Args:
        tuple1 (tuple): The first tuple of numbers.
        tuple2 (tuple): The second tuple of numbers.

    Returns:
        tuple: A tuple containing the results of the subtraction.
    """
    # Implement the subtraction logic here
    return tuple(x - y for x, y in zip(tuple1, tuple2))

def tuple_modulo(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Perform element-wise modulo operation between two tuples of the same length.

    Args:
        tuple1 (tuple): The first tuple of integers.
        tuple2 (tuple): The second tuple of integers.

    Returns:
        tuple: A tuple containing the modulo results.
    """
    # Ensure the tuples are of the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length.")

    # Placeholder for the solution
    return tuple(x % y for x, y in zip(tuple1, tuple2))

def count_tuple_occurrences(input_list):
    """
    Count the occurrences of unique tuples in the input list, treating tuples
    with reversed elements as equivalent.

    Args:
        input_list (list of tuples): A list containing tuples of integers.

    Returns:
        dict: A dictionary mapping each unique tuple (with reversed elements) to its count.
    """
    # Reverse each tuple in the list before counting
    reversed_tuples = [tuple(sorted(t)) for t in input_list]
    
    # Use Counter to count occurrences of each tuple in the reversed list
    return dict(Counter(reversed_tuples))

def index_multiplication(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Perform index-wise multiplication of tuple elements in the given two tuples.

    Args:
        tuple1 (tuple of tuples): The first tuple of tuples.
        tuple2 (tuple of tuples): The second tuple of tuples.

    Returns:
        tuple of tuples: A new tuple of tuples with index-wise multiplied elements.
    """
    # Initialize the result tuple
    result = tuple(tuple(x * y for x, y in zip(t1, t2)) for t1, t2 in zip(tuple1, tuple2))
    
    return result

def multiply_elements(input_tuple: tuple) -> tuple:
    """
    Given a tuple of numbers, return a new tuple where each element is the product
    of consecutive elements in the input tuple.

    Args:
    input_tuple (tuple): A tuple of numbers.

    Returns:
    tuple: A tuple containing the products of consecutive elements.
    """
    # Initialize an empty list to store the products
    result = []
    
    # Loop through the tuple and multiply consecutive elements
    for i in range(len(input_tuple) - 1):
        result.append(input_tuple[i] * input_tuple[i + 1])
    
    # Return the result as a tuple
    return tuple(result)

def find_combinations(tuple_list: list[tuple]) -> list[tuple]:
    """
    Given a list of tuples, return a list of tuples representing the sum of corresponding elements
    from all possible pairs of tuples in the input list.

    Args:
    tuple_list (list of tuples): A list of tuples, where each tuple contains two integers.

    Returns:
    list of tuples: A list of tuples with summed elements.
    """
    # Placeholder for the solution
    # List to store the result
    result = []
    
    # Generate all pairs of tuples
    for t1, t2 in combinations(tuple_list, 2):
        # Sum corresponding elements of the tuples
        summed_tuple = (t1[0] + t2[0], t1[1] + t2[1])
        result.append(summed_tuple)
    
    return result

def tuple_to_dict(input_tuple: tuple) -> dict:
    """
    Given a tuple, return a dictionary where the keys are the first elements of pairs, 
    and the values are the sum of the second elements of all pairs with the same key.

    Args:
    input_tuple (tuple): A tuple containing pairs of values.

    Returns:
    dict: A dictionary where the key is the first element of the pair and the value 
          is the sum of the second elements of all pairs with the same key.
    """
    result = {}
    
    # Loop through the tuple in steps of 2 (pairs)
    for i in range(0, len(input_tuple), 2):
        key = input_tuple[i]  # First element of the pair
        value = input_tuple[i+1]  # Second element of the pair
        
        # Add the value to the corresponding key in the result dictionary
        if key in result:
            result[key] += value  # Add to the existing value
        else:
            result[key] = value  # Initialize with the first value
    
    return result

def tuple_to_int(nums: tuple) -> int:
    """
    Convert a tuple of positive integers into a single integer by concatenating the digits.

    Args:
        nums (tuple): A tuple of positive integers.

    Returns:
        int: The concatenated integer.
    """
    # Placeholder for the solution
    return int("".join([str(x) for x in nums]))

def union_elements(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Returns a tuple containing the sorted union of elements from tuple1 and tuple2.

    Args:
    tuple1 (tuple): First input tuple.
    tuple2 (tuple): Second input tuple.

    Returns:
    tuple: A tuple containing the sorted union of elements.
    """
    # Combine the tuples, remove duplicates, and sort the result
    value = tuple1 + tuple2
    return tuple(sorted(remove_duplicates(value)))

def find_unique_element(arr: list) -> int:
    """
    Given a list where every element appears twice except for one element that appears once,
    find and return the unique element.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The unique element that appears only once.
    """
    unique_element = 0
    
    # XOR all elements in the list
    for num in arr:
        unique_element ^= num  # XOR the current number with the running result
    
    return unique_element
            
def find_unique_elements(lst: list) -> list:
    """
    Finds the unique elements in a given list.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the unique elements.
    """
    # TODO: Implement the find_unique_elements function
    value = []
    for i in lst:
        if i not in value:
            value.append(i)
    return value

def unique_product(list_data: list) -> int:
    """
    Calculate the product of unique numbers in the given list.

    Args:
        list_data (list): A list of integers.

    Returns:
        int: The product of unique numbers.
    """
    # Convert the list to a set to remove duplicates
    data = set(list_data)
    # Initialize the product to 1
    product = 1
    # Iterate through the unique numbers and calculate the product
    for i in data:
        product = product * i
    return product

def find_unique_characters(string: str) -> str:
    """
    Finds the unique characters in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: A new string with the unique characters.
    """
    return "".join([char for i, char in enumerate(string) if char not in string[:i]])

def count_unique_tuples(lst: list) -> int:
    """
    Count the number of unique tuples in the list.
    Two tuples are considered the same if they contain the same elements, regardless of order.

    Args:
        lst (list): A list of tuples.

    Returns:
        int: The number of unique tuples.
    """
    # Convert each tuple into a sorted tuple, and add it to a set to ensure uniqueness
    unique_tuples = {tuple(sorted(t)) for t in lst}
    
    # Return the count of unique tuples
    return len(unique_tuples)

def is_decimal(num: str) -> bool:
    """
    Check if the given string is a valid decimal number with up to two decimal places.

    Args:
        num (str): The string to check.

    Returns:
        bool: True if the string is a valid decimal number, False otherwise.
    """
    # Define the regular expression pattern for a valid decimal number
    expression = r"^\d+(\.\d{1,2})?$"
    # Placeholder for the solution
    return None != re.search(expression, num)

def text_lowercase_underscore(text: str) -> bool:
    """
    Check if the input string contains sequences of lowercase letters joined by an underscore.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string matches the pattern, False otherwise.
    """
    # Define the pattern for lowercase letters joined by an underscore
    pattern = r'^[a-z]+_[a-z]+$'  # TODO: Add the correct regex pattern
    # Check if the pattern matches the input text
    return None != re.search(pattern, text)

def count_word_frequency(file_path: str):
    """
    Counts the frequency of each word in a file, considering case sensitivity and punctuation.
    Two words are considered the same if they match exactly (including case).

    Args:
        file_path (str): The path to the input file.

    Returns:
        dict: A dictionary containing the word frequency.
    """
    # Open the file and read the contents
    with open(file_path, "r") as file:
        text = file.read()

    # Remove unwanted characters (strip extra punctuation but leave useful punctuation like !, ?)
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s!.,?;\'"-]', '', text)

    # Split the cleaned text into words
    words = cleaned_text.split()

    # Use Counter to count the frequency of each word
    word_frequency = Counter(words)

    return dict(word_frequency)

def zero_to_nonzero_ratio(nums: list) -> float:
    """
    Calculate the ratio of zeroes to non-zeroes in a list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        float: The ratio of zeroes to non-zeroes, or float('inf') if no non-zeroes exist.
    """
    # Count the number of zeroes and non-zeroes
    zero_count = 0
    nonzero_count = 0

    # Iterate through the list to count zeroes and non-zeroes
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            nonzero_count += 1

    # Calculate and return the ratio
    if nonzero_count == 0:
        return float('inf')
    else:
        return zero_count/nonzero_count

def create_dictionary(keys: list, values: list) -> dict:
    """
    Creates a dictionary by combining elements from two lists.

    Args:
        keys (list): The list of keys.
        values (list): The list of values.

    Returns:
        dict: A dictionary created by pairing the elements from both lists.
    """
    # TODO: Implement the create_dictionary function
    return {key: value for key, value in zip(keys, values)}

def myzip(*lists: list) -> list:
    """
    Zips an arbitrary number of lists together and returns the zipped list.

    Args:
    *lists: The input lists.

    Returns:
    list: The zipped list.
    """
    return [list(x) for x in zip(*lists)]

def zipwith(f, *lists: list) -> list:
    """
    Applies a function to the corresponding elements of the given lists and returns a list of the results.

    Args:
    f: The function to apply.
    *lists: The input lists.

    Returns:
    list: The list of results.
    """
    return [f(*x) for x in zip(*lists)]

def add(*args) -> int|float:
    """
    Adds an arbitrary number of arguments together and returns the sum.

    Args:
    *args: The input arguments.

    Returns:
    int or float: The sum of all the arguments.
    """
    # TODO: Implement the add function
    return sum(args)

def add_dict_to_tuple(test_tup: tuple, test_dict: dict) -> tuple:
    """
    Add a dictionary to the end of a tuple.

    Args:
        test_tup (tuple): The original tuple.
        test_dict (dict): The dictionary to add.

    Returns:
        tuple: A new tuple with the dictionary added.
    """
    # Your code here
    return test_tup + (test_dict,)

def capital_words_spaces(input_string: str) -> str:
    """
    Insert spaces between words starting with capital letters in the given string.

    Args:
        input_string (str): The input string containing words without spaces.

    Returns:
        str: A new string with spaces inserted between capitalized words.
    """
    # Use a regular expression to identify the pattern and insert spaces
    return "".join([(x + " ") for x in re.findall(r"[A-Z][a-z]*", input_string)]).strip()

def get_adjacent_coordinates(coord: tuple) -> list:
    """
    Given a tuple representing a coordinate in a 2D grid, return a list of all adjacent coordinates.

    Args:
    coord (tuple): A tuple of two integers representing the coordinate.

    Returns:
    list: A list of tuples representing adjacent coordinates.
    """
    x, y = coord  # Unpack the coordinate into x and y
    adjacent_coords = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),  # Diagonal and above
        (x - 1, y),                   (x + 1, y),       # Left and Right
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)     # Diagonal and below
    ]
    return adjacent_coords

def angle_of_complex(real: float, imag: float) -> float:
    """
    Calculate the angle (phase) of a complex number given its real and imaginary parts.

    Args:
        real (float): The real part of the complex number.
        imag (float): The imaginary part of the complex number.

    Returns:
        float: The angle (in radians) of the complex number.
    """
    # Create the complex number from real and imaginary parts
    # Use cmath.phase to calculate the angle
    return cmath.phase(complex(real, imag))

def add_lists(test_list: list, test_tup: tuple) -> tuple:
    """
    Append the elements of test_list to test_tup and return the resulting tuple.

    Args:
    test_list (list): The list of elements to append.
    test_tup (tuple): The tuple to which elements will be appended.

    Returns:
    tuple: A new tuple containing elements of test_tup followed by elements of test_list.
    """
    # Combine the tuple and list into a new tuple
    return test_tup + tuple(test_list)

def apply_format_to_list(elements: list, format_string: str) -> list:
    """
    Apply a format string to each element in a list.

    Args:
        elements (list): A list of elements to format.
        format_string (str): A format string containing a single `{}` placeholder.

    Returns:
        list: A new list with the formatted strings.
    """
    # Replace the following line with your implementation
    return [re.sub("{}", str(x), format_string) for x in elements]

def is_armstrong_number(number: int) -> bool:
    """
    Determine if the given number is an Armstrong number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Placeholder for the solution
    return number == sum([pow(int(x), len(str(number))) for x in str(number)])

def intersection_array(array_nums1: list, array_nums2: list) -> list:
    """
    Find the intersection of two arrays.

    Args:
        array_nums1 (list): The first list of integers.
        array_nums2 (list): The second list of integers.

    Returns:
        list: A list containing the intersection of the two input lists.
    """
    # Your code here
    return ([x for x in array_nums1 if x in array_nums2])

def average_tuple(nums: tuple) -> list:
    """
    Calculate the average value for each position across all tuples.

    Args:
        nums (tuple of tuples): A tuple containing tuples of numerical values.

    Returns:
        list: A list of average values for each position.
    """
    # Placeholder for the solution
    total = [0] * len(nums[0])  # Assuming all tuples have the same length
    
    # Sum the values in corresponding positions
    for t in nums:
        for i in range(len(t)):
            total[i] += t[i]
    
    # Calculate the average by dividing the sum by the number of tuples
    num_tuples = len(nums)
    return [x / num_tuples for x in total]

def babylonian_squareroot(number: float, tolerance: float = 1e-6) -> float:
    """
    Compute the square root of a number using the Babylonian method.

    Args:
        number (float): The number to compute the square root of.
        tolerance (float): The precision of the result.

    Returns:
        float: The approximated square root.
    """
    # Handle the edge case for zero
    if number == 0:
        return 0.0

    # Initial guess
    guess = number / 2.0

    # Iterative process
    while True:
        # Compute the next guess
        next_guess = 0.5 * (guess + number / guess)

        # Check if the difference between the guess and next guess is within the tolerance
        if abs(guess - next_guess) < tolerance:
            break

        # Update guess
        guess = next_guess

    # Return the computed square root
    return guess

def bitwise_xor(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Perform bitwise XOR operation between corresponding elements of two tuples.

    Args:
        tuple1 (tuple): The first tuple of integers.
        tuple2 (tuple): The second tuple of integers.

    Returns:
        tuple: A tuple containing the XOR results.
    """
    # Ensure that the tuples have the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length.")

    # Perform the bitwise XOR operation for each corresponding element
    result = tuple(a ^ b for a, b in zip(tuple1, tuple2))

    return result

def power(a: int, b: int) -> int:
    """
    Calculate the value of 'a' raised to the power of 'b' using recursion.

    Args:
    a (int): The base number.
    b (int): The exponent.

    Returns:
    int: The result of a^b.
    """
    # Base cases
    if b == 0:
        return 1
    elif a == 0:
        return 0
    return (a * power(a, b-1))

def wind_chill(v: float, t: float) -> int:
    """
    Calculate the wind chill index given wind velocity and temperature.

    Args:
        v (float): Wind velocity in km/h.
        t (float): Temperature in Celsius.

    Returns:
        int: The wind chill index rounded to the nearest integer.
    """
    # Placeholder for the wind chill calculation
    return int(13.12 + 0.6215 * t - 11.37 * pow(v, 0.16) + 0.3965 * t * pow(v, 0.16))

def contains_a_followed_by_bbs(text: str) -> bool:
    """
    Check if the string contains 'a' followed by exactly two or three 'b' characters.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the pattern exists, False otherwise.
    """
    # Write your implementation here
    return bool(re.search(r"a[b]{2,3}(?!b)", text))

from collections import deque

def check_expression(expression: str) -> bool:
    """
    Check if the given expression has balanced parentheses, curly braces, and square brackets.

    Args:
        expression (str): The input string containing parentheses, curly braces, and square brackets.

    Returns:
        bool: True if the expression has balanced parentheses, False otherwise.
    """
    # Initialize a stack to keep track of opening parentheses
    stack = deque()

    # Create a mapping of closing brackets to their corresponding opening brackets
    matching_bracket = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # Iterate through each character in the expression
    for char in expression:
        # If it's an opening bracket, push it onto the stack
        if char in "({[":
            stack.append(char)
        # If it's a closing bracket, check for a matching opening bracket
        elif char in ")}]":
            if not stack or stack.pop() != matching_bracket[char]:
                return False

    # If the stack is empty, all brackets are matched
    return len(stack) == 0

def all_bits_unset_in_range(n: int, l: int, r: int) -> bool:
    """
    Check if all bits in the binary representation of n are unset within the range [l, r].

    Args:
    n (int): The number to check.
    l (int): The starting position of the range (1-based).
    r (int): The ending position of the range (1-based).

    Returns:
    bool: True if all bits in the range are unset, False otherwise.
    """
    # Create a mask that has 1's in the positions [l, r]
    mask = ((1 << (r - l + 1)) - 1) << (l - 1)
    
    # Check if the bits in the range [l, r] are all unset
    return (n & mask) == 0

def check_consecutive(lst: list) -> bool:
    """
    Check if the given list contains consecutive numbers.

    Args:
    lst (list): A list of integers.

    Returns:
    bool: True if the list contains consecutive numbers, False otherwise.
    """
    # If the list is empty or has only one element, it's trivially consecutive
    if len(lst) <= 1:
        return True

    # Sort the list
    lst.sort()

    # Check if each number is exactly 1 more than the previous one
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1] + 1:
            return False

    return True

def check_value(dictionary: dict, value: any) -> bool:
    """
    Check if all values in the dictionary are equal to the specified value.

    Args:
        dictionary (dict): The dictionary to check.
        value (any): The value to compare against.

    Returns:
        bool: True if all values are equal to the specified value, False otherwise.
    """
    # Implement the function logic here
    for i in dictionary.values():
        if i != value:
            return False
    return True

def contains_duplicates(nums: list) -> bool:
    """
    Determine if the list contains any duplicate elements.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if duplicates exist, False otherwise.
    """
    # Placeholder for the solution
    temp = []
    for i in nums:
        if i in temp:
            return True
        else:
            temp.append(i)
    return False

def check_equal_tuple_lengths(tuples_list: list) -> bool:
    """
    Determine if all tuples in the list have the same length.

    Args:
        tuples_list (list): A list of tuples.

    Returns:
        bool: True if all tuples have the same length, False otherwise.
    """
    if len(tuples_list) == 0:
        return True
    length = len(tuples_list[0])
    for i in tuples_list[1:]:
        if len(i) != length:
            return False
    return True

def has_even_divisors_count(n: int) -> bool:
    """
    Determines whether the count of divisors of n is even.

    Args:
        n (int): A positive integer.

    Returns:
        bool: True if the count of divisors is even, False otherwise.
    """
    # Placeholder for the solution
    return bool(len(get_divisors(n)) % 2 == 0)

def even_position(nums: list) -> bool:
    """
    Check if every even index in the list contains an even number.

    Args:
    nums (list): A list of integers.

    Returns:
    bool: True if all even indices contain even numbers, False otherwise.
    """
    # Placeholder for the solution
    for i in range(0, len(nums), 2):
        if nums[i] % 2 != 0:
            return False
    return True

def check_integer(text: str) -> bool:
    """
    Check if the given string represents a valid integer.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a valid integer, False otherwise.
    """
    # Strip any leading or trailing whitespace
    text = text.strip()
    # Placeholder for implementation
    return bool(re.match(r"^[+-]?[0-9]+$", text))

def check_min_heap(arr):
    """
    Check if the given array represents a min heap.

    Args:
        arr (list): The array representation of a binary tree.

    Returns:
        bool: True if the array represents a min heap, False otherwise.
    """
    n = len(arr)
    
    # Check each node except the leaves (since leaves don't have children)
    for i in range((n // 2) - 1, -1, -1):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        
        # Check if left child exists and if it violates the heap property
        if left_child_index < n and arr[i] > arr[left_child_index]:
            return False
        
        # Check if right child exists and if it violates the heap property
        if right_child_index < n and arr[i] > arr[right_child_index]:
            return False
    
    return True

def is_monotonic(arr: list) -> bool:
    """
    Determine if the given array is monotonic.

    Args:
        arr (list): The input list of integers.

    Returns:
        bool: True if the array is monotonic, False otherwise.
    """
    # Placeholder for the solution
    increasing = False
    decreasing = False
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i+1]:
            pass
        elif arr[i] < arr[i+1]:
            increasing = True
        elif arr[i] > arr[i+1]:
            decreasing = True
    if increasing and decreasing:
        return False
    else:
        return True

def check_greater(arr: list, number: int) -> bool:
    """
    Check if the given number is greater than all elements in the array.

    Args:
        arr (list): A list of integers.
        number (int): An integer to compare against the array elements.

    Returns:
        bool: True if the number is greater than all elements, False otherwise.
    """
    # Handle the case of an empty array
    if len(arr) == 0:
        return True
    # Sort the array to find the largest element
    arr.sort()
    # Compare the number with the largest element
    return bool(number > arr[-1])

def find_parity(x):
    """
    Determine if the parity of the binary representation of x is odd.

    Args:
        x (int): The input integer.

    Returns:
        bool: True if the parity is odd, False otherwise.
    """
    # Count the number of 1-bits in the binary representation of x
    return bin(x).count('1') % 2 == 1

def check_number_relation(n: int) -> bool:
    """
    Determines if the given number is one less than twice its reverse.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the condition is met, False otherwise.
    """
    # Helper function to reverse the digits of a number
    def reverse_number(num: int) -> int:
    # Flag to handle negative numbers
        is_negative = num < 0
        num = abs(num)
        
        reversed_num = 0
        
        while num != 0:
            # Extract the last digit and add it to the reversed number
            reversed_num = reversed_num * 10 + num % 10
            num //= 10  # Remove the last digit
        
        # Reapply the negative sign if needed
        if is_negative:
            reversed_num = -reversed_num
        
        return reversed_num

    # Placeholder for main logic
    return n + 1 == 2 * reverse_number(n)

def odd_position(nums: list) -> bool:
    """
    Check if every odd index in the list contains an odd number.

    Args:
    nums (list): A list of integers.

    Returns:
    bool: True if all odd indices contain odd numbers, False otherwise.
    """
    # Implement the function logic here
    for i in range(1, len(nums), 2):
        if nums[i] % 2 != 1:
            return False
    return True

def differ_at_one_bit(a: int, b: int) -> bool:
    """
    Determine if two integers differ at exactly one bit position.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    bool: True if they differ at exactly one bit position, False otherwise.
    """
    # XOR the two numbers, and check if the result has exactly one '1' bit.
    return (a ^ b) != 0 and (a ^ b) & ((a ^ b) - 1) == 0

def opposite_signs(x: int, y: int) -> bool:
    """
    Check if two integers have opposite signs.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        bool: True if x and y have opposite signs, False otherwise.
    """
    # Implement the logic to check for opposite signs
    return (x * y) < 0

def overlapping(seq1: list|tuple, seq2: list|tuple) -> bool:
    """
    Check if any value in seq1 exists in seq2.

    Args:
        seq1: The first sequence.
        seq2: The second sequence.

    Returns:
        bool: True if any value in seq1 exists in seq2, otherwise False.
    """
    # Implement the logic to check for overlapping elements
    for i in seq1:
        if i in seq2: return True
    return False

def is_samepatterns(colors: list, patterns: list) -> bool:
    """
    Check if the sequence in colors follows the sequence in patterns.

    Args:
    colors (list): A list of strings representing colors.
    patterns (list): A list of strings representing patterns.

    Returns:
    bool: True if the sequence in colors follows the sequence in patterns, False otherwise.
    """
    # Maps to store the correspondence between colors and patterns
    if len(colors) != len(patterns):
        return False
    
    color_to_pattern = {}
    pattern_to_color = {}
    
    for color, pattern in zip(colors, patterns):
        # Check if this color already has a different pattern
        if color in color_to_pattern and color_to_pattern[color] != pattern:
            return False
        # Check if this pattern already has a different color
        if pattern in pattern_to_color and pattern_to_color[pattern] != color:
            return False
        
        # Otherwise, establish the mappings
        color_to_pattern[color] = pattern
        pattern_to_color[pattern] = color
        
    return True

def is_perfect_square(n: int) -> bool:
    """
    Determine if the given number is a perfect square.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if n is a perfect square, False otherwise.
    """
    # Placeholder for the solution
    i = 0
    while pow(i, 2) <= n:
        if pow(i, 2) == n:
            return True
        i += 1
    return False

def is_prime(n: int) -> bool:
    """
    Determine if the given integer is a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    # Implement the logic to check for prime numbers
    divisors = get_divisors(n)
    return bool(len(divisors) == 2)

def is_product_even(arr: list) -> bool:
    """
    Determine if the product of all numbers in the list is even.

    Args:
        arr (list): A list of integers.

    Returns:
        bool: True if the product is even, False otherwise.
    """
    for i in arr:
        if i % 2 == 0:
            return True
    return False

def check_char(string: str) -> str:
    """
    Check if the given string starts and ends with the same character.

    Args:
    string (str): The input string to check.

    Returns:
    str: "Valid" if the string starts and ends with the same character, "Invalid" otherwise.
    """
    # Implement the function logic here
    if string[0] == string[-1]:
        return "Valid"
    else:
        return "Invalid"

def check_str(string):
    """
    Check if the given string starts with a vowel using regex.

    Args:
        string (str): The input string to check.

    Returns:
        bool: True if the string starts with a vowel, False otherwise.
    """
    # Define the regex pattern for a string starting with a vowel
    pattern = r'^[aeiouAEIOU]'
    # Use re.match to check the pattern
    return bool(re.match(pattern, string))

def is_sublist(main_list: list, sub_list: list) -> bool:
    """
    Check if sub_list is a sublist of main_list.

    Args:
        main_list (list): The main list to check within.
        sub_list (list): The list to check as a sublist.

    Returns:
        bool: True if sub_list is a sublist of main_list, False otherwise.
    """
    # Placeholder for the solution
        # Handle edge cases
    if not sub_list:
        return True  # An empty list is always a sublist
    if len(sub_list) > len(main_list):
        return False  # If sub_list is longer than main_list, it's impossible to be a sublist
    
    # Iterate through main_list and check for a matching subsequence
    for i in range(len(main_list) - len(sub_list) + 1):
        if main_list[i:i + len(sub_list)] == sub_list:
            return True
    return False

def find_substring(strings: list[str], substring: str) -> bool:
    """
    Check if a substring is present in any string within a list.

    Args:
        strings (list of str): The list of strings to search within.
        substring (str): The substring to search for.

    Returns:
        bool: True if the substring is found in any string, False otherwise.
    """
    # Implement the function logic here
    for i in strings:
        if substring in i:
            return True
    return False

def check_smaller(test_tup1: tuple, test_tup2: tuple) -> bool:
    """
    Check if each element of the second tuple is smaller than its corresponding element in the first tuple.

    Args:
    test_tup1 (tuple): The first tuple of integers.
    test_tup2 (tuple): The second tuple of integers.

    Returns:
    bool: True if all elements in test_tup2 are smaller than their counterparts in test_tup1, False otherwise.
    """
    # Implement the function logic here
    if len(test_tup1) != len(test_tup2):
        return False
    for i in range(len(test_tup1)):
        if test_tup1[i] <= test_tup2[i]:
            return False
    return True

def check_type(test_tuple: tuple) -> bool:
    """
    Check if all elements in the tuple have the same data type.

    Args:
    test_tuple (tuple): The tuple to check.

    Returns:
    bool: True if all elements have the same data type, False otherwise.
    """
    # Placeholder for the solution
    if len(test_tuple) == 0:
        return True
    types = type(test_tuple[0])
    for i in test_tuple[1:]:
        if type(i) != types:
            return False
    return True

def is_undulating(n: int) -> bool:
    """
    Check if the given number is undulating.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is undulating, False otherwise.
    """
    # Convert the number to a string for easier manipulation
    n = str(n)
    
    # If the number has fewer than two digits, it's not undulating
    if len(n) < 2:
        return False
    
    # Check if the number alternates between two different digits
    for i in range(1, len(n)):
        if n[i] == n[i - 1]:  # If two consecutive digits are the same
            return False
    
    # Check if the pattern alternates between exactly two distinct digits
    distinct_digits = set(n)
    return len(distinct_digits) == 2

def is_woodall(n: int) -> bool:
    """
    Check if the given number is a Woodall number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a Woodall number, False otherwise.
    """
    # Implement the function logic here
    a = 1
    woodNum = lambda a: (a * pow(2, a)) - 1

    while woodNum(a) <= n:
        if woodNum(a) == n:
            return True
        a += 1
    return False

def common_element(list1: list, list2: list) -> bool:
    """
    Check if two lists have at least one common element.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        bool: True if there is at least one common element, False otherwise.
    """
    # Placeholder for the solution
    return bool([x for x in list1 if x in list2])

def common_in_nested_lists(nestedlist: list[list[int]]) -> list[int]:
    """
    Find the common elements in all nested lists.

    Args:
        nestedlist (list of list of int): A list containing nested lists of integers.

    Returns:
        list of int: A list of integers that are common to all nested lists.
    """
    if not nestedlist:
        return []

    # Start with the set of the first sublist
    common_elements = set(nestedlist[0])

    # Iterate over the remaining sublists and take the intersection
    for sublist in nestedlist[1:]:
        common_elements &= set(sublist)

    # Return the common elements as a sorted list
    return list(common_elements)

def concatenate_tuple(elements: tuple) -> str:
    """
    Concatenate elements of a tuple into a single string separated by a hyphen.

    Args:
        elements (tuple): A tuple containing elements of any type.

    Returns:
        str: A string with all elements concatenated, separated by a hyphen.
    """
    # Implement the function logic here
    return "".join([(str(x) + "-") for x in elements]).strip("-")

def volume_of_cone(radius: float, height: float) -> float:
    """
    Calculate the volume of a cone given its radius and height.

    Args:
        radius (float): The radius of the cone's base.
        height (float): The height of the cone.

    Returns:
        float: The volume of the cone.
    """
    # Placeholder for the solution
    return ((1/3) * math.pi * pow(radius, 2) * height)

def pair_wise(lst: list) -> list[tuple]:
    """
    Returns a list of tuples containing consecutive pairs of elements from the input list.

    Args:
    l1 (list): The input list.

    Returns:
    list: A list of tuples with consecutive pairs.
    """
    # Initialize an empty list to store the pairs
    result = []
    # Iterate through the list to form pairs
    for i in range(len(lst) - 1):
        result.append((lst[i], lst[i + 1]))
    # Placeholder for implementation
    return result

def convert_to_polar(complex_number: complex) -> tuple:
    """
    Convert a complex number to its polar coordinates.

    Args:
        complex_number (complex): The complex number to convert.

    Returns:
        tuple: A tuple containing the magnitude and angle in radians.
    """
    # Use cmath.polar to compute the polar coordinates
    return cmath.polar(complex_number)

def change_date_format(dt: str) -> str:
    """
    Convert a date from yyyy-mm-dd format to dd-mm-yyyy format.

    Args:
        dt (str): A date string in the format yyyy-mm-dd.

    Returns:
        str: The date string in the format dd-mm-yyyy.
    """
    # Write your code here
    arr = dt.split("-")
    return "".join([arr[2], "-", arr[1], "-", arr[0]])

def convert_to_floats(data: list[list]) -> list[list]:
    """
    Convert all convertible elements in a list of lists to floats.

    Args:
        data (list of lists): A list containing sublists with string elements.

    Returns:
        list of lists: A new list of lists with convertible elements converted to floats.
    """
    # Initialize the result list
    result = []
    
    # Iterate through each sublist
    for sublist in data:
        # Process each element in the sublist
        converted_sublist = []
        for element in sublist:
            try:
                # Attempt to convert the element to a float
                converted_sublist.append(float(element))
            except ValueError:
                # If the element cannot be converted, append it as is
                converted_sublist.append(element)
        
        # Append the processed sublist to the result
        result.append(converted_sublist)
    
    return result

def convert_list_dictionary(l1: list, l2: list, l3: list) -> list[dict]:
    """
    Convert three lists into a list of nested dictionaries.

    Args:
        l1 (list): List of keys for the outer dictionary.
        l2 (list): List of keys for the inner dictionary.
        l3 (list): List of values for the inner dictionary.

    Returns:
        list: A list of nested dictionaries.
    """
    # Implement the function logic here
    result = []
    
    # Iterate through each element of l1 to form the outer dictionary
    for i in range(len(l1)):
        outer_dict = {l1[i]: {}}
        # The inner dictionary will have a key from l2[i] and a corresponding value from l3[i]
        outer_dict[l1[i]][l2[i]] = l3[i]
        result.append(outer_dict)
    
    return result

def tuple_str_to_int(tuple_str: str) -> tuple:
    """
    Convert a string representation of a tuple into an actual tuple of integers.

    Args:
    tuple_str (str): A string representation of a tuple.

    Returns:
    tuple: A tuple of integers.
    """
    # Write your code here
    return tuple([int(x.strip()) for x in tuple_str.strip("()").split(",")])

def count_inversions(arr):
    """
    Count the number of inversions in the array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The number of inversions in the array.
    """
    # Initialize the inversion count
    inversion_count = 0

    # Implement the logic to count inversions
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversion_count += 1
    # Placeholder for the solution

    return inversion_count

def is_sorted(arr: list) -> bool:
    """
    Check if the list is sorted in ascending order.

    Parameters:
    arr (list): The list to check.

    Returns:
    bool: True if the list is sorted, False otherwise.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def count_rotations(arr: list) -> int:
    """
    Determine the number of rotations required to sort the array.

    Args:
        arr (list): A rotated version of a sorted array.

    Returns:
        int: The number of rotations required to sort the array.
    """
    n = len(arr)
    
    # Edge case: if the array is empty or has only one element, no rotation is needed
    if n == 0:
        return 0

    # If the array is already sorted, no rotation is needed
    if is_sorted(arr):
        return 0
    
    # Now, perform a linear search to find the point where the sorted order is broken
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return i

    return 0

def count_char_position(input_string: str) -> int:
    """
    Count the number of characters in the string that occur at the same position
    in the string as in the English alphabet (case insensitive).

    Args:
    input_string (str): The input string to evaluate.

    Returns:
    int: The count of characters matching the condition.
    """
    # Initialize the count variable
    count = 0

    # Iterate through the string and check the condition
    for i, char in enumerate(input_string):
        # Convert the character to lowercase to ensure case insensitivity
        char = char.lower()

        # Only check alphabetic characters
        if 'a' <= char <= 'z':
            # Calculate the position of the character in the alphabet
            alphabet_position = ord(char) - ord('a') + 1
            
            # Compare the alphabet position with the 1-based index of the string
            if alphabet_position == i + 1:
                count += 1

    # Return the final count
    return count

def count_vowel_neighbors(s: str) -> int:
    """
    Count characters in the string that have vowels as their neighbors.

    Args:
        s (str): The input string.

    Returns:
        int: The count of characters with vowels as neighbors.
    """
    # Define the set of vowels (case insensitive)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize count to 0
    count = 0
    #Edge case of array must have 2 letters
    if len(s) < 2:
        return 0
    #check first

    if s[0] not in vowels and s[1] in vowels:
        count += 1
    #check last
    if s[-1] not in vowels and s[-2] in vowels:
        count += 1
    
    # Iterate through the string to check neighbors
    for i in range(1, len(s) - 1):
        if s[i] not in vowels and (s[i-1] in vowels or s[i+1] in vowels):
            count += 1

    return count

def count_divisors(n: int) -> int:
    """
    Calculate the number of divisors of a given positive integer n.

    Args:
    n (int): The integer to find divisors for.

    Returns:
    int: The number of divisors of n.
    """
    # Placeholder for the solution
    return len(get_divisors(n))

def count_element_frequency(lst: list) -> dict:
    """
    Counts the frequency of each element in the given list.

    Args:
    lst (list): The input list.

    Returns:
    dict: A dictionary containing the frequency of each element.
    """
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

def count_first_elements(test_tup: tuple) -> int:
    """
    Count the number of elements before the first tuple element in the given tuple.

    Args:
    test_tup (tuple): The input tuple.

    Returns:
    int: The count of elements before the first tuple element.
    """
    # Iterate through the tuple and find the first tuple element
    # Replace the following line with your implementation
    count = 0
    for i in test_tup:
        if isinstance(i, tuple):  # Check if the element is a tuple
            return count  # Return count if a tuple is found
        count += 1
    return len(test_tup)  # Return count if no tuple is found

def count_occurrences(tup: tuple, lst: list) -> int:
    """
    Count the occurrences of elements from the list in the tuple.

    Parameters:
    tup (tuple): The tuple to search within.
    lst (list): The list of elements to count in the tuple.

    Returns:
    int: The total count of elements from the list found in the tuple.
    """
    return len([x for x in tup if x in lst])

def count_samepair(list1: list, list2: list, list3: list) -> int:
    """
    Count the number of items that are identical and in the same position across three lists.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        int: The count of identical items in the same position.
    """
    # Initialize the result counter
    result = 0
    # Iterate through the lists and compare items
    for i in range(len(list1)):
        if list1[i] == list2[i] and list2[i] == list3[i]:
            result += 1
    # Placeholder for the solution
    return result

def count_list_occurrences(list_of_lists: list) -> dict:
    """
    Count the occurrences of each sublist in the input list of lists.

    Args:
        list_of_lists (list): A list containing sublists.

    Returns:
        dict: A dictionary where keys are tuples representing sublists and values are their counts.
    """
    # Initialize an empty dictionary to store the counts
    result = {}
    # Iterate through the list of lists
    for sublist in list_of_lists:
        # Convert the sublist to a tuple (tuples are hashable and can be dictionary keys)
        sublist_tuple = tuple(sublist)
        # Update the count in the dictionary
        result[sublist_tuple] = result.get(sublist_tuple, 0) + 1
    # Return the resulting dictionary
    return result

def count_lists_in_tuple(input_tuple: tuple) -> int:
    """
    Count the number of lists present in the given tuple.

    Args:
        input_tuple (tuple): A tuple containing various elements.

    Returns:
        int: The number of lists in the tuple.
    """
    # Initialize a counter for lists
    list_count = 0
    # Iterate through the elements of the tuple
    for element in input_tuple:
        # Check if the element is a list
        if isinstance(element, list):
            # Increment the counter
            list_count += 1
    # Return the count of lists
    return list_count

def count_same_pair(*lists) -> int:
    """
    Count the number of items that are identical and in the same position across multiple lists.

    Args:
        *lists: A variable number of lists.

    Returns:
        int: The count of identical items in the same position across all lists.
    """
    # Initialize the result counter
    result = 0
    # Check the length of the shortest list to avoid IndexError
    min_len = min(len(lst) for lst in lists)
    
    # Iterate through the lists and compare items
    for i in range(min_len):
        # Compare the i-th item of all lists
        if all(lst[i] == lists[0][i] for lst in lists):
            result += 1
    
    return result

def number_of_substrings(s: str) -> int:
    """
    Calculate the number of non-empty substrings of the given string.

    Args:
    s (str): The input string.

    Returns:
    int: The number of non-empty substrings.
    """
    # Placeholder for the solution
    n = len(s)
    return ((n * (n + 1)) / 2)

def count_odd_binary_rotations(binary_string: str, rotations: int) -> int:
    """
    Count the number of odd binary numbers obtained by rotating the binary string.

    Args:
    binary_string (str): The binary string to rotate.
    rotations (int): The number of rotations to perform.

    Returns:
    int: The count of odd binary numbers.
    """
    # Initialize the count of odd numbers
    count = 0
    n = len(binary_string)
    
    # Loop over the number of rotations and check each rotated string
    for i in range(rotations):
        rotated = binary_string[i % n:] + binary_string[:i % n]  # Perform rotation
        if rotated[-1] == '1':  # Check if the last bit is 1 (odd binary number)
            count += 1
    
    return count

def count_odd_xor_pairs(arr: list) -> int:
    """
    Count the number of unique pairs (i, j) such that the XOR of arr[i] and arr[j] is odd.

    Args:
    arr (list): A list of integers.

    Returns:
    int: The count of pairs with an odd XOR value.
    """
    # Placeholder for the solution
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if (arr[i] ^ arr[j]) % 2 == 1:
                count += 1
    return count

def get_pairs_count(arr: list, target_sum: int) -> int:
    """
    Count the number of unique pairs in the list whose sum equals the target_sum.

    Args:
    arr (list): List of integers.
    target_sum (int): The target sum for the pairs.

    Returns:
    int: The number of pairs whose sum equals target_sum.
    """
    # Initialize a counter for the pairs
    count = 0
    # Placeholder for the solution
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                count += 1
    return count

def count_primes(n: int) -> int:
    """
    Count the number of prime numbers less than a given non-negative integer n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The count of prime numbers less than n.
    """
    # Placeholder for the solution
    count = 0
    i = 0
    while i < n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of a number.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The count of set bits in the binary representation of n.
    """
    return len([x for x in str(bin(n)) if x == '1'])

def count_element_in_list(list1: list[list], x: any) -> int:
    """
    Count the number of sublists in list1 that contain the element x.

    Args:
        list1 (list of list): A list containing sublists.
        x (any): The element to search for in the sublists.

    Returns:
        int: The count of sublists containing the element x.
    """
    # Initialize a counter to zero
    count = 0
    # Iterate through each sublist in the list
    for sublist in list1:
        # Check if the element x is in the current sublist
        if x in sublist:
            # Increment the counter
            count += 1
    # Return the final count
    return count

def count_unequal_pairs(lst: list[int]) -> int:
    """
    Count the number of unordered pairs (i, j) where i < j and lst[i] != lst[j].

    Args:
        lst (list): A list of integers.

    Returns:
        int: The count of such pairs.
    """
    # Initialize the count variable
    count = 0
    # Implement the logic to count the pairs
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            if lst[i] != lst[j]:
                count += 1
    # Placeholder for the solution
    return count

def find_even_pair(A: list) -> int:
    """
    Count the number of pairs of integers in the list A whose XOR results in an even number.

    Args:
    A (list): A list of integers.

    Returns:
    int: The count of pairs whose XOR is even.
    """
    # Initialize the count of pairs
    count = 0
    # Iterate through all pairs in the list
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if ((A[i] ^ A[j]) % 2 == 0):
                count += 1
    # Return the count of such pairs
    return count

def cube_sum_of_evens(n: int) -> int:
    """
    Calculate the sum of the cubes of the first n even natural numbers.

    Args:
        n (int): The number of even natural numbers to consider.

    Returns:
        int: The sum of the cubes of the first n even natural numbers.
    """
    # Initialize the sum
    total = 0
    # Loop through the first n even numbers
    for i in range(2, (n*2) + 1, 2):
        total += pow(i, 3)
    return total

def cumulative_sum(tuple_list: list[tuple]) -> int:
    """
    Calculate the cumulative sum of all values in a list of tuples.

    Args:
        tuple_list (list of tuples): A list where each element is a tuple of integers.

    Returns:
        int: The cumulative sum of all integers in the tuples.
    """
    # Initialize the cumulative sum
    total_sum = 0

    # Iterate through the list of tuples
    for tpl in tuple_list:
        total_sum += sum(tpl)
    return total_sum

def surface_area_cylinder(radius: float, height: float) -> float:
    """
    Calculate the surface area of a cylinder.

    Args:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.

    Returns:
        float: The surface area of the cylinder.
    """
    # Placeholder for the solution
    return ((2 * math.pi * pow(radius, 2)) + (2 * math.pi * radius * height))

def filter_even_values(dictionary: dict) -> dict:
    """
    Filters a dictionary to include only the key-value pairs where the value is an even number.

    Args:
    dictionary (dict): The input dictionary.

    Returns:
    dict: A new dictionary with the filtered key-value pairs.
    """
    return {key: value for key, value in dictionary.items() if value % 2 == 0}

def square_dict_values(dictionary: dict) -> dict:
    """
    Creates a new dictionary where the values are the squares of the original values.

    Args:
    dictionary (dict): The input dictionary.

    Returns:
    dict: A new dictionary with the squared values.
    """
    return {key: pow(value, 2) for key, value in dictionary.items()}

def dict_depth(d: dict) -> int:
    """
    Calculate the depth of a nested dictionary.

    Args:
        d (dict): The dictionary to evaluate.

    Returns:
        int: The depth of the dictionary.
    """
    if not isinstance(d, dict) or not d:
        return 1
    
    max_depth = 1
    for value in d.values():
        if isinstance(value, dict):
            # Recursively calculate the depth of the nested dictionary
            max_depth = max(max_depth, dict_depth(value) + 1)
    
    return max_depth

def isOdd(n: int) -> bool:
    return n % 2 == 1
def isEven(n: int) -> bool:
    return n % 2 == 0

def diff_even_odd(numbers: list) -> int|None:
    """
    Calculate the difference between the first even and first odd number in the list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int or None: The difference between the first even and first odd number, or None if either is not found.
    """
    # Find the first even number
    first_even = None
    # Find the first odd number
    first_odd = None
    for i in numbers:
        if isOdd(i) and first_odd == None:
            first_odd = i
        elif isEven(i) and first_even == None:
            first_even = i
        if first_even and first_odd:
            return (first_even - first_odd)
    return None

def can_be_difference_of_squares(n: int) -> bool:
    """
    Determine if the given number can be represented as the difference of two squares.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number can be represented as the difference of two squares, False otherwise.
    """
    # Placeholder for the solution
    k = 0
    fun = lambda k: (4 * k) + 2
    while (fun(k)) <= n:
        if fun(k) == n:
            return False
        k += 1
    return True

def validate(n: int) -> bool:
    """
    Check whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Args:
        n (int): The input integer.

    Returns:
        bool: True if the condition is met, False otherwise.
    """
    # Convert the integer to its absolute value to handle negatives
def validate(n: int) -> bool:
    """
    Check whether the frequency of each digit in the integer is less than or equal to the digit itself.

    Args:
        n (int): The input integer.

    Returns:
        bool: True if the condition is met, False otherwise.
    """
    # Edge case: If n is 0, return True since 0 appears once, and it satisfies the condition
    if n == 0:
        return True
    
    # Convert the integer to its absolute value to handle negatives
    n = abs(n)
    
    # Convert the integer to a string to easily process each digit
    str_n = str(n)
    
    # Count the frequency of each digit in the string representation
    digit_count = Counter(str_n)
    
    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit, count in digit_count.items():
        if count > int(digit):  # If frequency exceeds the digit's value
            return False
    
    # If all digits satisfy the condition
    return True

def divisible_by_digits(startnum: int, endnum: int) -> list:
    """
    Find numbers in the given range [startnum, endnum] that are divisible by every non-zero digit they contain.

    Args:
    startnum (int): The starting number of the range.
    endnum (int): The ending number of the range.

    Returns:
    list: A list of numbers satisfying the condition.
    """
    value = []
    for i in range(startnum, endnum + 1):  # Include endnum, so use endnum + 1
        num_str = str(i)
        divisible = True
        
        # Check each digit in the number
        for digit in num_str:
            digit_int = int(digit)
            if digit_int != 0 and i % digit_int != 0:  # If it's non-zero and not divisible
                divisible = False
                break
        
        # Exclude numbers with zero digits, they should not be included
        if divisible and '0' not in num_str:
            value.append(i)
    
    return value

def freq_count(elements: list) -> dict:
    """
    Calculate the frequency of each element in the input list.

    Args:
        elements (List): A list of hashable elements.

    Returns:
        Dict: A dictionary with elements as keys and their frequencies as values.
    """
    return dict(Counter(elements))

def element_search(arr: list, element: any) -> tuple:
    """
    Search for an element in the list and return a tuple with a boolean and the index.

    Parameters:
    arr (list): The list to search in.
    element (any): The element to search for.

    Returns:
    tuple: (bool, int) where bool indicates presence and int is the index or -1.
    """
    # Your code here
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)

def div_list(nums1: list, nums2: list) -> list:
    """
    Divides elements of two lists element-wise.

    Args:
        nums1 (list): The first list of numbers.
        nums2 (list): The second list of numbers.

    Returns:
        list: A list containing the element-wise division results.

    Raises:
        ValueError: If the input lists are of different lengths.
        ZeroDivisionError: If division by zero is attempted.
    """
    # Check if the lists have the same length
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must have the same length.")
    
    # Perform element-wise division and handle division by zero
    result = []
    for n1, n2 in zip(nums1, nums2):
        if n2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result.append(n1 / n2)
    
    return result
def division_elements(tuple1: tuple, tuple2: tuple) -> tuple:
    """
    Perform element-wise integer division on two tuples.

    Args:
        tuple1 (tuple): The first tuple of integers.
        tuple2 (tuple): The second tuple of integers.

    Returns:
        tuple: A tuple containing the results of element-wise integer division.
    """
    # Perform element-wise integer division
    # Replace the following line with your implementation
    return tuple(x/y for x, y in zip(tuple1, tuple2))

def and_tuples(test_tup1: tuple, test_tup2: tuple) -> tuple:
    """
    Perform elementwise bitwise AND operation on two tuples.

    Args:
    test_tup1 (tuple): The first tuple of integers.
    test_tup2 (tuple): The second tuple of integers.

    Returns:
    tuple: A tuple containing the result of the bitwise AND operation.
    """
    # Placeholder for the solution
    return tuple(x&y for x, y in zip(test_tup1, test_tup2))

def sub_list(nums1: list, nums2: list) -> list:
    """
    Subtracts elements of nums2 from nums1 element-wise.

    Args:
        nums1 (list): The first list of integers.
        nums2 (list): The second list of integers.

    Returns:
        list: A list containing the element-wise subtraction of nums2 from nums1.
    """
    return [x-y for x, y in zip(nums1, nums2)]