import random
import string

def generate_password(length=12, use_digits=True, use_punctuation=True):
    """
    Generate a random password.

    Parameters:
    - length (int): Length of the password (default is 12).
    - use_digits (bool): Include digits in the password (default is True).
    - use_punctuation (bool): Include punctuation in the password (default is True).

    Returns:
    - password (str): Generated password.
    """
    
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    # Generate the password randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
generated_password = generate_password(length=16, use_digits=True, use_punctuation=True)
print("Generated Password:", generated_password)
