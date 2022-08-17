num1=int(input("Enter Number 1: "))
sum1=num1//100+num1//10%10+num1%10

while 100<=num1<=999:
    print(sum1)
    num1 = int(input("Enter Number 1: "))
else:
    print("Invalid number")