from random import randint
num=int(input("Enter Number: "))

# operators for if comparison:
# > < >= <= == != (different from...)

# check if num positive or negative
if num>=0:
    print("Positive")
else:
    print("Negative")

# check if num is divided by 3

if num%3==0:
    print("Divided by 3 ")
else:
    print("Not divided by 3 ")

num2 = randint(1,50)
print("num2", num)

# check if the sum of num and num2 is divided by 3
if (num+num2)%3==0:
    print(f"{num+num2} is divided by 3")
else:
    print(f"{num+num2} is not divided by 3")


