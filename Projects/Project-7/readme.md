# Multi-Utility Toolkit

## Project Overview

The **Multi-Utility Toolkit** is a menu-driven Python application that demonstrates the practical use of Python built-in modules, custom modules, packages, file handling, and modular programming concepts.

The project is developed using Python packages and follows the `if __name__ == "__main__"` paradigm to separate reusable code from executable code.

The toolkit provides multiple utilities such as date and time operations, mathematical calculations, random data generation, UUID generation, file management, and dynamic module exploration.

---

# Objectives

- Explore Python built-in modules:

  - datetime
  - time
  - math
  - random
  - uuid
  - os

- Create custom Python modules and packages.

- Organize reusable code using packages and `__init__.py`.

- Implement modular programming concepts.

- Use `dir()` function for dynamic module exploration.

- Build a menu-driven console application.

- Separate reusable functions from main execution logic using:

```python
if __name__ == "__main__":
```

---

# Project Structure

```
Project_7/

│

├── main.py

│

└── MyPackage/

    │

    ├── __init__.py

    ├── datetime_module.py

    ├── time_module.py

    ├── math_module.py

    ├── random_module.py

    ├── uuid_module.py

    ├── file_module.py

    ├── explorer_module.py

    │

    └── __pycache__/

        │

        ├── datetime_module.cpython-*.pyc

        ├── time_module.cpython-*.pyc

        ├── math_module.cpython-*.pyc

        ├── random_module.cpython-*.pyc

        ├── uuid_module.cpython-*.pyc

        ├── file_module.cpython-*.pyc

        └── explorer_module.cpython-*.pyc
```

---

# Features

## 1. Datetime and Time Operations

Uses:

- datetime module
- time module

Functions include:

- Display current date and time
- Calculate difference between two dates
- Format dates using `strftime()`
- Stopwatch implementation
- Countdown timer


Example:

```
Current Date and Time:

27-06-2026 22:10:35
```

---

## 2. Mathematical Operations

Uses:

```
math module
```

Functions include:

- Factorial calculation
- Compound Interest calculation
- Trigonometric operations
- Area calculation of geometric shapes


Example:

```
Enter number:

5

Factorial:

120
```

---

## 3. Random Data Generation

Uses:

```
random module
```

Features:

- Random number generation
- Random list selection
- Random password generator
- Random OTP generator


Example:

```
Generated Password:

Ab8@Pq1Xr


Generated OTP:

483927
```

---

## 4. UUID Generation

Uses:

```
uuid module
```

Generates unique identifiers using UUID4.


Example:

```
Generated UUID:

4dd364cc-83e6-4bd6-a3a2-878b4f6f9db9
```

---

## 5. File Operations (Custom Module)

Uses:

```
os module
```

Operations:

- Create file
- Write file content
- Read file
- Append content
- Delete file


Example:

```
File created successfully!

Content written successfully!

File Content:

Hello Python

Content appended successfully!

File deleted successfully!
```

---

## 6. Module Explorer

Uses:

```
dir()
```

Allows users to explore available attributes of:

- datetime_module
- file_module
- math_module
- random_module
- uuid_module


Example:

```
Available Attributes:

['__name__',
 '__file__',
 'function_name',
 ...]
```

---

# Menu Interface

```
Welcome to Multi-Utility Toolkit

Choose an option:

1. Datetime and Time Operations

2. Mathematical Operations

3. Random Data Generation

4. Generate Unique Identifiers (UUID)

5. File Operations (Custom Module)

6. Explore Module Attributes (dir())

7. Exit
```

---

# Modules Used

| Module | Purpose |
|--------|---------|
| datetime | Date and time operations |
| time | Stopwatch and countdown |
| math | Mathematical calculations |
| random | Random generation |
| uuid | Unique identifier generation |
| os | File handling operations |

---

# Custom Package

The project contains a custom package:

```
MyPackage
```

It contains reusable modules:

```
datetime_module.py

math_module.py

random_module.py

uuid_module.py

file_module.py

explorer_module.py
```

Package initialization file:

```
__init__.py
```

The package also contains:

```
__pycache__
```

which stores automatically generated Python bytecode files after running the program.

---

# Use of if __name__ == "__main__"

Each module follows Python execution standards:

```python
if __name__ == "__main__":

    FunctionName()
```

This provides:

- Code reusability
- Module importing without execution
- Better project structure
- Separation of logic

---

# Example Outputs

## Date Difference

```
Enter first date:

01-01-2026


Enter second date:

15-01-2026


Difference:

14 days
```

---

## Compound Interest

```
Principal:

10000


Rate:

8


Time:

2


Compound Interest:

11664.0
```

---

## Random Number

```
Generated Random Number:

57
```

---

## File Management

```
File created successfully!

Content written successfully!

File deleted successfully!
```

---

# Example Use Case

A small business owner can use this toolkit for daily operations:

- Calculate working hours using time utilities.
- Generate passwords for employees.
- Create unique invoice IDs using UUID.
- Store records using file operations.
- Explore module features dynamically using `dir()`.

---

# Concepts Covered

- Python Modules
- Python Packages
- Built-in Libraries
- Custom Modules
- File Handling
- Random Data Generation
- UUID Generation
- Date and Time Handling
- Mathematical Operations
- Menu Driven Programming
- Modular Programming
- `__init__.py`
- `__pycache__`
- `dir()` Function
- `if __name__ == "__main__"`

---

# Project Summary

**Project Name:**

Multi-Utility Toolkit


**Language:**

Python


**Programming Concepts:**

- Modules
- Packages
- Standard Library
- File Handling
- Modular Design
- Console Application Development