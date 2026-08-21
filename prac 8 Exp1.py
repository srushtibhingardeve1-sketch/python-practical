def sanitize_name(first_name: str, last_name: str) -> str:
    """
    Removes leading/trailing whitespace and formats names into Title Case.
    """
    # .strip() removes surrounding spaces
    # .title() capitalizes the first letter of each word and lowers the rest
    clean_first = first_name.strip().title()
    clean_last = last_name.strip().title()
    
    # Combines them into a single clean string
    return f"{clean_first} {clean_last}"

# --- Example Usage ---
if __name__ == "__main__":
    # Simulating messy user inputs
    input_first = "   jOHN  "
    input_last = "  dOE   "
    
    full_name = sanitize_name(input_first, input_last)
    
    print(f"Original: '{input_first}' '{input_last}'")
    print(f"Sanitized Full Name: '{full_name}'")
    # Output: 'John Doe'
