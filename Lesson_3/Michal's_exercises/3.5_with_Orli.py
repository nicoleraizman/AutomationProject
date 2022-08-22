amount = int(input("enter how many numbers in fibonacci series (at least 2): "))

num1=0
num2=1

print(num1,num2,end= ' ')
# 0 1 1 2

for i in range(amount-2):
    num3 = num1+num2
    print(num3,end=' ')
    num1 = num2
    num2 = num3

