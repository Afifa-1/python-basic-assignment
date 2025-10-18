# Password checker
password = input("enter the password: ")
strength = 0
if len(password) < 7:
    print("Password is too short")
elif len(password) >= 7:
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1 
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "~!@#$%^&*()_+:<>,'`" for char in password):
        strength += 1

if strength == 1:
    print("Password is too weak")

elif strength == 2:
    print("Password is moderate")
    
elif strength ==3:
    print("Password is strong")
    
elif strength == 4:
    print("your password is perfectly strongg")
