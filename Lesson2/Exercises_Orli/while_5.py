num1=int(input("Enter Number 1: "))

while 10<=num1<=99:
    num1 = int(input("Enter Number 1: "))
    if num1%7==0 or num1//10==7:
        print(f"This is a lucky number")
else:
    print("Invalid number")