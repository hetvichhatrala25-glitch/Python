import math


def MathematicalMenu():
    while True:
        print("\nMathematical Operations:")
        print("Enter 1 to calculate Factorial")
        print("Enter 2 to solve Compound Interest")
        print("Enter 3 to do Trigonometric calculations")
        print("Enter 4 to calculate an area of Geometric Shapes")
        print("Enter 5 to go back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            num = int(input("Enter a number: "))
            print("Factorial:", math.factorial(num))

        elif choice == 2:
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))

            amount = p * ((1 + r / 100) ** t)

            print("Compound Interest:", round(amount, 2))

        elif choice == 3:
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)

            print("sin =", round(math.sin(rad),4))
            print("cos =", round(math.cos(rad),4))
            print("tan =", round(math.tan(rad),4))

        elif choice == 4:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            
            area = 0.5 * base * height

            print("Area of Triangle:", round(area, 2))

        elif choice == 5:
            break

        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    MathematicalMenu()