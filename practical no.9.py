students = []
marks = []


def add_student():
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))

    students.append(name)
    marks.append(mark)

    print("Student added successfully!\n")


def display_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Marks ---")
    for i in range(len(students)):
        print(f"{i + 1}. {students[i]} - {marks[i]} marks")
    print()


def update_marks():
    name = input("Enter student name to update marks: ")

    if name in students:
        index = students.index(name)
        new_mark = float(input("Enter new marks: "))

        marks[index] = new_mark
        print("Marks updated successfully!\n")
    else:
        print("Student not found.\n")


def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        index = students.index(name)
        print(f"{students[index]} has {marks[index]} marks.\n")
    else:
        print("Student not found.\n")


def delete_student():
    name = input("Enter student name to delete: ")

    if name in students:
        index = students.index(name)

        students.pop(index)
        marks.pop(index)

        print("Student record deleted successfully!\n")
    else:
        print("Student not found.\n")



while True:
    print("===== Student Marks Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Marks")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_marks()

    elif choice == "4":
        search_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.\n")