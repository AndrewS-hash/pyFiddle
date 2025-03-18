from imports import *

def add_tuple(test_list: list, test_tup: tuple) -> list:
    """
    Appends the elements of a tuple to a list and returns the resulting list.

    Args:
        test_list (list): The original list.
        test_tup (tuple): The tuple to append.

    Returns:
        list: The list with the tuple elements appended.
    """
    # Your code here
    results = test_list
    for i in test_tup:
        results.append(i)
    return results

def ascii_value(char: str) -> int:
    """
    Returns the ACII value of the given character
    
    Args:
        char (str): A single character
    
    Returns:
        int: the ASCII value of the charater
    """
    return ord(char)

def loss_amount(actual_cost: float, sale_amount: float) -> float:
    """
    Calculate the loss amount on a sale.

    Parameters:
    actual_cost (float): The actual cost of the item.
    sale_amount (float): The sale amount of the item.

    Returns:
    float: The loss amount if sale_amount > actual_cost, otherwise 0.
    """
    # Implement the function logic here
    if sale_amount > actual_cost:
        return sale_amount - actual_cost
    return 0

def is_30_day_month(month_number: int) -> bool:
    """
    Determine if the given month number corresponds to a month with 30 days.

    Args:
        month_number (int): The month number (1 for January, 12 for December).

    Returns:
        bool: True if the month has 30 days, False otherwise.
    """
    # Implement the logic to check if the month has 30 days
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return (days[month_number-1] == 30)

def all_characters_same(s: str) -> bool:
    """
    Check if all characters in the string are the same.

    Args:
        s (str): The input string.

    Returns:
        bool: True if all characters are the same, False otherwise.
    """
    # Placeholder for the solution
    if len(s) <= 1:
        return True
    x = s[0]
    for i in s[1:]:
        if x != i:
            return False
    return True

def check_tuplex(tuplex: tuple, element: any) -> bool:
    """
    Check if an element exists within a tuple.

    Args:
        tuplex (tuple): The tuple to search within.
        element (any): The element to search for.

    Returns:
        bool: True if the element exists in the tuple, False otherwise.
    """
    # Implement the function logic here
    return element in tuplex

def are_all_dicts_empty(dict_list: list[dict]) -> bool:
    """
    Check if all dictionaries in the given list are empty.

    Args:
        dict_list (list): A list of dictionaries.

    Returns:
        bool: True if all dictionaries are empty, False otherwise.
    """
    # Placeholder for the solution
    for i in dict_list:
        if i != {}:
            return False
    return True 

