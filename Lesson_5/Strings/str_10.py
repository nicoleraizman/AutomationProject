from random import choice
user_name = input("Enter a user name: ")
password = ""

for i in range(6):
    password += choice(user_name)

print(password)