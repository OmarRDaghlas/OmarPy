
username = input("Enter your username: ")
password = input("Enter your password: ")
#-----------------------------------------
username = username.lower()

#-----------------------------------------
username = username.replace(" ", "_")

##-----------------------------------------
print("\nUser info")
print("fixed username:", username)
print("password length:", len(password))

# --boolean---
print("\nChecks")
print("Password length >= 8:", len(password) >= 8)
print("is username 'admin':", username == "admin")
print("Is password '1234':", password == "1234")
print("Is default account (admin + 1234):", username == "admin" and password == "1234")

# --------------------------------------------
print(f"\nWelcome, {username}! Your password is {len(password)} characters long")
# Pythonassignment-2
# Pythonassignment-2
