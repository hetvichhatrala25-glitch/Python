# Personal Journal Manager

## Project Overview

Personal Journal Manager is a menu-driven Python application that allows users to create, view, search, and manage personal journal entries stored in a text file. The project demonstrates Object-Oriented Programming (OOP), file handling operations, exception handling, and user interaction through a console-based interface.

The application stores all journal entries in a file named **journal.txt**.

---

# Objectives

This project is designed to demonstrate:

* Object-Oriented Programming (OOP)
* File handling operations
* Exception handling
* Menu-driven programming
* Reading and writing text files
* User input validation

---

# Features

## 1. Add a New Entry

Users can:

* Enter a date
* Enter a time
* Enter multiple journal entries separated by commas

The program stores the entries in **journal.txt** using append mode (`a`).

### Example

**Input**

```text
Date: 15-06-2026
Time: 10:30
Entries:
Completed assignment, Learned Python OOP, Practiced file handling
```

**Stored Output**

```text
[15-06-2026 10:30]
1. Completed assignment
2. Learned Python OOP
3. Practiced file handling
```

---

## 2. View All Entries

Displays all journal entries stored in the journal file.

If the file is empty, the program displays:

```text
Your journal is empty.
```

---

## 3. Search for an Entry

Users can search journal entries by:

* Keyword
* Date

The program displays all matching lines.

### Example

**Search Keyword**

```text
Python
```

**Output**

```text
2. Learned Python OOP
```

---

## 4. Delete All Entries

Users are prompted for confirmation before deletion.

### Example

```text
Are you sure you want to delete all entries? (yes/no):
```

If the user enters:

```text
yes
```

All journal contents are cleared.

---

## 5. Exit Program

Safely terminates the application.

---

# Object-Oriented Design

The application is built using the `JournalManager` class.

## Class

```python
class JournalManager
```

### Methods

| Method               | Description                      |
| -------------------- | -------------------------------- |
| `__init__()`         | Initializes the journal file     |
| `AddNewEntry()`      | Adds a new journal entry         |
| `ViewAllEntries()`   | Displays all entries             |
| `SearchEntry()`      | Searches entries by keyword/date |
| `DeleteAllEntries()` | Deletes all journal entries      |
| `ExitProgram()`      | Exits the program                |

---

# File Handling Modes Used

## Read Mode (`r`)

Used for:

* Viewing entries
* Searching entries

Example:

```python
open("journal.txt", "r")
```

---

## Write Mode (`w`)

Used for:

* Clearing all journal entries

Example:

```python
open("journal.txt", "w")
```

---

## Append Mode (`a`)

Used for:

* Adding new entries

Example:

```python
open("journal.txt", "a")
```

---

## Create Mode (`x`)

Used for:

* Creating the journal file if it does not exist

Example:

```python
open("journal.txt", "x")
```

---

# Exception Handling

The program handles several exceptions to prevent crashes.

## FileExistsError

Occurs when attempting to create a file that already exists.

Handled in:

```python
__init__()
```

---

## FileNotFoundError

Occurs when attempting to read a file that does not exist.

Handled in:

* ViewAllEntries()
* SearchEntry()
* DeleteAllEntries()

---

## PermissionError

Occurs when the program does not have permission to access the file.

Handled in:

* File creation
* File reading
* File writing
* File deletion

---

## ValueError

Occurs when the user enters invalid menu input.

Example:

```text
abc
```

instead of:

```text
1
```

The program displays:

```text
Invalid input. Please enter a number between 1 and 5.
```

---

# Program Workflow

```text
Start Program
      │
      ▼
Display Main Menu
      │
      ▼
User Selects Option
      │
      ├── Add Entry
      ├── View Entries
      ├── Search Entries
      ├── Delete Entries
      └── Exit
      │
      ▼
Return to Menu
      │
      ▼
Exit Program
```

---

# File Structure

```text
PersonalJournalManager/
│
├── main.py
├── journal.txt
└── README.md
```

---

# Requirements

* Python 3.x
* No external libraries required

---

# How to Run

## Step 1

Save the source code as:

```text
main.py
```

## Step 2

Open Command Prompt or Terminal.

## Step 3

Navigate to the project folder.

```bash
cd PersonalJournalManager
```

## Step 4

Run the program.

```bash
python main.py
```

---

# Sample Menu

```text
Welcome Menu:
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

---

# Learning Outcomes

After completing this project, the following concepts are demonstrated:

* Object-Oriented Programming
* Classes and Objects
* Methods
* File Handling
* Text File Management
* Exception Handling
* User Input Validation
* Menu-Driven Applications

---

# Author

Personal Journal Manager Project

Developed using Python and Object-Oriented Programming concepts.

---

# License

This project is intended for educational and learning purposes.
