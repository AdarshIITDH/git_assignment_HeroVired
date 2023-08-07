import pytest
from CalculatorPlus import Calculator  # Assuming your Calculator class is in a file named calculator.py

def test_add():
    calculator = Calculator()
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 5) == 4
    assert calculator.add(0, 0) == 0

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 7) == 3
    assert calculator.subtract(0, 0) == 0

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(5, -2) == -10
    assert calculator.multiply(0, 0) == 0

def test_divide():
    calculator = Calculator()
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(0, 1) == 0

    # Test division by zero - it should raise a ValueError
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

def test_square_root():
    calculator = Calculator()
    assert calculator.square_root(25) == 5
    assert calculator.square_root(9) == 3
    assert calculator.square_root(0) == 0

    # Test square root of a negative number - it should raise a ValueError
    with pytest.raises(ValueError):
        calculator.square_root(-1)
