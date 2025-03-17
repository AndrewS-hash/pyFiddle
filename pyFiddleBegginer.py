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