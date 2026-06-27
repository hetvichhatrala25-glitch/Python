import MyPackage.datetime_module as datetime_module
import MyPackage.file_module as file_module
import MyPackage.math_module as math_module
import MyPackage.random_module as random_module
import MyPackage.uuid_module as uuid_module

def ExploreModuleMenu():
    while True:
        print("\nExplore Module Attributes:")
        print("Enter 1 to explore datetime module")
        print("Enter 2 to explore file module")
        print("Enter 3 to explore math module")
        print("Enter 4 to explore random module")
        print("Enter 5 to explore uuid module")
        print("Enter 6 to go back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nAvailable Attributes in datetime module:")
            print(dir(datetime_module))

        elif choice == 2:
            print("\nAvailable Attributes in file module:")
            print(dir(file_module))

        elif choice == 3:
            print("\nAvailable Attributes in math module:")
            print(dir(math_module))

        elif choice == 4:
            print("\nAvailable Attributes in random module:")
            print(dir(random_module))

        elif choice == 5:
            print("\nAvailable Attributes in uuid module:")
            print(dir(uuid_module))

        elif choice == 6:
            break

        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    ExploreModuleMenu()