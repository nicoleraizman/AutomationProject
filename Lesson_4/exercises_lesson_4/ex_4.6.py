list1=[]

for i in range(1,11):
    list1.append(i)
# a)
print(list1[-3:])
print("========================================================")
# b)
print(list1)
print(list1[::-1])
print("========================================================")
# c)
print(list1[1::2])
print("========================================================")
# d)
print(list1[::2])
print("========================================================")
# e)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

list1 = list1[:4] + [num1, num2] + list1[:6] + [num3]
print(list1)
print("========================================================")

# f)

list1=[]

for i in range(1,11):
    list1.append(i)
print(list1)

for i in range(len(list1)):
    list1[i]*=2

print(list1)

print("========================================================")
list1=[]

for i in range(1,11):
    list1.append(i)
print(list1)

list2 = [list1[0],list1[-1]]
print(list2)

