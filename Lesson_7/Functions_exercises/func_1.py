def sum(num):
    sum1 = (num1%10)+(num1//100)+(num1//10%10)
    return sum1

num1 = int(input("Enter a number: "))

sum1 = sum(num1)
print(sum1)
