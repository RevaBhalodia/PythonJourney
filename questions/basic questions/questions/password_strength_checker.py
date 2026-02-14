import string

def check_password_strength(password):
    
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:", result)
