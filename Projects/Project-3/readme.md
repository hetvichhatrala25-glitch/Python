# Student Data Organizer

## Overview

Student Data Organizer is a simple Python console-based application that helps manage student records. Users can add, view, update, and delete student information while maintaining a list of unique subjects offered.

## Features

* Add new student records
* Display all student records
* Update student information:

  * Name
  * Age
  * Grade
  * Subjects
* Delete student records
* View all unique subjects offered
* User-friendly menu-driven interface
* Basic input validation for menu choices

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Sets
* Loops and Conditional Statements
* Exception Handling

## Data Structure

Each student is stored as a dictionary:

```python
{
    "id": 1,
    "name": "John",
    "age": 15,
    "grade": "10th",
    "subjects": ["Math", "Science", "English"]
}
```

### Student Collection

```python
students = []
```

### Subjects Collection

```python
subjects_offered = set()
```

## Menu Options

### 1. Add Student

Allows the user to enter:

* Name
* Age
* Grade
* Subjects (comma-separated)

Example:

```text
Name: John
Age: 15
Grade: 10th
Subjects: Math, Science, English
```

### 2. Display All Students

Displays all stored student records.

Example:

```text
Student ID : 1
Name       : John
Age        : 15
Grade      : 10th
Subjects   : Math, Science, English
```

### 3. Update Student Information

Update any of the following:

* Name
* Age
* Grade
* Subjects

### 4. Delete Student

Delete a student record using Student ID.

### 5. Display Subjects Offered

Shows all unique subjects available in the system.

Example:

```text
English
Math
Science
```

### 6. Exit

Closes the application.

## How to Run

1. Install Python 3.
2. Save the program as:

```text
student_data_organizer.py
```

3. Open a terminal or command prompt.
4. Navigate to the project directory.
5. Run the program:

```bash
python student_data_organizer.py
```

## Sample Workflow

```text
Welcome to Student Data Organizer

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice: 1

Enter Student Details
Name: Alice
Age: 16
Grade: 11th
Subjects: Physics, Chemistry, Mathematics

Student added successfully!
```

## Future Improvements

* Save data to a file (JSON/CSV)
* Load records automatically when the program starts
* Search students by name or ID
* Sort students by grade or age
* Better input validation
* Graphical User Interface (GUI)
* Database integration using SQLite or MySQL

## Author

Developed as a Python practice project for learning:

* Lists
* Dictionaries
* Sets
* CRUD Operations
* Exception Handling
* Menu-Driven Programming
