min_length = 6
password = input("Password: ")
password_length = len(password)
while password_length < min_length:
    print("Incorrect password length minimum length is", min_length)
    password = input("Password: ")
    password_length = len(password)
print(password_length * "*")
