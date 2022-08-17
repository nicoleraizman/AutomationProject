num=int(input("Enter Number: "))
sum1=(num%10)+(num//10%10)+(num//100)

if 100<=num<=999:
    print(sum1)
else:
    print("Invalid Number")

