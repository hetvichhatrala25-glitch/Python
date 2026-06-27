
from MyPackage.datetime_module import DatetimeTimeMenu
from MyPackage.math_module import MathematicalMenu
from MyPackage.random_module import RandomDataGeneration
from MyPackage.uuid_module import UUID_Module
from MyPackage.file_module import FileMenu
from MyPackage.module_explorer import ExploreModuleMenu


def MainMenu():
    while True:
        print("\nWelcome to Main Menu !")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            DatetimeTimeMenu()

        elif choice == 2:
            MathematicalMenu()

        elif choice == 3:
            RandomDataGeneration()

        elif choice == 4:
            UUID_Module()

        elif choice == 5:
            FileMenu()

        elif choice == 6:
            ExploreModuleMenu()

        elif choice == 7:
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    MainMenu()