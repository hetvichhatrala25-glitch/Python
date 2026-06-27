import random


def RandomDataGeneration():
    while True:
        print("\nRandom Data Generation:")
        print("Enter 1 to generate Random Number")
        print("Enter 2 to generate Random List")
        print("Enter 3 to generate Random Password")
        print("Enter 4 to generate Random OTP")
        print("Enter 5 to go back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number: "))
            print("Generated Random Number:", random.randint(num1,num2))

        elif choice == 2:
            li = [23,44,75,82,63]
            print("Original List:", li)
            print("Random List:")

            for i in range(5):
                print(random.choice(li), end=" ")
            print()

        elif choice == 3:
            length = int(input("Enter password length: "))

            characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@$&_"

            print("Generated Password:", end=" ")

            for i in range(length):
                print(random.choice(characters), end="")

            print()

        elif choice == 4:
            print("Generated OTP:", end=" ")

            for i in range(6):
                print(random.randint(0, 9), end="")

            print()

        elif choice == 5:
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    RandomDataGeneration()