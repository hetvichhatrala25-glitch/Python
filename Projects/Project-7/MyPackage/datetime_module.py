import datetime
import time


def DatetimeTimeMenu():
    while True:
        print("\nDatetime and Time Operations:")
        print("Enter 1 to display current date and time")
        print("Enter 2 to calculate difference between two dates/times")
        print("Enter 3 to format date into custom format")
        print("Enter 4 to make stopwatch")
        print("Enter 5 to make countdown timer")
        print("Enter 6 to go back to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Date and Time:",
                  datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        elif choice == 2:
            dt1 = input("Enter first date (DD-MM-YYYY): ")
            dt2 = input("Enter second date (DD-MM-YYYY): ")

            date1 = datetime.datetime.strptime(dt1, "%d-%m-%Y")
            date2 = datetime.datetime.strptime(dt2, "%d-%m-%Y")

            print("Difference:", abs((date2 - date1).days), "days")

        elif choice == 3:
            now = datetime.datetime.now()
            print(now.strftime("%d/%m/%Y %I:%M:%S %p"))

        elif choice == 4:
            input("Press Enter to Start:")
            start = time.time()

            input("Press Enter to Stop:")
            end = time.time()

            print("Time Taken:", round(end - start, 2), "seconds")

        elif choice == 5:
            sec = int(input("Enter countdown time (seconds): "))

            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1

            print("Time Up!")

        elif choice == 6:
            break

        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    DatetimeTimeMenu()