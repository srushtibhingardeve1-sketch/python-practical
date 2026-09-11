# Create a starting list of grades
grades = [85, 92, 78, 90, 64]
print("Original grades:", grades)

# Prompt the user for the index position and the new grade
index_input = input("\nEnter the index position to update (0 to 4): ")
position = int(index_input)

grade_input = input("Enter the new grade: ")
new_grade = int(grade_input)

# Update the value at that specific index
grades[position] = new_grade

# Sort the list so it is ordered
grades.sort()

# Display the final sorted list
print("\nUpdated and Ordered Grades:")
print(grades)