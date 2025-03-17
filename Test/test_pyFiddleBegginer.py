from pyFiddleBegginer import *
from imports import *
import pytest

def test_add_tuple():
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]
    assert add_tuple([], (1, 2, 3)) == [1, 2, 3]
    assert add_tuple([1, 2], ()) == [1, 2]
