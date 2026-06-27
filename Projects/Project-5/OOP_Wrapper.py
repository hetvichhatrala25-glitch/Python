class Employee:
    
    def __init__(self, name=None, age=None, emp_id=None, salary=30000):
        self.name = name
        self.age = age
        self.__emp_id = emp_id
        self.__salary = salary
        
    def get_emp_id(self):
        return self.__emp_id
    
    def get_salary(self):
        return self.__salary
    
    def set_emp_id(self,emp_id):
        self.__emp_id = emp_id
        
    def set_salary(self,salary):
        self.__salary = salary
        
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Employee ID :",self.get_emp_id())
        print("Salary :",self.get_salary())
        
    def __del__(self):
        print("Employee Deleted")
        

class Manager(Employee):
    
    def __init__(self,name,age,emp_id,salary,department):
        super().__init__(name,age,emp_id,salary)
        self.department = department
        
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Employee ID :",self.get_emp_id())
        print("Salary :",self.get_salary())
        print("Department :",self.department)
        

class Developer(Employee):
    
    def __init__(self,name,age,emp_id,salary,language):
        super().__init__(name,age,emp_id,salary)
        self.language = language
        
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Employee ID :",self.get_emp_id())
        print("Salary :",self.get_salary())
        print("Programming Language :",self.language)
        
print("Manager is Employee's child:", issubclass(Manager, Employee))
print("Developer is Employee's child:", issubclass(Developer, Employee))

        
emp = []
man = []
dev = []


while True:
    
    print("\n---Employee Management System---")
    print("Enter 1 to create Employee")
    print("Enter 2 to create Manager")
    print("Enter 3 to create Developer")
    print("4. Show Details")
    print("5. Exit")
     
    choice = int(input("Enter your choice: "))


    if choice == 1:

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = "Emp" + str(len(emp)+1)
        salary = int(input("Enter salary: "))

        empl = Employee(name,age,emp_id,salary)
        emp.append(empl)

        print("Employee created successfully")


    elif choice == 2:
    
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = "Man" + str(len(man)+1)
        salary = int(input("Enter salary: "))
        department = input("Enter department: ")

        manger = Manager(name,age,emp_id,salary,department)
        man.append(manger)

        print("Manager created successfully")


    elif choice == 3:

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = "Dev" + str(len(dev)+1)
        salary = int(input("Enter salary: "))
        language = input("Enter programming language: ")

        devper = Developer(name,age,emp_id,salary,language)
        dev.append(devper)

        print("Developer created successfully")


    elif choice == 4:
    
    
        print("\nShow Details of:")
        print("Enter 1 to show Employee details")
        print("Enter 2 to show Manager details")
        print("Enter 3 to show Developer details")

        ch = int(input("Enter your choice: "))


        if ch == 1:

            print("\nEmployees Details")

            if len(emp) == 0:
                print("Not found")

            for empl in emp:
                empl.display()


        elif ch == 2:

            print("\nManagers Details")

            if len(man) == 0:
                print("Not Found")

            for manger in man:
                manger.display()


        elif ch == 3:

            print("\nDevelopers Details")

            if len(dev) == 0:
                print("Not found")

            for devper in dev:
                devper.display()


        else:
            print("Invalid choice")

    elif choice == 5:
    
        print("Exit")
        break


    else:
        print("Invalid choice")