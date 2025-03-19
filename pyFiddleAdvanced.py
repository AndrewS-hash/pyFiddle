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

def count_balanced_binary_sequences(n: int) -> int:
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

def read_csv_file(file_path: str, columns: list) -> list:
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

def eulerian_num(n: int, m: int) -> int:
    """
    Calculate the Eulerian number A(n, m) using its recursive definition.

    Args:
        n (int): The number of elements.
        m (int): The number of ascents.

    Returns:
        int: The Eulerian number A(n, m).
    """
    # Base cases
    if m >= n or n == 0:
        return 0
    if m == 0:
        return 1
    return (n-m) * eulerian_num(n-1, m-1) + ((m+1) * eulerian_num(n-1, m))

def extract_email_addresses(string: str) -> list[str]:
    """
    Extracts email addresses from a given string using regex.

    Args:
        string (str): The input string.

    Returns:
        list: A new list with the extracted email addresses.
    """
    """ONLY LOOKING AT LETTERS and .com Emails"""
    pattern = r"[a-zA-Z]+@[a-zA-Z]+\.com"
    return re.findall(pattern, string)

def count_no_of_ways(n: int, k: int) -> int:
    """
    Calculate the number of ways to paint a fence with n posts and k colors such that
    no more than two adjacent posts have the same color.

    Args:
    n (int): The number of posts.
    k (int): The number of colors.

    Returns:
    int: The number of ways to paint the fence modulo 10^9+7.
    """
    MOD = 10**9 + 7
    if n == 1:
        return k  # If there's only one post, the number of ways is simply k
    
    # dp[i][0] is the number of ways to paint i posts such that the i-th post is different from (i-1)-th post
    # dp[i][1] is the number of ways to paint i posts such that the i-th post is the same as (i-1)-th post
    dp = [[0] * 2 for _ in range(n+1)]
    
    # Base cases
    dp[1][0] = k  # One post, k ways to paint it
    dp[1][1] = 0  # It's impossible to have the first post same as the previous one
    
    for i in range(2, n+1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * (k-1) % MOD
        dp[i][1] = dp[i-1][0] % MOD
    
    return (dp[n][0] + dp[n][1]) % MOD

def find_common_elements(*lists: list) -> list:
    """
    Finds the common elements across multiple lists.

    Args:
        *lists (list): The input lists.

    Returns:
        list: A new list with the common elements.
    """
    # Convert the first list into a set
    common_elements = set(lists[0])
    
    # Intersect the set with sets of the remaining lists
    for lst in lists[1:]:
        common_elements &= set(lst)
    
    # Return the common elements as a list
    return list(common_elements)

#POORLY WORDED NEEDS
def find_element(arr: list[int], ranges: list[tuple], rotations: int, index: int) -> int:
    """
    Find the element at a given index after performing a series of rotations.

    Parameters:
    arr (list): The list of integers.
    ranges (list): A list of tuples defining the rotation ranges.
    rotations (int): The number of rotations to perform. <-- Poorly Worded
    index (int): The index to find the element at.

    Returns:
    int: The element at the specified index after rotations.
    """
    # Perform rotations on the specified ranges
    for start, end in ranges:
        # Slice the range to rotate
        subrange = arr[start:end+1]
        n = len(subrange)
        
        # Perform the rotation: number of rotations modulo the length of the subrange
        rotations_effective = 1 % n
        
        # Perform the rotation by slicing
        rotated_subrange = subrange[-rotations_effective:] + subrange[:-rotations_effective]
        
        # Put the rotated subrange back into the array
        arr[start:end+1] = rotated_subrange
        rotations -= 1
        if rotations == 0:
            break
    
    # Return the element at the specified index
    return arr[index]

def flatten(tree: list) -> list:
    """
    Returns a flattened list of all the elements in the tree.

    Args:
    tree: The input tree structure, where each element can be a value or a subtree (a list).

    Returns:
    list: The flattened list of elements.
    """
    result = []
    
    # Iterate over each element in the tree
    for item in tree:
        if isinstance(item, list):
            # If the item is a list, recursively flatten it
            result.extend(flatten(item))
        else:
            # If it's a leaf (not a list), add it to the result
            result.append(item)
    
    return result

def find_solution(a: int, b: int, n: int) -> tuple|None:
    """
    Find integers x and y such that a * x + b * y = n.

    Args:
        a (int): Coefficient of x.
        b (int): Coefficient of y.
        n (int): Target value.

    Returns:
        tuple: A tuple (x, y) if a solution exists, otherwise None.
    """
    function = lambda x, y: (a*x + b*y) == n
    for i in range(0, n//a + 1):
        for j in range(0, n//b + 1):
            if function(i, j): return (i, j)
    return None

def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    """
    Find the k smallest pairs from two sorted arrays.

    Args:
        nums1 (List[int]): First sorted list of integers.
        nums2 (List[int]): Second sorted list of integers.
        k (int): Number of smallest pairs to find.

    Returns:
        List[List[int]]: List of k smallest pairs.
    """
    # Make a list of lists of all pairs
    pairs = []
    for i in nums1:
        for j in nums2:
            pairs.append([i, j])
    #Sort array based on sum of pairs
    pairs.sort(key=lambda x: sum(x))
    #Return first K number of pairs
    return pairs[:k]

def find_kth(arr1: list, arr2: list, k: int) -> int:
    """
    Find the kth smallest element from two sorted arrays.

    Args:
        arr1 (list): First sorted array.
        arr2 (list): Second sorted array.
        k (int): The kth position to find (1-based index).

    Returns:
        int: The kth smallest element.
    """
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            k -= 1
            if k == 0:
                return arr1[i]
            i += 1
        else:
            k -= 1
            if k == 0:
                return arr2[j]
            j += 1

    # If one array is exhausted, continue with the other array
    while i < len(arr1):
        k -= 1
        if k == 0:
            return arr1[i]
        i += 1

    while j < len(arr2):
        k -= 1
        if k == 0:
            return arr2[j]
        j += 1

    return None

def largest_subset(numbers: List[int]) -> int:
    """
    Find the size of the largest subset of numbers such that every pair is divisible.
    
    Args:
    numbers (List[int]): A list of positive integers.

    Returns:
    int: The size of the largest divisible subset.
    """
    if not numbers:
        return 0

    # Sort the numbers to simplify the divisibility check
    numbers.sort()

    # DP array to store the largest subset size ending at each number
    dp = [1] * len(numbers)

    # Variable to store the maximum size of the divisible subset
    max_subset_size = 1

    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] % numbers[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        max_subset_size = max(max_subset_size, dp[i])

    return max_subset_size

def max_sub_array_sum_repeated(arr: list, n: int, k: int) -> int:
    """
    Find the largest sum of a contiguous subarray in the modified array formed by repeating the given array k times.

    Parameters:
    a (list): The input array.
    n (int): The length of the input array.
    k (int): The number of times the array is repeated.

    Returns:
    int: The largest sum of a contiguous subarray.
    """
    # Placeholder for the implementation
    maxVal = arr[0]
    for i in range(k-1):
        arr.extend(arr)
    for start in range(0, (n*k) + 1):
        for end in range(start, (n*k) + 1):
            if sum(arr[start:end+1]) > maxVal:
                maxVal = sum(arr[start:end+1])
    return maxVal

def lcs_of_three(X: str, Y: str, Z: str) -> int:
    """
    Calculate the length of the longest common subsequence among three strings.

    Args:
        X (str): The first string.
        Y (str): The second string.
        Z (str): The third string.

    Returns:
        int: The length of the longest common subsequence.
    """
    # Initialize lengths of the strings
    m, n, o = len(X), len(Y), len(Z)

    # Create a 3D dp array to store lengths of LCS of substrings
    dp = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                # If characters match in all three strings
                if X[i - 1] == Y[j - 1] == Z[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    # The value in dp[m][n][o] will be the length of LCS of X, Y, and Z
    return dp[m][n][o]

def longest_palindromic_subsequence(s: str) -> int:
    """
    Calculate the length of the longest palindromic subsequence in the given string.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest palindromic subsequence.
    """
    n = len(s)
    
    # Initialize the DP table with 0s
    dp = [[0] * n for _ in range(n)]
    
    # Base case: single character subsequences
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the DP table
    for length in range(2, n+1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # The result is the value in dp[0][n-1]
    return dp[0][n-1]

def get_ludic(n: int) -> list:
    """
    Generate all Ludic numbers less than or equal to the given integer n.

    Args:
        n (int): The upper limit to generate Ludic numbers.

    Returns:
        list: A list of Ludic numbers up to n.
    """
    # Initialize the list of numbers from 1 to n
    # Implement the sieve process to filter Ludic numbers
    nums = list(range(1, n+1))
    ludNums = []
    while nums:
        ludNums.append(nums.pop(0))
        nums = [x for x in nums if x not in nums[nums[0]::nums[0]]]
    return ludNums

def transpose_matrix(matrix: list[list]) -> list:
    """
    Transposes a matrix represented as a list of lists.

    Args:
        matrix (list): The input matrix.

    Returns:
        list: The transposed matrix.
    """
    # Use zip to transpose the matrix and return the result as a list of lists
    return [list(row) for row in zip(*matrix)]

def max_sum_bitonic_subsequence(arr: List[int]) -> int:
    """
    Calculate the maximum sum of a bitonic subsequence in the given array.
    
    Args:
    arr (List[int]): The input array of integers.
    
    Returns:
    int: The maximum sum of a bitonic subsequence.
    """
    n = len(arr)
    
    # Edge case: if the array has less than 3 elements, it cannot form a bitonic subsequence
    if n < 3:
        return sum(arr)
    
    # Step 1: Calculate maximum sum of increasing subsequence up to each index
    inc = arr[:]  # This will hold the maximum sum of increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + arr[i])

    # Step 2: Calculate maximum sum of decreasing subsequence from each index
    dec = arr[:]  # This will hold the maximum sum of decreasing subsequences
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j] + arr[i])

    # Step 3: Calculate the maximum sum of bitonic subsequence
    max_sum = 0
    for i in range(n):
        if inc[i] + dec[i] - arr[i] > max_sum:
            max_sum = inc[i] + dec[i] - arr[i]  # Subtract arr[i] because it is counted twice
    
    return max_sum
        
def max_average_path(matrix: list[list[int]]) -> float:
    """
    Calculate the maximum average path in a square matrix.

    Args:
        matrix (list of list of int): The square matrix of costs.

    Returns:
        float: The maximum average of any valid path.
    """
    n = len(matrix)
    
    # DP table to store the maximum sum of path to each cell
    dp = [[-float('inf')] * n for _ in range(n)]
    
    # Base case: start at the top-left corner
    dp[0][0] = matrix[0][0]
    
    # Fill the DP table
    for i in range(n):
        for j in range(n):
            # Skip the starting point since it's already initialized
            if i == 0 and j == 0:
                continue
            
            # If we can move down from the above cell
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + matrix[i][j])
            
            # If we can move right from the left cell
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + matrix[i][j])
    
    # The answer will be the sum at the bottom-right corner divided by the number of steps
    total_steps = 2 * (n - 1)
    return dp[n-1][n-1] / (total_steps + 1)

def max_subarray_product(arr: list[int]) -> int:
    """
    Find the maximum product of any contiguous subarray in the given array.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum product of any contiguous subarray.
    """
    # Placeholder for the solution
    def makeSubarray(arr: list) -> list[list]:
        val = []
        for i in range(0, len(arr)+1):
            for j in range(i+1, len(arr)+1):
                val.append(arr[i:j])
        return val
    return max([math.prod(x) for x in makeSubarray(arr)])

def get_median(arr1: list, arr2: list, n: int) -> float:
    """
    Calculate the median of two sorted lists of the same size.

    Args:
    arr1 (list): First sorted list.
    arr2 (list): Second sorted list.
    n (int): Size of each list.

    Returns:
    float: The median of the combined sorted list.
    """
    # Merge the two lists
    merged_arr = arr1 + arr2
    merged_arr.sort()
    
    # Calculate median for an even-length array
    mid = len(merged_arr) // 2
    if len(merged_arr) % 2 == 0:
        return (merged_arr[mid - 1] + merged_arr[mid]) / 2
    else:
        return merged_arr[mid]

def rearrange_bigger(n: int) -> int|bool:
    """
    Given an integer n, find the next bigger number that can be formed by rearranging its digits.
    If no such number exists, return False.

    Args:
    n (int): The input number.

    Returns:
    int or bool: The next bigger number or False if not possible.
    """
    # Convert the number to a list of its digits
    digits = list(str(n))
    
    # Step 1: Find the first digit that is smaller than the digit next to it (from the right)
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such digit is found, return False (the digits are in descending order)
    if i == -1:
        return False
    
    # Step 2: Find the smallest digit on the right of 'digits[i]' that is larger than 'digits[i]'
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Step 3: Swap the digits
    digits[i], digits[j] = digits[j], digits[i]
    
    # Step 4: Sort the digits after position i in ascending order to get the smallest number
    digits = digits[:i + 1] + sorted(digits[i + 1:])
    
    # Convert the list back to an integer and return
    return int(''.join(digits))

def bell_number(n: int) -> int:
    """
    Calculate the nth Bell number.

    Args:
        n (int): The index of the Bell number to compute.

    Returns:
        int: The nth Bell number.
    """
    # Create a table to store the Bell numbers
    bell = [[0] * (n+1) for _ in range(n+1)]
    
    # The first Bell number is always 1
    bell[0][0] = 1
    
    # Fill the Bell triangle
    for i in range(1, n + 1):
        # First value in every row is the last value of the previous row
        bell[i][0] = bell[i - 1][i - 1]
        
        # Fill the rest of the entries in the Bell triangle
        for j in range(1, i + 1):
            bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]
    
    # The Bell number is the last element in the nth row
    return bell[n][0]

