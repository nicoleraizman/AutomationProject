num1=int(input("Enter Number 1: "))

if 10<=num1<=99:
    if (num1%10==7 or num1//10==7) or num1%7==0:
        print("Lucky Number")
else:
    print("Invalid Number")