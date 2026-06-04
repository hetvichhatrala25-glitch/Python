# Pattern Generator and Number Analyzer

## Overview

This Python program provides a simple menu-driven interface that allows users to:

1. Generate a star (`*`) pattern based on a specified number of rows.
2. Analyze a range of numbers by determining whether each number is even or odd and calculating their total sum.
3. Exit the application.

The program uses loops, conditional statements, and user input handling to demonstrate basic Python programming concepts.

---

## Features

### 1. Pattern Generator
- Accepts a positive integer as the number of rows.
- Generates a right-angled triangle pattern using asterisks (`*`).
- Validates that the number of rows is greater than zero.

**Example:**

Input:
```
5
```

Output:
```
*
**
***
****
*****
```

---

### 2. Number Range Analyzer
- Accepts a starting and ending number.
- Identifies each number in the range as **Even** or **Odd**.
- Calculates and displays the sum of all numbers within the range.
- Validates that the ending number is not less than the starting number.

**Example:**

Input:
```
Start: 1
End: 5
```

Output:
```
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd

Sum of all numbers from 1 to 5 is: 15
```

---

### 3. Exit Option
- Safely terminates the program.
- Displays a farewell message before exiting.

---

## Requirements

- Python 3.x

No external libraries are required.

---

## How to Run

1. Save the program as `pattern_number_analyzer.py`.
2. Open a terminal or command prompt.
3. Navigate to the file location.
4. Run the program using:

```bash
python pattern_number_analyzer.py
```

---

## Menu Structure

```
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
```

---

## Input Validation

### Pattern Generator
- If the number of rows is less than or equal to zero:
```
Invalid row count! Rows must be positive.
```

### Number Analyzer
- If the ending value is smaller than the starting value:
```
Error! End number must be greater than or equal to start.
```

### Invalid Menu Choice
- If the user enters an unsupported option:
```
Invalid choice! Please select a valid option.
```

---

## Concepts Demonstrated

- `while` loops
- `for` loops
- Nested loops
- Conditional statements (`if`, `elif`, `else`)
- User input handling
- Data validation
- Arithmetic operations
- String formatting with f-strings

---

## Sample Program Flow

```
Welcome to the Pattern Generator and Number Analyzer!

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 1
Enter the number of rows for the pattern: 4

Pattern:
*
**
***
****

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit

Enter your choice: 3

Thank you for using the Student Data Organizer.
Exiting the program. Goodbye!
```

---

## Author

Created as a beginner-friendly Python project to practice loops, conditionals, and menu-driven programming.