def is_even(n: int) -> bool:
    """
    Check if the given number is even using bitwise operations.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return (n & 1) == 0


def is_dict_empty(input_dict: dict) -> bool:
    """
    Check if the given dictionary is empty.

    Args:
        input_dict (dict): The dictionary to check.

    Returns:
        bool: True if the dictionary is empty, False otherwise.
    """
    # Write your code here
    return input_dict == {}

def is_sorted(lst):
    """
    Check if the given list is sorted in ascending order.

    Args:
        lst (list): The list of numbers to check.

    Returns:
        bool: True if the list is sorted, False otherwise.
    """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def check_element(lst: list, element: any) -> bool:
    """
    Check if all elements in the list are equal to the given element.

    Args:
        lst (list): The list of elements to check.
        element (any): The element to compare against.

    Returns:
        bool: True if all elements in the list are equal to the given element, False otherwise.
    """
    # Implement the function logic here
    for i in lst:
        if element != i:
            return False
    return True

def has_31_days(month_number: int) -> bool:
    """
    Determine if the given month has 31 days.

    Args:
        month_number (int): The month number (1 for January, 12 for December).

    Returns:
        bool: True if the month has 31 days, False otherwise.
    """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month_number - 1] == 31

def noprofit_noloss(actual_cost: int, sale_amount: int) -> bool:
    """
    Check if the sale results in no profit and no loss.

    Parameters:
    actual_cost (int): The actual cost of the item.
    sale_amount (int): The sale amount of the item.

    Returns:
    bool: True if no profit and no loss, False otherwise.
    """
    # Compare actual_cost and sale_amount
    return actual_cost == sale_amount

def unique_element(arr: list) -> bool:
    """
    Check if the list contains only one distinct element.

    Args:
        arr (list): A list of numbers.

    Returns:
        bool: True if the list contains only one distinct element, False otherwise.
    """
    # Your code here
    if len(arr) == 0:
        return False
    x = arr[0]
    for i in arr[1:]:
        if i != x:
            return False
    return True

def check_distinct(test_tup: tuple) -> bool:
    """
    Check if the given tuple contains no duplicate elements.

    Args:
        test_tup (tuple): The tuple to check.

    Returns:
        bool: True if no duplicates, False otherwise.
    """
    # Placeholder for the solution
    values = []
    for i in test_tup:
        if i not in values:
            values.append(i)
        else:
            return False
    return True

def check_func(test_tup: tuple, k: any = None) -> bool:  
    """
    Supporting function for Check_none and check_k
    
    Args:
        test_tup (tuple): The tuple to check
        k (any): Default None, value to fund in test_tup
        
    Returns:
        bool: True if K in test_tup, else False
    """
    for i in test_tup:
        if i == k:
            return True
    return False


def check_none(test_tup: tuple) -> bool:
    """
    Check if the given tuple contains any None values.

    Args:
        test_tup (tuple): The tuple to check.

    Returns:
        bool: True if any element is None, False otherwise.
    """
    #return bool([x for x in test_tup if x == None])
    return check_func(test_tup, None)

def check_k(test_tup: tuple, k: any) -> bool:
    """
    Check if the value k exists in the tuple test_tup.

    Args:
    test_tup (tuple): The tuple to search in.
    k (any): The value to search for.

    Returns:
    bool: True if k is found in test_tup, False otherwise.
    """
    # Placeholder for the solution
    return check_func(test_tup, k)

def all_unique(test_list: list) -> bool:
    """
    Check if all elements in the list are unique.

    Args:
        test_list (list): The list to check.

    Returns:
        bool: True if all elements are unique, False otherwise.
    """
    # Placeholder for the solution
    return check_distinct(tuple(test_list))

def is_word_length_odd(word: str) -> bool:
    """
    Determine if the length of the given word is odd.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the length is odd, False otherwise.
    """
    # Implement the logic to check if the length of the word is odd
    return len(word) % 2 == 1

def circle_circumference(r: float) -> float:
    """
    Calculate the circumference of a circle given its radius.

    Args:
        r (float): The radius of the circle.

    Returns:
        float: The circumference of the circle.
    """
    # Replace the following line with your implementation
    return (2 * math.pi * r)

def closest_smaller_number(n: int) -> int:
    """
    Returns the closest smaller number than the given integer n.

    Args:
    n (int): A positive integer greater than 1.

    Returns:
    int: The closest smaller number than n.
    """
    # Placeholder for the solution
    return (n-1)

def degrees_to_radians(degrees: float) -> float:
    """
    Convert an angle from degrees to radians.

    Args:
        degrees (float): The angle in degrees.

    Returns:
        float: The angle in radians.
    """
    # Implement the conversion formula here
    return (degrees * (math.pi / 180))

def list_to_tuple(input_list: list) -> tuple:
    """
    Convert a list to a tuple.

    Args:
        input_list (list): The list to convert.

    Returns:
        tuple: A tuple containing the elements of the input list.
    """
    # Replace the following line with your implementation
    return tuple(input_list)

def convert_to_lowercase(input_string: str) -> str:
    """
    Convert the given string to lowercase.

    Args:
        input_string (str): The string to convert.

    Returns:
        str: The lowercase version of the input string.
    """
    # Your code here
    return input_string.lower()

def convert_to_uppercase(input_string: str) -> str:
    """
    Convert the given string to uppercase.

    Args:
        input_string (str): The string to convert.

    Returns:
        str: The uppercase version of the input string.
    """
    # Replace the following line with your implementation
    return input_string.upper()

def count_characters(input_string: str) -> int:
    """
    Count the total number of characters in the given string.

    Args:
        input_string (str): The string to count characters in.

    Returns:
        int: The total number of characters in the string.
    """
    return len(input_string)

def count_digits(input_string: str) -> int:
    """
    Count the number of digit characters in the given string.

    Args:
        input_string (str): The string to analyze.

    Returns:
        int: The count of digit characters in the string.
    """
    # Initialize a counter for digits
    digit_count = 0
    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            # Increment the counter
            digit_count += 1
    # Return the total count of digits
    return digit_count

def count_occurrences(tup: tuple, element: any) -> int:
    """
    Count the occurrences of an element in a tuple.

    Parameters:
    tup (tuple): The tuple to search within.
    element (any): The element to count.

    Returns:
    int: The number of times the element appears in the tuple.
    """
    return len([x for x in tup if x == element])

def count_equal_numbers(a: int, b: int, c: int) -> int:
    """
    Count the number of equal numbers among the three given integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int: The count of equal numbers.
    """
    # Implement the logic to count equal numbers
    count = 0
    if a == b: count += 1
    if a == c: count += 1
    if b == c: count += 1
    #adjust for offset
    if count == 1: count += 1
    return count

def count_integer_elements(lst: list) -> int:
    """
    Count the number of integer elements in the given list.

    Args:
        lst (list): The input list containing elements of various types.

    Returns:
        int: The count of integer elements in the list.
    """
    #return len([x for x in lst if type(x) == int])
    # Initialize a counter to zero
    count = 0
    # Iterate through the list and check each element
    for element in lst:
        # Placeholder for checking and counting integer elements
        if type(element) == int:
            count += 1
    # Return the final count
    return count

def count_nested_lists(input_list: list) -> int:
    """
    Count the number of nested lists within the given list.

    Args:
        input_list (list): The list to check for nested lists.

    Returns:
        int: The count of nested lists.
    """
    # Initialize a counter for nested lists
    count = 0
    # Iterate through the input list
    for element in input_list:
        # Check if the element is a list
        if isinstance(element, list):
            # Increment the counter
            count += 1
    # Return the count
    return count

def frequency(lst: list[int], num: int) -> int:
    """
    Count the number of occurrences of `num` in the list `lst`.

    Args:
    lst (list): A list of integers.
    num (int): The integer to count in the list.

    Returns:
    int: The count of occurrences of `num` in `lst`.
    """
    # Initialize a counter variable
    return len([x for x in lst if x == num])

def count_odd_numbers(numbers: list[int]) -> int:
    """
    Counts the number of odd numbers in a given list.

    Args:
        numbers (list): The input list of integers.

    Returns:
        int: The count of odd numbers in the list.
    """
    isOdd = lambda x: x%2 == 1
    return len([x for x in numbers if isOdd(x)])

def count_positive_numbers(numbers: list[int]) -> int:
    """
    Count the number of positive numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The count of positive numbers in the list.
    """
    return len([x for x in numbers if x > 0])

def count_occurrences(s: str) -> int:
    """
    Count the number of occurrences of the substring 'std' in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The count of 'std' occurrences.
    """
    return len(re.findall("std", s))

def count_true_booleans(lst: list) -> int:
    """
    Count the number of True values in the given list of booleans.

    Args:
    lst (list): A list containing boolean values.

    Returns:
    int: The count of True values in the list.
    """
    # Placeholder for the solution
    return len([x for x in lst if x])

def count_uppercase(s: str) -> int:
    """
    Count the number of uppercase characters in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The count of uppercase characters.
    """
    # Initialize a counter for uppercase characters
    count = 0
    # Iterate through each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Increment the counter
            count += 1
    # Return the final count
    return count

def count_vowels(string: str) -> int:
    """
    Counts the number of vowels in a given string.

    Args:
    string (str): The input string.

    Returns:
    int: The count of vowels in the string.
    """
    vowels = r"[AEIOUaeiou]"
    return len(re.findall(vowels, string))

def new_tuple(test_list: list[str], test_str: str) -> tuple:
    """
    Combine a list of strings and a single string into a tuple.

    Args:
    test_list (list): A list of strings.
    test_str (str): A single string.

    Returns:
    tuple: A tuple containing all elements of the list followed by the string.
    """
    # Add test_str to the list
    test_list.append(test_str)
    
    # Convert the list to a tuple and return
    return tuple(test_list)

def volume_cube(side: float) -> float:
    """
    Calculate the volume of a cube given its side length.

    Args:
    side (float): The length of a side of the cube.

    Returns:
    float: The volume of the cube.
    """
    # Placeholder for the solution
    return round(pow(side, 3), 3)

def volume_cylinder(radius: float, height: float) -> float:
    """
    Calculate the volume of a cylinder given its radius and height.

    Args:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.

    Returns:
        float: The volume of the cylinder.
    """
    # Placeholder for the solution
    return (math.pi * pow(radius, 2) * height)

def decimal_to_binary(n: int) -> str:
    """
    Convert a decimal number to its binary equivalent as a string.

    Args:
    n (int): A non-negative integer.

    Returns:
    str: The binary representation of the number without leading zeros.
    """
    # Replace the following line with your implementation
    if n == 0: return "0"
    return str(bin(n)).lstrip("0b")

def big_diff(nums: list[int]) -> int:
    """
    Calculate the difference between the largest and smallest values in a list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The difference between the largest and smallest values.
    """
    largest = smallest = nums[0]
    for i in nums[1:]:
        if i > largest: largest = i
        elif i < smallest: smallest = i
    return largest - smallest

def is_divisible_by_11(n: int) -> bool:
    """
    Determine if a number is divisible by 11.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is divisible by 11, False otherwise.
    """
    # Placeholder for the solution
    return n % 11 == 0

def divisible_numbers(numbers: list[int]) -> str:
    """
    Returns a comma-separated sequence of numbers that are divisible by 3 but not a multiple of 7.

    Args:
    numbers (list): The list of numbers.

    Returns:
    str: The comma-separated sequence of numbers.
    """
    return ",".join([str(x) for x in numbers if (x % 3 == 0 and x % 7 != 0)])

def dog_age(human_years: int) -> float:
    """
    Calculate a dog's age in dog years based on the given human years.

    Args:
        human_years (int): The age of the dog in human years.

    Returns:
        float: The age of the dog in dog years.
    """
    # Implement the logic to calculate the dog's age in dog years
    if human_years == 0:
        return 0
    if human_years <= 2:
        return 10.5 + dog_age(human_years - 1)
    else:
        return 4 + dog_age(human_years - 1)
    
def drop(n: int, seq: list) -> list:
    """
    Returns a list containing the elements of seq with the first n elements dropped.

    Args:
    n: The number of elements to drop.
    seq: The input sequence.

    Returns:
    list: The list with the first n elements dropped.
    """
    return seq[n:]

def drop_empty(input_dict: dict) -> dict:
    """
    Removes key-value pairs from the dictionary where the value is None.

    Args:
        input_dict (dict): The dictionary to process.

    Returns:
        dict: A new dictionary with None values removed.
    """
    # Implement the function logic here
    return {Key: Value for Key, Value in input_dict.items() if Value is not None}

def check_voting_eligibility(age: int) -> str:
    """
    Checks the voting eligibility based on the given age.

    Args:
    age (int): The person's age.

    Returns:
    str: A string indicating the voting eligibility.
    """
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
    
def exclude_first_last_items(lst: list) -> list:
    """
    Returns a new list that contains all elements of the original list except for the first and last items.

    Args:
    lst (list): The input list.

    Returns:
    list: The new list with excluded first and last items.
    """
    return lst[1:-1]

def extract_first_elements(lst: list[list]) -> list:
    """
    Extract the first element from each sublist in the given list.

    Args:
        lst (list of list): A list containing sublists.

    Returns:
        list: A list containing the first element of each sublist.
    """
    # Write your code here
    return [x[0] for x in lst]

def rear_extract(tuples_list: list[tuple]) -> list:
    """
    Extract the last element from each tuple in the list.

    Args:
        tuples_list (list of tuples): A list containing tuples.

    Returns:
        list: A list containing the last element of each tuple.
    """
    # Placeholder for the solution
    return [x[-1] for x in tuples_list]

def filter_negatives(numbers: list[int]) -> list:
    """
    Filters and returns the negative numbers from the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list containing only the negative integers from the input list.
    """
    return [x for x in numbers if x < 0]

def filter_odds(numbers: list) -> list:
    """
    Filters the odd numbers from a list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list containing only the odd integers from the input list.
    """
    # Placeholder for the solution
    isOdd = lambda x: x % 2 == 1
    return [x for x in numbers if isOdd(x)]

def filter_odd_numbers(nums: list[int]) -> list:
    """
    Filters the odd numbers from a list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list containing only the odd integers from the input list.
    """
    return list(filter(lambda x: x % 2 == 1, nums))

def cube_nums(nums: list[int]) -> list[int]:
    """
    Calculate the cube of each number in the input list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list containing the cubes of the input integers.
    """
    # Replace the following line with your implementation
    return [pow(x, 3) for x in nums]

def find_even_numbers(numbers: list[int]) -> list[int]:
    """
    This function takes a list of integers and returns a list of even numbers.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A list containing only the even integers from the input list.
    """
    # Placeholder for the solution
    return list(filter(lambda x: x % 2 == 0, numbers))

def first_digit(n: int) -> int:
    """
    Returns the first digit of the given integer.

    Args:
    n (int): The input integer.

    Returns:
    int: The first digit of the number.
    """
    # Placeholder for the solution
    return int(str(abs(n))[0])

def last_digit(n: int) -> int:
    """
    Returns the last digit of the given integer n.

    Args:
    n (int): The input integer.

    Returns:
    int: The last digit of n.
    """
    # Your code here
    return int(str(abs(n))[-1])

def smallest_num(xs: list[int|float]) -> int|float:
    """
    Find the smallest number in a list.

    Args:
        xs (list): A list of numbers.

    Returns:
        number: The smallest number in the list.
    """
    smallest = xs[0]
    for i in xs[1:]:
        if i < smallest: smallest = i
    return smallest

def generate_dictionary(n: int) -> dict:
    """
    Generates a dictionary containing (i, i*i) pairs for each integral number between 1 and n (both inclusive).

    Args:
    n (int): The input number.

    Returns:
    dict: The generated dictionary.
    """
    value = {}
    for i in range(1, n+1):
        value.update({i: pow(i, 2)})
    return value

def create_empty_dicts(n: int) -> list[dict]:
    """
    Create a list of n empty dictionaries.

    Args:
        n (int): The number of empty dictionaries to create.

    Returns:
        list: A list containing n empty dictionaries.
    """
    # Your code here
    return [{}] * n

def find_quotient(n: int, m: int) -> int:
    """
    Calculate the quotient of n divided by m, rounded down to the nearest integer.

    Args:
    n (int): The dividend.
    m (int): The divisor.

    Returns:
    int: The quotient of the division.
    """
    # Implement the function using integer division
    return n // m

def lateral_surface_area(l: float) -> float:
    """
    Calculate the lateral surface area of a cube given its side length.

    Args:
        l (float): The side length of the cube.

    Returns:
        float: The lateral surface area of the cube.
    """
    # Replace the following line with the correct implementation
    return (4 * pow(l, 2))

def multiply_list(numbers: list[int|float]) -> list[int|float]:
    """
    Multiplies each element in the given list by 2.

    Args:
        numbers (list): The input list of numbers.

    Returns:
        list: A new list with each element multiplied by 2.
    """
    return [(x*2) for x in numbers]

def order_list(strings: str) -> list[str]:
    """
    Orders the given list of strings in alphabetical order.

    Args:
        strings (list): The input list of strings.

    Returns:
        list: A new list with the strings sorted in alphabetical order.
    """
    return sorted(strings, reverse=True)

def maximum(a: int|float, b: int|float) -> int|float:
    """
    Returns the maximum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The larger of the two numbers.
    """
    return max(a, b)

def median_trapezium(base1: float, base2: float) -> float:
    """
    Calculate the median length of a trapezium given the lengths of its two parallel sides.

    Args:
    base1 (float): The length of the first parallel side.
    base2 (float): The length of the second parallel side.

    Returns:
    float: The median length of the trapezium.
    """
    # Calculate the median length
    # Replace the following line with your implementation
    return ((base1 + base2) / 2)

def median_of_three(a: float, b: float, c: float) -> float:
    """
    Returns the median of three numbers.

    Args:
        a (float): The first number.
        b (float): The second number.
        c (float): The third number.

    Returns:
        float: The median of the three numbers.
    """
    # Implement the logic to find the median of three numbers
    return (sorted([a, b, c]))[1]

def min_of_three(a: int|float, b: int|float, c: int|float) -> int|float:
    """
    Returns the smallest of three numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.

    Returns:
    int or float: The smallest of the three numbers.
    """
    # Placeholder for the solution
    return min([a, b, c])

def minimum(a: int|float, b: int|float) -> int|float:
    """
    Returns the smaller of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The smaller of the two numbers.
    """
    # Write your code here
    return min(a, b)

def classify_number(number: int) -> str:
    """
    Classifies the given number as positive, negative, or zero.

    Args:
        number (int): The input number.

    Returns:
        str: A string indicating the classification of the number.
    """
    if number > 0: return "Positive"
    elif number < 0: return "Negative"
    elif number == 0: return "Zero"

def perimeter_pentagon(side_length: float) -> float:
    """
    Calculate the perimeter of a regular pentagon given the side length.

    Args:
        side_length (float): The length of one side of the pentagon.

    Returns:
        float: The perimeter of the pentagon.
    """
    # Placeholder for the solution
    return 5 * side_length

def rectangle_area(length: int, breadth: int) -> int:
    """
    Calculate the area of a rectangle given its length and breadth.

    Args:
        length (int): The length of the rectangle.
        breadth (int): The breadth of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return length * breadth

