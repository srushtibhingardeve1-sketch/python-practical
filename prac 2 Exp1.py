# Accept marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3

# Display formatted scorecard
print("\n" + "=" * 40)
print(f"{'STUDENT SCORECARD':^40}")
print("=" * 40)
print(f" Subject 1      : {subject1:<20.2f}")
print(f" Subject 2      : {subject2:<20.2f}")
print(f" Subject 3      : {subject3:<20.2f}")
print("-" * 40)
print(f" Total Marks    : {total_marks:<20.2f}")
print(f" Average Marks  : {average_marks:<20.2f}")
print("=" * 40)