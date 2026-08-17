# Accept marks for three subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total_marks = sub1 + sub2 + sub3
average_marks = total_marks / 3

# Print the final scorecard
print("\n--- Student Scorecard ---")
print(f"Subject 1: {sub1}")
print(f"Subject 2: {sub2}")
print(f"Subject 3: {sub3}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")