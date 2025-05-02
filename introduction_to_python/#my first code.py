# Python Beginner's Guide

# 1. Hello World: Your First Python Program
print("Hello World")

# 2. Variables and Dynamic Typing
# Python allows dynamic typing, unlike C#. You can assign different 
# types to the same variable.
x = 10
print(f"x is an integer: {x}")
x = "Now I'm a string"
print(f"x is now a string: {x}")

# 3. Control Structures: Loops and Indentation
# Python uses indentation for blocks instead of braces.
for i in range(3):
    print(f"Loop iteration {i}")

# 4. Data Structures: Lists and Dictionaries
# Python has built-in support for lists, dictionaries, and other data 
# structures.
my_list = [1, 2, 3]
my_dict = {"key": "value", "another_key": 42}
print(f"List: {my_list}, Dictionary: {my_dict}")

# 5. List Comprehensions
# Python supports list comprehensions for concise and readable code.
squared_numbers = [x**2 for x in range(5)]
print(f"Squared numbers: {squared_numbers}")

# 6. Making HTTP Requests
# Python has a rich set of libraries and frameworks for various tasks.
# For example, you can use the requests library to make HTTP requests.
import requests

response = requests.get("https://api.github.com")
print(f"Response from GitHub API: {response.status_code}")

# 7. Functions
# Define a simple function
def add(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

# Example usage
print(f"2 + 3 = {add(2, 3)}")

# 8. Unit Testing with unittest
# Python has a built-in module called unittest for unit testing.
import unittest

# Create a test case by subclassing unittest.TestCase
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)  # Test if 2 + 3 equals 5
        self.assertEqual(add(-1, 1), 0)  # Test if -1 + 1 equals 0
        self.assertEqual(add(0, 0), 0)  # Test if 0 + 0 equals 0

# 9. Advanced: Using Decorators
import functools

# Decorator to log function calls
def log_function_call(func):
    """Decorator to log function calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

@log_function_call
def greet(name, greeting="Hello"):
    """Greet a person with a name and an optional greeting."""
    return f"{greeting}, {name}!"

# Test the decorated functions
print(multiply(6, 50))
print(greet("Alice"))

# 10. Classes and Object-Oriented Programming
# Example of a class with methods
class Calculator:
    def __init__(self, precision=2):
        """Initialize the calculator with a default precision."""
        self.precision = precision

    def add(self, a, b):
        """Add two numbers with the specified precision."""
        return round(a + b, self.precision)

    def subtract(self, a, b):
        """Subtract two numbers with the specified precision."""
        return round(a - b, self.precision)

    def multiply(self, a, b, scale=1):
        """Multiply two numbers with the specified precision and scale."""
        return round((a * b) * scale, self.precision)

    def divide(self, a, b, safe_mode=True):
        """Divide two numbers with the specified precision and safe mode."""
        if safe_mode and b == 0:
            return "Error: Division by zero"
        return round(a / b, self.precision)

# Example usage
calc = Calculator(precision=3)
print(calc.add(1.2345, 2.3456))  # Default precision of 3
print(calc.divide(10, 0))  # Safe mode prevents division by zero

# 11. Keyword Arguments and Variable-Length Arguments
class Person:
    def __init__(self, name, age):
        """Initialize a person with a name and age."""
        self.name = name
        self.age = age

    def introduce(self, greeting="Hello"):
        """Introduce the person with an optional greeting."""
        return f"{greeting}, my name is {self.name} and I am \
        {self.age} years old."

person = Person("Alice", 30)
print(person.introduce())  # Default greeting

class Logger:
    def log(self, *messages):
        """Log messages to the console."""
        for message in messages:
            print(f"Log: {message}")

logger = Logger()
logger.log("This is a log message.")

# 12. Keyword-Only Arguments
class Config:
    def __init__(self, **kwargs):
        """Initialize configuration with keyword arguments."""
        self.settings = kwargs

    def get_setting(self, key, default=None):
        """Get a setting value by key, with a default value."""
        return self.settings.get(key, default)

# 13. Testing with pytest
# Pytest is a popular testing framework that is simpler and more 
# flexible than unittest.
# Define the same function to test
def add(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b

# Write test functions using pytest
def test_add_positive_numbers():
    """Test the add function with positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test the add function with negative numbers."""
    assert add(-1, -1) == -2

def test_add_zero():
    """Test the add function with zero."""
    assert add(0, 0) == 0

# To run these tests, save the file and execute `pytest <filename>.py` 
# in the terminal.

# 14. CPU vs GPU Processing with NumPy and CuPy
import numpy as np
import cupy as cp

try:
    gpu_available = True
except ImportError:
    gpu_available = False
    print("CuPy is not installed. GPU processing will not be available.")

def process_on_cpu(data):
    """Process data on the CPU using NumPy."""
    return np.sum(data ** 2)

def process_on_gpu(data):
    """Process data on the GPU using CuPy."""

    data_gpu = cp.array(data)
    result_gpu = cp.sum(data_gpu ** 2)
    return cp.asnumpy(result_gpu)

# Example usage
data = np.random.rand(1000000)  # Generate random data

if gpu_available:
    print("Processing on GPU...")
    result = process_on_gpu(data)
else:
    print("Processing on CPU...")
    result = process_on_cpu(data)

print(f"Result: {result}")

# 15. Running Tests
# Run the tests
if __name__ == "__main__":
    unittest.main()