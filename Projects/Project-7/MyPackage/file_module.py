import os

def FileMenu():
    while True:
        print("\nFile Operations:")
        print("Enter 1 to create a new file")
        print("Enter 2 to write to a file")
        print("Enter 3 to read from a file")
        print("Enter 4 to append to a file")
        print("Enter 5 to delete a file")
        print("Enter 6 to go back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            FileName = input("\nEnter file name: ")

            if os.path.exists(FileName):
                print("File already exists!")
            else:
                with open(FileName, "w"):
                    pass
                print("File created successfully!")

        elif choice == 2:
            FileName = input("\nEnter file name: ")

            if os.path.exists(FileName):
                content = input("Enter content to write: ")

                with open(FileName, "w") as file:
                    file.write(content)

                print("Content written successfully!")
            else:
                print("File not found!")

        elif choice == 3:
            FileName = input("\nEnter file name: ")

            if os.path.exists(FileName):
                with open(FileName, "r") as file:
                    print("File Content:")
                    print(file.read())
            else:
                print("File not found!")

        elif choice == 4:
            FileName = input("\nEnter file name: ")

            if os.path.exists(FileName):
                content = input("Enter data to append: ")

                with open(FileName, "a") as file:
                    file.write(content)

                print("Content appended successfully!")
            else:
                print("File not found!")

        elif choice == 5:
            FileName = input("\nEnter file name to delete: ")

            if os.path.exists(FileName):
                os.remove(FileName)
                print("File deleted successfully!")
            else:
                print("File not found!")

        elif choice == 6:
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    FileMenu()