from imports import *

def bell_number(n: int) -> int:
    """
    Calculate the nth Bell number, which represents the number of ways to partition a set of n elements.

    Args:
        n (int): The number of elements in the set.

    Returns:
        int: The nth Bell number.
    """
    # Initialize a table to store the Bell numbers
    dp = [1] + [0] * n

    for i in range(1, n+1):
        # The first element in each row is the same as the last element in the previous row
        prev = dp[0]
        dp[0] = dp[i-1]
        for j in range(1, i+1):
            # The Bell number for n is the sum of the Bell numbers for all previous partitions
            temp = dp[j]
            dp[j] = prev + dp[j-1]
            prev = temp

    return dp[0]

def is_majority(arr: list[int], x: int) -> bool:
    """
    Determine if x is the majority element in the sorted array arr.

    Args:
        arr (list[int]): The sorted array of integers.
        x (int): The element to check for majority.

    Returns:
        bool: True if x is the majority element, False otherwise.
    """
    # Count the frequency of the element x in the array
    count = arr.count(x)
    
    # Check if the count of x is more than half the length of the array
    return count > len(arr) // 2

def compose(f, g):
    """
    Performs function composition by taking two functions as input and returning a composed function.

    Args:
    f: The first function.
    g: The second function.

    Returns:
    function: The composed function.
    """
    return lambda x: f(g(x))

def count_balanced_binary_sequences(n):
    """
    Calculate the number of binary sequences of length 2n such that the sum of the first n bits
    is equal to the sum of the last n bits.

    Args:
    n (int): The half-length of the binary sequence.

    Returns:
    int: The count of such balanced binary sequences.
    """
    total_sequences = 0
    
    # For each possible number of 1's in the first half (k)
    for k in range(0, n + 1):
        # The number of ways to place k 1's in the first half (C(n, k))
        # and the number of ways to place k 1's in the second half (C(n, k))
        total_sequences += math.comb(n, k) ** 2
        
    return total_sequences

def read_csv_file(file_path, columns):
    """
    Reads a CSV file and extracts data from specific columns.

    Args:
    file_path (str): The path to the CSV file.
    columns (list): The list of column names to extract data from.

    Returns:
    list: A list of dictionaries containing the data from the specified columns.
    """
    result = []
    
    # Open the CSV file and read it using csv.DictReader
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV file
        for row in reader:
            # Extract only the specified columns and add to result
            filtered_row = {col: row[col] for col in columns if col in row}
            result.append(filtered_row)
    
    return result