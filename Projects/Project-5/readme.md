# Employee Management System

## Project Description

Employee Management System is a Python project based on Object-Oriented Programming (OOP) concepts.

This program allows users to create and manage different types of employees:
- Employee
- Manager
- Developer

The program uses a menu-driven interface where users can create records and display details.

---

## Features

- Create Employee
- Create Manager
- Create Developer
- Display Employee details
- Display Manager details
- Display Developer details
- Automatic Employee ID generation
- Exit program from menu

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## Project Structure

```
Employee-Management-System
│
├── employee_management.py
│
└── README.md
```

---

# OOP Concepts Used

## 1. Class and Object

Three classes are created:

### Employee (Base Class)

Stores:

- Name
- Age
- Employee ID
- Salary

### Manager (Derived Class)

Additional attribute:

- Department

### Developer (Derived Class)

Additional attribute:

- Programming Language

---

## 2. Constructor

Constructor is used to initialize object values.

Example:

```python
def __init__(self, name=None, age=None, emp_id=None, salary=30000):
```

Default values allow creating objects in different ways.

---

## 3. Encapsulation

Sensitive data is kept private:

```python
__emp_id
__salary
```

Getter and setter methods are used to access and modify values.

Getter methods:

```python
get_emp_id()
get_salary()
```

Setter methods:

```python
set_emp_id()
set_salary()
```

---

## 4. Inheritance

Manager and Developer inherit from Employee.

Example:

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

---

## 5. Method Overriding

The `display()` method is overridden in child classes.

Employee:

```python
display()
```

Manager:

```python
display()
```

Developer:

```python
display()
```

Each class displays its own details.

---

## 6. super() Method

`super()` is used to call the parent class constructor.

Example:

```python
super().__init__(name,age,emp_id,salary)
```

---

## 7. issubclass()

Used to check inheritance relationship.

Example:

```python
issubclass(Manager, Employee)
```

Output:

```
True
```

---

## 8. Destructor

Destructor is used when an object is deleted.

Example:

```python
def __del__(self):
```

---

## Automatic Employee ID

Employee IDs are created automatically using `len()`.

Examples:

Employee:

```
Emp1
Emp2
```

Manager:

```
Man1
Man2
```

Developer:

```
Dev1
Dev2
```

---

## Menu Options

```
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit
```

---

## How to Run

1. Install Python

2. Open terminal

3. Run:

```bash
python employee_management.py
```

---

## Example Output

```
---Employee Management System---

Enter 1 to create Employee
Enter 2 to create Manager
Enter 3 to create Developer
Enter 4 to Show Details
Enter 5 to Exit
```

---

## Author

Employee Management System Project
```