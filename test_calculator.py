import calculator
import math

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 4) == -4

def test_multiply():
    assert calculator.multiply(4, 5) == 20
    assert calculator.multiply(-2, 3) == -6

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(5, 0) == "Oops! Cannot divide by zero."

def test_square():
    assert calculator.square(4) == 16
    assert calculator.square(-3) == 9

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1

def test_sqrt():
    assert math.isclose(calculator.sqrt(9), 3.0)
    assert calculator.sqrt(-1) == "Oops! Can't find the square root of a negative number."
