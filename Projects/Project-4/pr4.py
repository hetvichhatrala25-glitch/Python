dataset = []

print(__doc__)

print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:

        def input_data():
            
            global dataset

            print("\n" + input_data.__doc__)

            data = input("Enter data for a 1D array (separated by spaces): ")
            dataset = [int(i) for i in data.split()]

            print("Data has been stored successfully!")

        input_data()

    elif choice == 2:

        def display_summary():

            print("\n" + display_summary.__doc__)

            print("Total elements:", len(dataset))
            print("Minimum value:", min(dataset))
            print("Maximum value:", max(dataset))
            print("Sum of all values:", sum(dataset))
            print("Average value:", round(sum(dataset) / len(dataset), 2))

        display_summary()

    elif choice == 3:

        def factorial(n):

            if n == 0 or n == 1:
                return 1

            return n * factorial(n - 1)

        def calculate_factorial():

            print("\n" + calculate_factorial.__doc__)

            num = int(input("Enter a number to calculate its factorial: "))
            print("Factorial of", num, "is:", factorial(num))

        calculate_factorial()

    elif choice == 4:

        def filter_data():

            print("\n" + filter_data.__doc__)

            threshold = int(input("Enter a threshold value: "))

            option = int(input(
                "1. Values >= Threshold\n"
                "2. Values < Threshold\n"
                "Enter your choice: "
            ))

            if option == 1:
                print("Filtered Data (values >= threshold):")
                for value in dataset:
                    if value >= threshold:
                        print(value, end=" ")

            elif option == 2:
                print("Filtered Data (values < threshold):")
                for value in dataset:
                    if value < threshold:
                        print(value, end=" ")

            else:
                print("Invalid choice!")

            print()

        filter_data()

    elif choice == 5:

        def sort_data():

            print("\n" + sort_data.__doc__)

            print("1. Ascending")
            print("2. Descending")

            sort_choice = int(input("Enter your choice: "))

            temp = dataset.copy()

            if sort_choice == 1:
                temp.sort()
                print("Sorted Data in Ascending Order:")

            elif sort_choice == 2:
                temp.sort(reverse=True)
                print("Sorted Data in Descending Order:")

            else:
                print("Invalid choice")
                return

            for value in temp:
                print(value, end=" ")

            print()

        sort_data()

    elif choice == 6:

        def dataset_statistics():

            minimum = min(dataset)
            maximum = max(dataset)
            total = sum(dataset)
            average = total / len(dataset)

            return minimum, maximum, total, average

        def display_statistics():

            print("\n" + display_statistics.__doc__)

            minimum, maximum, total, average = dataset_statistics()

            print("Minimum value:", minimum)
            print("Maximum value:", maximum)
            print("Sum of all values:", total)
            print("Average value:", round(average, 2))

        display_statistics()

    elif choice == 7:

        def exit_program():

            print("\n" + exit_program.__doc__)
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")

        exit_program()
        break

    else:
        print("Invalid choice!")