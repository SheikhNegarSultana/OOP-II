import random
import string

def generate_random_string(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random string
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

# Example usage
length = 12
print("Random String of length", length, ":", generate_random_string(length))
