def bigger(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def smaller(num1,num2):
    if num1<num2:
        return num1
    else:
        return num2

def printing(num1,num2):
    list1=[]
    for i in range(num1,num2+1):
        list1.append(i)
    print((list1))

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

printing(smaller(num1,num2),bigger(num1,num2))
