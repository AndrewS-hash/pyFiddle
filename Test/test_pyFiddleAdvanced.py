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
