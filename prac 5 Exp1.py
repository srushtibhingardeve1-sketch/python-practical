# Accept the number of rows from the user
rows = int(input("Enter the number of rows: "))

print("\n--- Right-Angled Triangle Pattern ---")

# Outer loop controls the row number (1 to rows)
for i in range(1, rows + 1):
    # Inner loop controls the column printing for the current row
    for j in range(1, i + 1):
        print(i, end=" ")
    # Print a newline after finishing each row
    print()