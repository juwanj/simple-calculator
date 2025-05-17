import math

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of a by b, or an error message if b is zero."""
    if b == 0:
        return "Oops! Cannot divide by zero."
    return a / b

def square(a):
    """Return the square of a number."""
    return a ** 2

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def sqrt(a):
    """Return the square root of a number or error if input is negative."""
    if a < 0:
        return "Oops! Can't find the square root of a negative number."
    return math.sqrt(a)