def partial(f, *args):
    """
    Returns a new function that is f partially applied to the arguments.

    Args:
    f: The function to partially apply.
    *args: The arguments to partially apply.

    Returns:
    function: The new function that is f partially applied to the arguments.
    """
    def wrapper(*remaining_args):
        return f(*args, *remaining_args)
    return wrapper

def validate_password(password):
    """
    Validates a password based on certain criteria using regex.

    Args:
        password (str): The input password.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    minLen = 8
    upper = r"[A-Z]"
    lower = r"[a-z]"
    digits = r"[0-9]"
    special = r"[!@#$%^&*]"
    valid = True
    if len(password) < minLen:
        valid = False
    elif not re.search(upper, password):
        valid = False
    elif not re.search(lower, password):
        valid = False
    elif not re.search(digits, password):
        valid = False
    elif not re.search(special, password):
        valid = False
    return valid

def extract_even(nested_tuple: tuple) -> tuple:
    """
    Removes all odd numbers from a nested tuple, preserving the structure.

    Args:
        nested_tuple (tuple): A tuple containing integers or other nested tuples.

    Returns:
        tuple: A new tuple with only even numbers.
    """
    # List comprehension to filter the tuple
    result = tuple(
        extract_even(item) if isinstance(item, tuple) else item
        for item in nested_tuple if isinstance(item, int) and item % 2 == 0 or isinstance(item, tuple)
    )
    return result



def sum_amicable_numbers(limit: int) -> int:
    """
    Calculate the sum of all amicable numbers from 1 to the given limit.

    Args:
        limit (int): The upper limit to find amicable numbers.

    Returns:
        int: The sum of all amicable numbers up to the limit.
    """
    def sum_of_divisors(n: int) -> int:
        """
        Calculate the sum of proper divisors of a number (excluding the number itself).

        Args:
            n (int): The number for which to find the sum of divisors.

        Returns:
            int: The sum of proper divisors of n.
        """
        divisors = {1}  # Start with 1 because every number is divisible by 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                if i != n // i:  # Avoid adding square roots twice
                    divisors.add(n // i)
        return sum(divisors)

    amicable_sum = 0
    seen = set()  # To avoid counting duplicates

    # Iterate through all numbers from 2 to the limit, inclusive
    for num in range(2, limit + 1):  # Including the limit
        if num not in seen:
            partner = sum_of_divisors(num)
            
            # Check if the partner is not the number itself and if they are amicable
            if partner != num and sum_of_divisors(partner) == num:
                amicable_sum += num
                amicable_sum += partner
                seen.add(num)
                seen.add(partner)

    return amicable_sum

def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient C(n, k).
    """
    if k > n:
        return 0
    return math.comb(n, k)

