grades = list(map(float, input("Enter student grades separated by spaces: ").split()))

print("Original Grades:", grades)


index = int(input("Enter index position to update: "))


new_grade = float(input("Enter new grade: "))


if 0 <= index < len(grades):
    grades[index] = new_grade
    print("Corrected Grades:", grades)
else:
    print("Invalid index position!")