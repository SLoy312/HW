# test_mycode.py
from mycode import david_function


def test_function_david():
    assert david_function(2) == 1
    assert david_function(10) == 1
    assert david_function(5) == 1
    assert david_function(7) == 1