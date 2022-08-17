num1=input("Enter the number of computers: ")

if num1=="":
    num1=15
else:
    num1=int(num1)

print(f"Tomorrow you will have to take care of {num1*2} computers")