def is_palindrome(s):
    # Reverse the string and compare with the original
    return s == s[::-1]

# Example usage
string = "radar"
if is_palindrome(string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
