# Data Analyzer and Transformer Program

## Overview

The **Data Analyzer and Transformer Program** is a menu-driven Python application that allows users to input, analyze, filter, and sort numerical data. The program demonstrates the use of important Python concepts such as:

* Functions
* Built-in Functions
* Recursion
* Function Docstrings (`__doc__`)
* Lists
* Conditional Statements
* Loops
* Returning Multiple Values

---

## Features

### 1. Input Data

* Accepts a one-dimensional array of integers from the user.
* Stores the values in a dataset for later processing.

### 2. Display Data Summary

Uses Python built-in functions to display:

* Total number of elements
* Minimum value
* Maximum value
* Sum of all values
* Average value

### 3. Calculate Factorial (Recursion)

* Accepts a number from the user.
* Calculates its factorial using a recursive function.

### 4. Filter Data by Threshold

Filters dataset values based on a threshold:

* Values greater than or equal to the threshold
* Values less than the threshold

### 5. Sort Data

Provides sorting options:

* Ascending Order
* Descending Order

### 6. Display Dataset Statistics

Uses a function that returns multiple values:

* Minimum value
* Maximum value
* Total sum
* Average value

### 7. Exit Program

* Safely terminates the application.

---

## Special Python Concepts Used

### Module Docstring (`__doc__`)

The program begins with a module-level docstring:

```python
"""
Data Analyzer and Transformer Program
"""
```

This docstring is displayed using:

```python
print(__doc__)
```

### Function Docstrings

Each function contains its own docstring describing its purpose:

```python
def input_data():
    """Input data into the dataset."""
```

The docstring is displayed using:

```python
print(input_data.__doc__)
```

---

## Program Flow

1. Display program documentation.
2. Show the main menu.
3. Allow the user to select an operation.
4. Execute the corresponding function.
5. Return to the main menu until the user chooses Exit.

---

## Requirements

* Python 3.x
* No external libraries required

---

## How to Run

Save the program as:

```text
data_analyzer.py
```

Run the program using:

```bash
python data_analyzer.py
```

---

## Sample Input

```text
Enter data for a 1D array (separated by spaces):
10 20 30 40 50
```

## Sample Output

```text
Total elements: 5
Minimum value: 10
Maximum value: 50
Sum of all values: 150
Average value: 30.0
```

---

## Learning Outcomes

This project demonstrates:

* Menu-driven programming
* Function creation and invocation
* Recursive functions
* Use of built-in functions
* Data filtering techniques
* Sorting operations
* Returning multiple values from functions
* Using `__doc__` for documentation

---

## Author

Developed as a Python practical project for learning data analysis and function-based programming concepts.
<!-- The use of *args, **kwargs, and the global keyword was not required in this program, as the implemented functionality could be achieved effectively without them. Therefore, they were intentionally omitted to maintain code simplicity and readability. -->