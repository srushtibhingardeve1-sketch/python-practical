# Accept user input paragraph
paragraph = input("Enter a paragraph:\n")

# Define target word
target_word = "python"

# Approach 1: Word-by-Word Matching (removes surrounding punctuation)
# Clean and split paragraph into words
words = paragraph.lower().split()

# Strip punctuation marks from each word and count matches
target_count = 0
for word in words:
    cleaned_word = word.strip(".,!?;:\"'()[]{}")
    if cleaned_word == target_word:
        target_count += 1

# Approach 2: Substring Counting (alternative built-in method)
# Counts all occurrences including embedded substrings (e.g., in "pythonic")
substring_count = paragraph.lower().count(target_word)

# Output Formatted Word Analysis Report
print("\n" + "=" * 50)
print(f"{'WORD COUNTER UTILITY REPORT':^50}")
print("=" * 50)
print(f" Target Word           : '{target_word}'")
print(f" Exact Word Matches    : {target_count}")
print(f" Total Substring Count : {substring_count}")
print("=" * 50)