def remove_odd_characters(input_string: str) -> str:
    """
    Removes characters at odd indices from the input string.

    Parameters:
    input_string (str): The string to process.

    Returns:
    str: A new string with characters at odd indices removed.
    """
    # Placeholder for the solution
    return "".join(x for x in input_string[::2])

def remove_odd(numbers: list[int]) -> list[int]:
    """
    Removes all odd numbers from the input list and returns a new list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list with all odd numbers removed.
    """
    return [x for x in numbers if x % 2 == 0]

def remove_whitespaces(text: str) -> str:
    """
    Remove all whitespaces from the given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with all whitespaces removed.
    """
    # Replace the following line with your implementation
    return text.replace(" ", "")

def replace_blank(input_string: str, replacement_char: str) -> str:
    """
    Replace all blank spaces in the input string with the specified replacement character.

    Args:
        input_string (str): The string to process.
        replacement_char (str): The character to replace spaces with.

    Returns:
        str: The modified string with spaces replaced.
    """
    return input_string.replace(" ", replacement_char)

def replace_characters(input_string: str, target_char: str, replacement_char: str) -> str:
    """
    Replace all occurrences of target_char in input_string with replacement_char.

    Args:
        input_string (str): The original string.
        target_char (str): The character to be replaced.
        replacement_char (str): The character to replace with.

    Returns:
        str: The modified string with replacements.
    """
    # Your code here
    return input_string.replace(target_char, replacement_char)

