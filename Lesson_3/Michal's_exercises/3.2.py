num=int(input("Enter a number: "))


for i in range(2,num):
    if num%i==0:
        print("Your number is not a primary number")
        break
else:
    print("Your number is a primary number")






