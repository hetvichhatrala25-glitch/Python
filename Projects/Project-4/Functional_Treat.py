dataset = []

def input_data():
    global dataset

    print("\nInput Data")
    data = input("Enter data for a 1D array (separated by spaces): ")

    dataset = [int(i) for i in data.split()]

    print("Data has been stored successfully!")


def display_summary():

    if not dataset:
        print("Dataset is empty!")
        return

    print("\nData Summary")
    print("Total elements:", len(dataset))
    print("Minimum value:", min(dataset))
    print("Maximum value:", max(dataset))
    print("Sum of all values:", sum(dataset))
    print("Average value:", round(sum(dataset) / len(dataset), 2))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():

    print("\nFactorial Calculation")

    num = int(input("Enter a number to calculate its factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return

    print("Factorial of", num, "is:", factorial(num))


def filter_data():

    if not dataset:
        print("Dataset is empty!")
        return

    print("\nFilter Data")

    threshold = int(input("Enter a threshold value: "))

    option = int(input(
        "1. Values >= Threshold\n"
        "2. Values < Threshold\n"
        "Enter your choice: "
    ))

    if option == 1:
        result = [x for x in dataset if x >= threshold]
        print("Filtered Data:", result)

    elif option == 2:
        result = [x for x in dataset if x < threshold]
        print("Filtered Data:", result)

    else:
        print("Invalid choice!")


def sort_data():

    if not dataset:
        print("Dataset is empty!")
        return

    print("\nSort Data")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    temp = dataset.copy()

    if choice == 1:
        temp.sort()
        print("Ascending Order:", temp)

    elif choice == 2:
        temp.sort(reverse=True)
        print("Descending Order:", temp)

    else:
        print("Invalid choice")


def dataset_statistics():

    minimum = min(dataset)
    maximum = max(dataset)
    total = sum(dataset)
    average = total / len(dataset)

    return minimum, maximum, total, average


def display_statistics():

    if not dataset:
        print("Dataset is empty!")
        return

    print("\nDataset Statistics")

    minimum, maximum, total, average = dataset_statistics()

    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Sum of all values:", total)
    print("Average value:", round(average, 2))


def exit_program():
    print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")


print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    choice = int(input("\nPlease enter your choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        display_summary()

    elif choice == 3:
        calculate_factorial()

    elif choice == 4:
        filter_data()

    elif choice == 5:
        sort_data()

    elif choice == 6:
        display_statistics()

    elif choice == 7:
        exit_program()
        break

    else:
        print("Invalid choice!")