students = []
subjects_offered = set()

print(" Welcome to Student Data Organizer ")

while True:

    print("\nSelect an Option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:

        student_id = len(students) + 1

        print("\nEnter Student Details")

        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")

        subject_input = input("Subjects (comma-separated): ")
        subject_list = [s.strip() for s in subject_input.split(",")]

        subjects_offered.update(subject_list)

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subject_list
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == 2:

        if len(students) == 0:
            print("No student records found.")

        else:
            print("\n----- Student Records -----")

            for student in students:
                print(f"\nStudent ID : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Grade      : {student['grade']}")
                print(f"Subjects   : {', '.join(student['subjects'])}")

    elif choice == 3:

        sid = int(input("Enter Student ID to update: "))
        found = False

        for student in students:

            if student["id"] == sid:

                found = True

                print("\n1. Update Name")
                print("2. Update Age")
                print("3. Update Grade")
                print("4. Update Subjects")

                update_choice = int(input("Enter your choice: "))

                if update_choice == 1:
                    student["name"] = input("Enter new name: ")
                    print("Name updated successfully!")

                elif update_choice == 2:
                    student["age"] = int(input("Enter new age: "))
                    print("Age updated successfully!")

                elif update_choice == 3:
                    student["grade"] = input("Enter new grade: ")
                    print("Grade updated successfully!")

                elif update_choice == 4:
                    new_subjects = input(
                        "Enter subjects (comma-separated): "
                    )

                    subject_list = [
                        s.strip()
                        for s in new_subjects.split(",")
                    ]

                    student["subjects"] = subject_list
                    subjects_offered.update(subject_list)

                    print("Subjects updated successfully!")

                else:
                    print("Invalid update option!")

                break

        if not found:
            print("Student ID not found.")

    elif choice == 4:

        sid = int(input("Enter Student ID to delete: "))
        found = False

        for student in students:

            if student["id"] == sid:
                students.remove(student)
                found = True

                print("Student deleted successfully!")
                break

        if not found:
            print("Student ID not found.")

    elif choice == 5:

        if len(subjects_offered) == 0:
            print("No subjects available.")

        else:
            print("\nUnique Subjects Offered:")

            for subject in sorted(subjects_offered):
                print(subject)

    elif choice == 6:

        print("\nThank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")
        