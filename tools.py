# CS50 Python Full Guide - Practical and In-Depth Examples in One File
# Save this file as cs50_python_guide.py and run sections individually

"""
    This guide provides a comprehensive overview of Python programming concepts, from basic syntax to advanced topics.
    Each section includes practical examples and explanations to help you understand the concepts better.
"""

# --- 1. Introduction to Python ---
print("Section 1: Introduction to Python")
print("Hello, world!")  # Your first Python program
# Output:
# Section 1: Introduction to Python
# Hello, world!


















# --- 2. Variables and Data Types ---
print("\nSection 2: Variables and Data Types")
name = "Alice"
age = 25
pi = 3.14
is_student = True
print(f"{name}, Age: {age}, Pi: {pi}, Student: {is_student}","","",sep=", ",end="")
# Output:
# Section 2: Variables and Data Types
# Alice, Age: 25, Pi: 3.14, Student: True


# Type Conversion
age_str = str(age)
age_int = int("30")
print(f"Converted age: {age_str} (str), Parsed age: {age_int} (int)")
# Output:
# Converted age: 25 (str), Parsed age: 30 (int)
















# --- 3. Control Flow ---
print("\nSection 3: Control Flow")
num = -2
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")
# Output:
# Section 3: Control Flow
# Negative

# For Loop
for i in range(3):
    print(f"For loop iteration: {i}")
# Output:
# For loop iteration: 0
# For loop iteration: 1
# For loop iteration: 2

# While Loop
count = 3
while count > 0:
    print(f"While loop countdown: {count}")
    count -= 1
# Output:
# While loop countdown: 3
# While loop countdown: 2
# While loop countdown: 1

# Using match-case (introduced in Python 3.10) to handle different command values
match "command":
    
    # If command is "start", execute this block
    case "start":
        print("Starting...")
    # If command is "stop", execute this block
    case "stop":
        print("Stopping...")
    # If command is "pause", execute this block
    case "pause":
        print("Paused.")
    # Default case: if command doesn't match any above
    case _:
        print("Unknown command")








# --- 4. Functions ---
print("\nSection 4: Functions")

def greet(name):
    """Prints a greeting message"""
    print(f"Hello, {name}!")

def square(n):
    """Returns the square of a number"""
    return n * n

greet("Bob")
print(f"Square of 4 is: {square(4)}")
# Output:
# Section 4: Functions
# Hello, Bob!
# Square of 4 is: 16












# --- 5. Data Structures ---
print("\nSection 5: Data Structures")

# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
# Output:
# Section 5: Data Structures
# I like apple
# I like banana
# I like cherry

# List: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()

# Tuple
person = ("Alice", 25)
name, age = person  # Tuple unpacking
print(f"{name} is {age} years old")
# Output:
# Alice is 25 years old

# Tuple: count(), index()


# Dictionary
grades = {"Alice": 90, "Bob": 85}
for student, score in grades.items():
    print(f"{student}: {score}")
# Output:
# Alice: 90
# Bob: 85
# Dictionary: get(), keys(), values(), items(), update(), pop(), popitem(), clear(), setdefault()

# Set
unique_numbers = {1, 2, 2, 3}
for num in unique_numbers:
    print(f"Unique number: {num}")
# Output:
# Unique number: 1
# Unique number: 2
# Unique number: 3

# Set: add(), update(), remove(), discard(), pop(), clear(), copy(), union(), intersection(), difference(), issubset(), issuperset()


# List comprehension
for x in range(5):
        x * x

squares = [x * x for x in range(5)]
print(f"Squares: {squares}")
# Output:
# Squares: [0, 1, 4, 9, 16]













# --- 6. Modules and Libraries ---
print("\nSection 6: Modules and Libraries")

import random

names = ["Alice", "Bob", "Charlie"]
for _ in range(3):
    print(f"Random name: {random.choice(names)}")
# Output: (Example, will vary due to randomness)
# Section 6: Modules and Libraries
# Random name: Charlie
# Random name: Bob
# Random name: Alice















import math
print(f"Square root of 16 is: {math.sqrt(16)}")
# Output:
# Square root of 16 is: 4.0






















# --- 7. File I/O ---
print("\nSection 7: File I/O")