def sum_of_binomial_products(n):
    """
    Calculate the sum of the product of consecutive binomial coefficients for a given n.
    """
    total_sum = 0
    for k in range(n):
        total_sum += binomial_coefficient(n, k) * binomial_coefficient(n, k + 1)
    return total_sum

def sum_of_subarray_products(arr: list) -> int:
    """
    Calculate the sum of the products of all possible subarrays of the given list.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The sum of the products of all possible subarrays.
    """
    n = len(arr)
    total_sum = 0
    
    # Iterate over each possible starting point of subarrays
    for i in range(n):
        product = 1
        # For each subarray starting at index i, calculate the product
        for j in range(i, n):
            product *= arr[j]
            total_sum += product
            
    return total_sum

def calculate_sum_tree(tree: list) -> int:
    """
    Calculates the sum of all the numbers in a tree structure.

    Args:
    tree (list): The input tree structure.

    Returns:
    int: The calculated sum.
    """
    # Base case: If the tree is empty, the sum is 0.
    if not tree:
        return 0
    
    # If the current element is a number, return it
    if isinstance(tree, int):
        return tree
    
    # If the current element is a list, recursively sum up its children
    return sum(calculate_sum_tree(subtree) for subtree in tree)

def toggle_middle_bits(n: int) -> int:
    """
    Toggle all bits of the number `n` except the first and last bits.
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The number with middle bits toggled.
    """
    # Step 1: Calculate the number of bits in n
    num_bits = n.bit_length()
    
    # Step 2: If the number has fewer than 3 bits, return the number as it is
    if num_bits < 3:
        return n
    
    # Step 3: Create a mask with all 1's except the first and last bits
    # The mask will be all 1's first, and then we will set the first and last bits to 0.
    mask = (1 << num_bits) - 1  # All bits set to 1
    
    # Set the first (most significant) bit and the last (least significant) bit to 0
    mask = mask & ~(1 << (num_bits - 1))  # Clear the first bit (most significant)
    mask = mask & ~1                    # Clear the last bit (least significant)
    
    # Step 4: XOR the number with the mask to toggle the middle bits
    return n ^ mask

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"TreeNode({self.value})"
    
    def max_depth(self):
        """
        Returns the maximum depth of the tree starting from this node.

        Returns:
            int: The maximum depth.
        """
        # If the node has no children (a leaf), the depth is 1
        if not self.children:
            return 1
        
        # Otherwise, the depth is 1 + the max depth of its children
        return 1 + max(child.max_depth() for child in self.children)


