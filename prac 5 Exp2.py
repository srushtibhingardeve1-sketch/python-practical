# Accept dimensions from the user
width = int(input("Enter frame width: "))
height = int(input("Enter frame height: "))

print("\n--- INVOICE FRAME BORDER ---\n")

# Build the top border, middle hollow rows, and bottom border
for row in range(height):
    if row == 0 or row == height - 1:
        # Top and bottom borders: filled entirely with asterisks
        print("*" * width)
    else:
        # Middle rows: asterisk at start and end, spaces in between
        if width > 1:
            print("*" + " " * (width - 2) + "*")
        else:
            print("*")