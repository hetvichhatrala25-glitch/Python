class JournalManager:
    
    def __init__(self):
        self.filename = "journal.txt"

        try:
            file = open(self.filename, "x")
            file.close()
        except FileExistsError:
            pass
        except PermissionError:
            print("Permission denied while creating journal file.")

    def AddNewEntry(self):
        print("\nAdd a New Entry:")

        date = input("Enter date for this entry (DD-MM-YYYY): ")
        time = input("Enter time for this entry (HH:MM): ")

        EntryLines = input(
            "Enter your journal entries separated by commas:\n"
        )

        li = EntryLines.split(",")

        try:
            file = open(self.filename, "a")

            file.write(f"[{date} {time}]\n")

            for index, sentence in enumerate(li, start=1):

                clean_sentence = sentence.strip()

                if clean_sentence:
                    file.write(f"{index}. {clean_sentence}\n")

            file.write("\n")
            file.close()

            print("\nEntry added successfully!")

        except PermissionError:
            print("\nPermission denied while writing to file.")

        except Exception:
            print("\nAn unexpected error occurred.")

    def ViewAllEntries(self):
        print("\nView All Entries:")

        try:
            file = open(self.filename, "r")

            content = file.read()

            file.close()

            if content.strip() == "":
                print("\nYour journal is empty.")
            else:
                print("\nYour Journal Entries:")
                print("---------------------------------")
                print(content)

        except FileNotFoundError:
            print(
                "\nError: The journal file does not exist."
            )

        except PermissionError:
            print(
                "\nPermission denied while reading the file."
            )

        except Exception:
            print(
                "\nAn unexpected error occurred."
            )

    def SearchEntry(self):
        print("\nSearch for an Entry:")

        keyword = input(
            "Enter a keyword or date to search: "
        )

        try:
            file = open(self.filename, "r")

            found = False

            print("\nMatching Entries:")
            print("---------------------------------")

            for line in file:

                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True

            file.close()

            if not found:
                print("No matching entries found.")

        except FileNotFoundError:
            print(
                "\nError: The journal file does not exist."
            )

        except PermissionError:
            print(
                "\nPermission denied while reading the file."
            )

        except Exception:
            print(
                "\nAn unexpected error occurred."
            )

    def DeleteAllEntries(self):
        print("\nDelete All Entries:")

        try:

            file = open(self.filename, "r")
            file.close()

            confirmation = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )

            if confirmation.lower() == "yes":

                file = open(self.filename, "w")
                file.write("")
                file.close()

                print(
                    "\nAll journal entries have been deleted."
                )

            else:
                print("\nDeletion cancelled.")

        except FileNotFoundError:
            print(
                "\nNo journal entries to delete."
            )

        except PermissionError:
            print(
                "\nPermission denied while deleting entries."
            )

        except Exception:
            print(
                "\nAn unexpected error occurred."
            )

    def ExitProgram(self):
        print("\nExiting program. Goodbye!")
        quit()


journal = JournalManager()

while True:

    print("\nWelcome Menu:")
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:")
    print()
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:

        ch = int(input("\nUser Input:\n"))

        if ch == 1:
            journal.AddNewEntry()

        elif ch == 2:
            journal.ViewAllEntries()

        elif ch == 3:
            journal.SearchEntry()

        elif ch == 4:
            journal.DeleteAllEntries()

        elif ch == 5:
            journal.ExitProgram()

        else:
            print(
                "\nInvalid option. Please select a valid option from the menu."
            )

    except ValueError:
        print(
            "\nInvalid input. Please enter a number between 1 and 5."
        )

    except Exception:
        print(
            "\nAn unexpected error occurred."
        )

