dataset = []

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

        print("\nInput Data")

        data = input("Enter data for a 1D array (separated by spaces): ")

        dataset=[int(i) for i in data.split()]

        print("Data has been stored successfully!")

    elif choice == 2:

        print("\nDisplay Data Summary (Built-in Functions)")

        print("Data Summary:")
        print("Total elements:", len(dataset))
        print("Minimum value:", min(dataset))
        print("Maximum value:", max(dataset))
        print("Sum of all values:", sum(dataset))
        print("Average value:", round(sum(dataset) / len(dataset), 2))

    elif choice == 3:

        print("\nCalculate Factorial (Recursion)")

        num = int(input("Enter a number to calculate its factorial: "))

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)

        print("Factorial of", num, "is:", factorial(num))

    elif choice == 4:

        print("\nFilter Data by Threshold (Lambda Function)")

        threshold = int(input("Enter a threshold value: "))


        choice = int(input("1. Values >= Threshold\n2. Values < Threshold\nEnter your choice: "))

        if choice == 1:
            print("Filtered Data (values >= threshold):")
            for value in dataset:
                if value >= threshold:
                    print(value, end=" ")

        elif choice == 2:
            print("Filtered Data (values < threshold):")
            for value in dataset:
                if value < threshold:
                    print(value, end=" ")

        else:
            print("Invalid choice!")

        print()

    elif choice == 5:

        print("\nSort Data")

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
            continue

        for value in temp:
            print(value, end=" ")

        print()

    elif choice == 6:

        print("\nDisplay Dataset Statistics (Return Multiple Values)")

        def dataset_statistics():
            minimum = min(dataset)
            maximum = max(dataset)
            total = sum(dataset)
            average = total / len(dataset)

            return minimum, maximum, total, average

        minimum, maximum, total, average = dataset_statistics()

        print("Dataset Statistics:")
        print("Minimum value:", minimum)
        print("Maximum value:", maximum)
        print("Sum of all values:", total)
        print("Average value:", round(average, 2))

    elif choice == 7:

        print("\nExit Program")
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice!")