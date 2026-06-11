# Data Analyzer and Transformer Program

## Overview

The **Data Analyzer and Transformer Program** is a menu-driven Python application that allows users to input, analyze, filter, sort, and transform a one-dimensional dataset.

It demonstrates core Python programming concepts such as:

* Functions
* Built-in Functions
* Recursion
* Function Docstrings (`__doc__`)
* Lists
* Conditional Statements
* Loops
* Returning Multiple Values
* Exception Handling

---

## Features

### 1. Input Data

* Accepts a space-separated list of integers from the user.
* Stores values in a global dataset for further operations.

---

### 2. Display Data Summary

Uses Python built-in functions to display:

* Total number of elements
* Minimum value
* Maximum value
* Sum of all values
* Average value

---

### 3. Calculate Factorial (Recursion)

* Accepts a number from the user.
* Calculates factorial using a recursive function.
* Handles negative number validation.

---

### 4. Filter Data by Threshold

Filters dataset based on user input threshold:

* Values greater than or equal to threshold
* Values less than threshold

---

### 5. Sort Data

Provides sorting options:

* Ascending order
* Descending order

---

### 6. Display Dataset Statistics

Uses a function that returns multiple values:

* Minimum value
* Maximum value
* Total sum
* Average value

---

### 7. Exit Program

* Safely terminates the program with a goodbye message.

---

## Special Python Concepts Used

### Module-Level Docstring (`__doc__`)

The program can include a module docstring:

```python
"""
Data Analyzer and Transformer Program
"""

# <!-- The use of *args and **kwargs was not required in this program, as the implemented functionality could be achieved effectively without them. Therefore, they were intentionally omitted to maintain code simplicity and readability. -->