def build_tree(lst):
    """
    Converts a nested list into a tree structure.

    Args:
        lst (list): A nested list representing the tree structure.

    Returns:
        TreeNode: The root node of the tree.
    """
    # Base case: If the list is empty, return None
    if not lst:
        return None

    # The first element of the list is the root value
    root = TreeNode(lst[0])

    # If there are other elements, they represent child nodes
    for item in lst[1:]:
        if isinstance(item, list):
            # If the item is a list, recursively build the subtree
            root.add_child(build_tree(item))
        else:
            # If the item is a value (leaf node), create a node and add as a child
            root.add_child(TreeNode(item))

    return root


def print_tree(node, level=0):
    """
    Helper function to print the tree structure.

    Args:
        node (TreeNode): The node to start printing from.
        level (int): The current level of indentation in the tree.
    """
    print(" " * (level * 2) + str(node.value))
    for child in node.children:
        print_tree(child, level + 1)

def calculate_depth_tree(tree):
    """
    Calculates the depth of a tree structure.

    Args:
    tree (list): The input tree structure.

    Returns:
    int: The calculated depth.
    """
    # If the tree is empty, return 0
    if not tree:
        return 0
    node = build_tree(tree)
    return node.max_depth()

def find_largest_value_tree(tree: list) -> int:
    """
    Finds the largest value in a tree structure.

    Args:
    tree (list): The input tree structure.

    Returns:
    int: The largest value found in the tree.
    """
    def flatten_list(nested_list: list) -> list:
        """
        Flatten a nested list into a single list.

        Args:
            nested_list (list): The input list which may contain other nested lists.

        Returns:
            list: The flattened list containing all elements in the original list, in order.
        """
        flattened = []
        
        # Iterate through each element in the nested list
        for item in nested_list:
            if isinstance(item, list):
                # Recursively flatten the sublist
                flattened.extend(flatten_list(item))
            else:
                # Add the item to the flattened list (it's a number, not a list)
                flattened.append(item)
        
        return flattened
    arr = flatten_list(tree)
    arr.sort()
    return arr[-1]

def tuple_intersection(list1: list, list2: list) -> set:
    """
    Returns the intersection of two lists of tuples, considering tuples as unordered pairs.

    Args:
    list1 (list): The first list of tuples.
    list2 (list): The second list of tuples.

    Returns:
    set: A set of tuples representing the intersection.
    """
    # Normalize the tuples by sorting the elements in each tuple
    set1 = {tuple(sorted(t)) for t in list1}
    set2 = {tuple(sorted(t)) for t in list2}
    
    # Return the intersection of the two sets
    return set1 & set2