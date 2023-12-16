# test_math_operations.py

# Import the module (assuming it's in the root folder)
# from ..math_operations import add, subtract  # Import specific functions or elements from the module

# Your test functions using the imported module functions
from math_operations import add, subtract


def test_addition():
    result = add(3, 5)
    assert result == 8

def test_subtraction():
    result = subtract(10, 4)
    assert result == 6
