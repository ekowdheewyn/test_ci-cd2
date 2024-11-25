# test.py

def add(a, b):
    """
    A simple function that adds two numbers.
    """
    return a + b

def test_add():
    """
    Test case for the add function.
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
