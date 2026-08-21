def format_feedback(customer_name, feedback):
    # Remove extra spaces and format the customer's name
    customer_name = customer_name.strip().title()

    # Remove extra spaces from feedback
    feedback = feedback.strip()

    # Capitalize the first letter of feedback
    if feedback:
        feedback = feedback[0].upper() + feedback[1:]

    # Replace informal words with professional words
    feedback = feedback.replace("can't", "cannot")
    feedback = feedback.replace("won't", "will not")

    # Create the professional message
    formatted_message = (
        f"Customer Name: {customer_name}\n"
        f"Feedback: {feedback}\n"
        f"Thank you, {customer_name}, for sharing your valuable feedback."
    )

    return formatted_message


# Get input from the user
name = input("Enter customer name: ")
feedback = input("Enter customer feedback: ")

# Format the feedback
result = format_feedback(name, feedback)

# Display the formatted feedback
print("\n--- Formatted Customer Feedback ---")
print(result)