# Writing to file
with open("output.txt", "w") as file:
    file.write("Hello from Python!\n")

# Reading from file
with open("output.txt", "r") as file:
    for line in file:
        print(f"File content: {line.strip()}")
# Output:
# Section 7: File I/O
# File content: Hello from Python!
















# --- 8. Exception Handling ---
print("\nSection 8: Exception Handling")

try:
    x = int("not a number")
except ValueError:
    print("Caught a ValueError!")
else :
    print("No exceptions occurred.")
# Output:
# Section 8: Exception Handling
# Caught a ValueError!





















# --- 9. Object-Oriented Programming ---
print("\nSection 9: Object-Oriented Programming")

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}")

class Student(Person):
    def greet(self):
        print(f"I'm a student named {self.name}")

p = Person("Alice")
p.greet()

s = Student("Bob")
s.greet()
# Output:
# Section 9: Object-Oriented Programming
# Hi, I'm Alice
# I'm a student named Bob


















# --- 10. Testing and Debugging ---
print("\nSection 10: Testing and Debugging")

def reverse_list(lst):
    return lst[::-1]

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    print("Test passed!")

test_reverse_list()
# Output:
# Section 10: Testing and Debugging
# Test passed!

# --- 11. Command-Line Arguments ---
print("\nSection 11: Command-Line Arguments")

import sys
print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
# Output: (Example if run as `python cs50_python_guide.py arg1 arg2`)
# Section 11: Command-Line Arguments
# Script name: cs50_python_guide.py
# Arguments: ['arg1', 'arg2']

# --- 12. Practical Application: Word Counter ---
print("\nSection 12: Practical Application - Word Counter")

def word_count(text):
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

sample_text = "hello world hello python python world"
counts = word_count(sample_text)
print("Word Frequencies:")
for word, count in counts.items():
    print(f"{word}: {count}")
# Output:
# Section 12: Practical Application - Word Counter
# Word Frequencies:
# hello: 2
# world: 2
# python: 2

# --- 13. Advanced: Decorators ---
print("\nSection 13: Advanced - Decorators")

import time

def timer(func):
    """A decorator that times the execution of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """A function that takes a while to execute."""
    time.sleep(2)

slow_function()
# Output: (Will vary slightly depending on system)
# Section 13: Advanced - Decorators
# Function slow_function took 2.0008 seconds

# --- 14. Advanced: Generators ---
print("\nSection 14: Advanced - Generators")

def fibonacci_generator(n):
    """A generator that yields the Fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_generator(10):
    print(num)
# Output:
# Section 14: Advanced - Generators
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

# --- 15. Advanced: Context Managers ---
print("\nSection 15: Advanced - Context Managers")

class FileContextManager:
    """A context manager for file operations."""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileContextManager("example.txt", "w") as f:
    f.write("Hello, context manager!")

with open("example.txt", "r") as f:
    print(f.read())
# Output:
# Section 15: Advanced - Context Managers
# Hello, context manager!

# --- 16. Advanced: Lambda Functions ---
print("\nSection 16: Advanced - Lambda Functions")

# A lambda function to square a number
square = lambda x: x * x
print(f"Square of 5 is: {square(5)}")

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(f"Squared numbers: {squared_numbers}")
# Output:
# Section 16: Advanced - Lambda Functions
# Square of 5 is: 25
# Squared numbers: [1, 4, 9, 16, 25]

# --- 17. Advanced: Regular Expressions ---
print("\nSection 17: Advanced - Regular Expressions")

import re

text = "My phone number is 123-456-7890 and another one is 987-654-3210."
phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(f"Phone numbers found: {phone_numbers}")

email = "Contact us at support@example.com or sales@company.net"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email)
print(f"Emails found: {emails}")
# Output:
# Section 17: Advanced - Regular Expressions
# Phone numbers found: ['123-456-7890', '987-654-3210']
# Emails found: ['support@example.com', 'sales@company.net']

# --- 18. Advanced: Data Serialization (JSON) ---
print("\nSection 18: Advanced - Data Serialization (JSON)")

import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data)
print(f"JSON string: {json_string}")

# Convert JSON string back to Python dictionary
python_dict = json.loads(json_string)
print(f"Python dictionary: {python_dict}")