def replace_last_element(list1: list, list2: list) -> list:
    """
    Replace the last element of list1 with all elements of list2.

    Args:
        list1 (list): The first list.
        list2 (list): The second list whose elements will replace the last element of list1.

    Returns:
        list: The modified list1 with its last element replaced by elements of list2.
    """
    # Replace the last element of list1 with the elements of list2
    return list1[:-1] + list2

def replace_spaces(string: str) -> str:
    """
    Replace all spaces in the given string with '%20'.

    Args:
        string (str): The input string.

    Returns:
        str: The modified string with spaces replaced by '%20'.
    """
    replacement = "%20"
    return string.replace(" ", replacement)

def surface_area_of_sphere(radius: float) -> float:
    """
    Calculate the surface area of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The surface area of the sphere.
    """
    # Implement the formula for the surface area of a sphere
    return (4 * math.pi * pow(radius, 2))

def volume_of_sphere(radius: float) -> float:
    """
    Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    return (4/3) * math.pi * radius**3

def split_two_parts(input_list: list, L: int) -> tuple:
    """
    Splits the input list into two parts based on the given length L.

    Args:
        input_list (list): The list to be split.
        L (int): The length of the first part.

    Returns:
        tuple: A tuple containing two lists.
    """
    # Implement the function logic here
    if L <= 0:
        return ([], input_list)
    return (input_list[:L], input_list[L:])

def generate_list(values: str) -> list:
    """
    Generates a list containing each number from a sequence of comma-separated numbers.

    Args:
    values (str): The input sequence of comma-separated numbers.

    Returns:
    list: The generated list.
    """
    if len(values) == 0: return []
    return values.split(",")

def split_string(word: str) -> list:
    """
    Splits the input string into a list of its individual characters.

    Args:
        word (str): The string to split.

    Returns:
        list: A list containing each character of the input string.
    """
    # Replace the following line with your implementation
    return list(word)

def square_nums(nums: list[int]) -> list[int]:
    """
    Given a list of integers, return a new list containing the squares of each element.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A list containing the squares of the input integers.
    """
    # Placeholder for the solution
    return [pow(x, 2) for x in nums]

def square_perimeter(side_length: float) -> float:
    """
    Calculate the perimeter of a square given its side length.

    Args:
        side_length (float): The length of one side of the square.

    Returns:
        float: The perimeter of the square.
    """
    # Replace the following line with your implementation
    return 4* side_length

def reverse_string(string: str) -> str:
    """
    Reverses the characters in the given string.

    Args:
    string (str): The input string.

    Returns:
    str: A new string with the characters reversed.
    """
    return string[::-1]

def string_to_list(string: str) -> list[str]:
    """
    Convert a string to a list of strings split on the space character.

    Args:
        string (str): The input string to be split.

    Returns:
        list: A list of strings split from the input string.
    """
    return string.split(" ")

def string_to_tuple(input_string: str) -> tuple:
    """
    Convert the input string into a tuple of characters.

    Args:
        input_string (str): The string to convert.

    Returns:
        tuple: A tuple containing all characters of the input string.
    """
    return tuple(input_string[::1])

def sum_and_average(n: int) -> tuple:
    """
    Calculate the sum and average of the first n natural numbers.

    Args:
        n (int): The number of natural numbers to consider.

    Returns:
        tuple: A tuple containing the sum and the average.
    """
    val = sum([x for x in range(1, n+1)])
    return (val, val/n)

def sum_lists(lst1: list, lst2: list) -> list:
    """
    Sums corresponding elements of two lists.

    Args:
        lst1 (list): The first list of numbers.
        lst2 (list): The second list of numbers.

    Returns:
        list: A list containing the sums of corresponding elements.
    """
    # Ensure the lists are of the same length
    # Implement the summation logic
    return [x + y for x, y in zip(lst1, lst2)]

def return_sum(input_dict: dict) -> int:
    """
    Calculate the sum of all values in the given dictionary.

    Args:
        input_dict (dict): A dictionary with string keys and integer values.

    Returns:
        int: The sum of all values in the dictionary.
    """
    return sum(input_dict.values())

def big_sum(nums: list) -> int:
    """
    Calculate the sum of the largest and smallest values in the list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of the largest and smallest values.
    """
    # Placeholder for the solution
    nums.sort()
    return nums[0] + nums[-1]

def sum_negative_numbers(nums: list[int]) -> int:
    """
    Calculate the sum of all negative numbers in the given list.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of all negative numbers in the list.
    """
    return sum([x for x in nums if x < 0])

def sum_of_array(arr: list) -> int:
    """
    Calculate the sum of all elements in the input list.

    Args:
        arr (list): A list of numeric values.

    Returns:
        int: The sum of the elements in the list.
    """
    return sum(arr)

def surface_area_of_cube(side_length: int) -> int:
    """
    Calculate the surface area of a cube given the side length.

    Args:
    side_length (int): The length of one side of the cube.

    Returns:
    int: The surface area of the cube.
    """
    return 6 * side_length**2

def swap_first_last(lst):
    """
    Swap the first and last elements of the list.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with the first and last elements swapped.
    """
    # Check if the list has fewer than two elements
    if len(lst) < 2:
        return lst
    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp

    return lst

def swap_numbers(a: int|float, b: int|float) -> tuple:
    """
    Swap the positions of two numbers and return them as a tuple.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        tuple: A tuple with the second number first and the first number second.
    """
    return (b, a)

def take(n: int, seq: list) -> list:
    """
    Returns a list containing the first n elements of seq.

    Args:
    n: The number of elements to take.
    seq: The input sequence.

    Returns:
    list: The list of the first n elements.
    """
    return seq[:n]

def toggle_case(string):
    """
    Toggle the case of all characters in the input string.

    Args:
        string (str): The input string.

    Returns:
        str: A new string with toggled case for each character.
    """
    return string.swapcase()
            
def find_volume(base_length: float, base_height: float, prism_height: float) -> float:
    """
    Calculate the volume of a triangular prism.

    Args:
        base_length (float): The length of the base of the triangle.
        base_height (float): The height of the triangle.
        prism_height (float): The height of the prism.

    Returns:
        float: The volume of the triangular prism.
    """
    return 0.5 * base_length * base_height * prism_height

def tuple_size(input_tuple: tuple) -> int:
    """
    Calculate the size in bytes of the given tuple.

    Args:
        input_tuple (tuple): The tuple whose size is to be calculated.

    Returns:
        int: The size of the tuple in bytes.
    """
    return sys.getsizeof(input_tuple)

def tuple_to_string(tup: tuple) -> str:
    """
    Convert a tuple of characters into a string.

    Args:
    tup (tuple): A tuple containing single-character strings.

    Returns:
    str: A string formed by concatenating the characters in the tuple.
    """
    return "".join(tup)