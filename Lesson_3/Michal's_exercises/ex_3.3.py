from random import randint
num1=randint(1,9)
num2=int(input("Guess the number: "))

while num1!=num2:
    if num1>num2:
        print("Your number is lower than the system number")
        num2 = int(input("Guess the number: "))
    elif num1 < num2:
        print("Your number is higher than the system number")
        num2 = int(input("Guess the number: "))
else:
    num1=num2
    print("Congrats! This is the correct number!")

