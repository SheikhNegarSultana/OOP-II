def count_substring_occurrences(main_string, substring):
    count = main_string.count(substring)
    return count

# Example usage
main_string = "GeeksforGeeks is best for Geeks"
substring = "Geeks"
occurrences = count_substring_occurrences(main_string, substring)
print(f"The substring '{substring}' occurs {occurrences} times in the main string.")