#Writing JSON to a file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4) #indent makes the JSON file readable

#Reading JSON from a file
with open('data.json', 'r') as infile:
    loaded_data = json.load(infile)
    print(f"Loaded from file: {loaded_data}")
# Output:
# Section 18: Advanced - Data Serialization (JSON)
# JSON string: {"name": "John Doe", "age": 30, "city": "New York"}
# Python dictionary: {'name': 'John Doe', 'age': 30, 'city': 'New York'}
# Loaded from file: {'name': 'John Doe', 'age': 30, 'city': 'New York'}

# --- 19. Advanced: Working with Dates and Times ---
print("\nSection 19: Advanced - Working with Dates and Times")

import datetime

# Get current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Format the date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")

# Create a specific date
specific_date = datetime.datetime(2024, 1, 1)
print(f"Specific date: {specific_date}")

#Date arithmetic
future_date = now + datetime.timedelta(days=7)
print(f"Date in 7 days: {future_date}")
# Output: (Will vary depending on current time)
# Section 19: Advanced - Working with Dates and Times
# Current date and time: 2023-11-17 16:35:00.123456
# Formatted date: 2023-11-17 16:35:00
# Specific date: 2024-01-01 00:00:00
# Date in 7 days: 2023-11-24 16:35:00.123456

# --- 20. Advanced: Using the `requests` Library for API Interaction ---
print("\nSection 20: Advanced - Using the `requests` Library for API Interaction")

import requests

try:
    # Make a GET request
    response = requests.get("https://api.github.com") #A simple public API
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    # Parse the JSON response
    data = response.json()
    print(f"API Response: {data}")

except requests.exceptions.RequestException as e:
    print(f"Error during API request: {e}")

# Output: (Will vary depending on the API's current response)
# Section 20: Advanced - Using the `requests` Library for API Interaction
# API Response: {'current_user_url': 'https://api.github.com/user', ...} #Truncated for brevity


# --- 21. Multithreading and Multiprocessing ---
print("\nSection 21: Multithreading and Multiprocessing")

import threading
import multiprocessing
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(1)  # Simulate some work
    print(f"Task {name} finished")

# Multithreading
print("\nMultithreading:")
threads = []
for i in range(2):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # Wait for all threads to complete

# Multiprocessing
print("\nMultiprocessing:")
processes = []
for i in range(2):
    p = multiprocessing.Process(target=task, args=(f"Process-{i}",))
    processes.append(p)
    p.start()

for p in processes:
    p.join()  # Wait for all processes to complete

print("All tasks finished")

# Output will be interleaved and order may vary:
# Section 21: Multithreading and Multiprocessing
#
# Multithreading:
# Task Thread-0 started
# Task Thread-1 started
# Task Thread-0 finished
# Task Thread-1 finished
#
# Multiprocessing:
# Task Process-0 started
# Task Process-1 started
# Task Process-0 finished
# Task Process-1 finished
# All tasks finished

# Key Differences:
# - Threads share the same memory space (GIL limitations).
# - Processes have separate memory spaces (more overhead, but can bypass GIL).
# - Multiprocessing is generally better for CPU-bound tasks, multithreading for I/O-bound.

# --- 22.  Virtual Environments ---

print("\nSection 22: Virtual Environments")
print("  -  Virtual environments are used to isolate project dependencies.")
print("  -  Use `python3 -m venv myenv` to create a virtual environment.")
print("  -  Activate it with `source myenv/bin/activate` (Linux/macOS) or `myenv\\Scripts\\activate` (Windows).")
print("  -  Install packages using `pip install <package_name>`.")
print("  -  Deactivate it with `deactivate`.")
print("  -  It's crucial for managing dependencies and reproducibility.")
# No direct code execution, as it involves external command-line usage.
# Output:
# Section 22: Virtual Environments
#   -  Virtual environments are used to isolate project dependencies.
#   -  Use `python3 -m venv myenv` to create a virtual environment.
#   -  Activate it with `source myenv/bin/activate` (Linux/macOS) or `myenv\Scripts\activate` (Windows).
#   -  Install packages using `pip install <package_name>`.
#   -  Deactivate it with `deactivate`.
#   -  It's crucial for managing dependencies and reproducibility.