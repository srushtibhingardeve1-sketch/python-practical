# Accept dimensions for the frame
width = int(input("Enter frame width: "))
height = int(input("Enter frame height: "))

print("\n--- INVOICE FRAME BORDER ---\n")

# Iterate through each row and column position
for i in range(height):
    for j in range(width):
        # Print asterisk on the outer boundaries, space inside
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end="")
        else:
            print(" ", end="")
    # Move to the next line after completing a row
    print()