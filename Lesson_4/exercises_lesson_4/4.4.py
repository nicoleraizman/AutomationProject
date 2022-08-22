list1=[]

list2=[]


# for i in range(5):
#     num1=int(input("Enter a number: "))
#     list1.append(num1)
#
# for i in range(5):
#     num2=input("Enter a number: ")
#     list2.append(num2)
#
# list3=list1+list2
# print(list3)


num1=input("Enter a number: ")
while num1 != "":
    list1.append(num1)
    num1=input("Enter a number: ")

num2=input("Enter a number: ")
while num2 !="":
    list2.append(num2)
    num2 = input("Enter a number: ")

list3 = list1 + list2
print(list3)

