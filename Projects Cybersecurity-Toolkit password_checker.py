# simple password strength evaluator
password = input("Enter your password")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(not c.isalnum() for c in password ):
    score += 1

if score <=1:
    print("Weak Password")
elif score <= 3:
    print("Medium password")
else:
    print("Strong password")
    

