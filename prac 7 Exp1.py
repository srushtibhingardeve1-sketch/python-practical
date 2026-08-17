# Accept a text block from the user
text_block = input("Enter the text block to scan:\n")

# Define target special symbols
special_symbols = ['@', '.', '!']

# Initialize counter variables
at_count = 0
dot_count = 0
exclamation_count = 0
total_special_count = 0

# Iterate through each character in the text block
for char in text_block:
    if char == '@':
        at_count += 1
        total_special_count += 1
    elif char == '.':
        dot_count += 1
        total_special_count += 1
    elif char == '!':
        exclamation_count += 1
        total_special_count += 1

# Output Formatted Scanner Report
print("\n" + "=" * 45)
print(f"{'EMAIL SCANNER REPORT':^45}")
print("=" * 45)
print(f" '@' Symbols Found  : {at_count}")
print(f" '.' Symbols Found  : {dot_count}")
print(f" '!' Symbols Found  : {exclamation_count}")
print("-" * 45)
print(f" Total Special Symbols : {total_special_count}")
print("=" * 45)