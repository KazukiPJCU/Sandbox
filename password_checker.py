min_length=6
password = input("Password: ")
password_length = len(password)
while password_length < min_length:
    password = input("Password: ")
print(password_length*"*")