import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. Minimum 8 characters required.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r'[@#$%^&+=]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (@#$%^&+=).")

    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

while True:
    password = input("Enter password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    for message in feedback:
        print(message)
    
    if strength == "Strong":
        break
    else:
        print("\nPlease try again with a stronger password.")
