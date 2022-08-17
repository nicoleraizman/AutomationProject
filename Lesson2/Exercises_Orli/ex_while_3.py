num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))


while num1%2==0 and num2%2==0:
    print(num1+num2)
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
print(num1*num2)