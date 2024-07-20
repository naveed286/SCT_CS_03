import re

def assess_password_strength(password):
    # Define the criteria
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_number = re.search(r'[0-9]', password)
    has_special_char = re.search(r'[\W_]', password)

    # Initialize score and feedback
    score = 0
    feedback = []

    # Check the criteria
    if len(password) >= min_length:
        score += 1
    else:
        feedback.append(f"Password should be at least {min_length} characters long.")

    if has_uppercase:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if has_lowercase:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if has_number:
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if has_special_char:
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Assess strength based on score
    strength = ""
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

# Example usage
password = "Example$1234"
result = assess_password_strength(password)
print(f"Password Strength: {result['strength']}")
for fb in result["feedback"]:
    print(f"- {fb}")
