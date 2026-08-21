import re

def moderate_text(feedback: str, banned_words: list) -> str:
    """
    Scans feedback and masks specified banned words with asterisks,
    ignoring letter case and matching full words only.
    """
    if not banned_words:
        return feedback

    # Escape words to handle special characters and join with regex OR (|)
    # \b ensures we match whole words only (e.g., 'bad' won't mask 'badge')
    pattern = r'\b(' + '|'.join(map(re.escape, banned_words)) + r')\b'
    
    # Lambda function dynamically matches the length of the caught word
    censored_text = re.sub(
        pattern, 
        lambda match: '*' * len(match.group(0)), 
        feedback, 
        flags=re.IGNORECASE
    )
    
    return censored_text

# --- Example Usage ---
if __name__ == "__main__":
    banned_list = ["terrible", "hate", "scam"]
    user_feedback = "This product is a SCAM! I hate it. The service was terrible, but the shipping was fast."
    
    clean_feedback = moderate_text(user_feedback, banned_list)
    
    print("Original Feedback:")
    print(user_feedback)
    print("\nModerated Feedback:")
    print(clean_feedback)
