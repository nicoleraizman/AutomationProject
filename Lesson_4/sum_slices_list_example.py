list1=[11,12,45,78,100,99,34,55,6]
print(list1)
print("sum(list1)",sum(list1))
print("sum(list1/len(list1)",sum(list1)/len(list1))
# average
print("max(list1)",max(list1))
print("max(list1)",max(list1))

print(list1[-1])
print(list1[-2])

#Slicing
print("list1[1:5]",list1[1:5])
print("list1[:5]",list1[:5])
print("list1[2:]",list1[2:])

print("list1[-3:]",list1[-3:])
print("list1[3:0:-1]",list1[3:0:-1])
print("list1[3::-1]",list1[3::-1])
print("list1[::-1]",list1[::-1])

list1=[11,12,45,78,100,99,34,55,6]
list1[1:4]=[10,20,30,40,50]
print(list1)
list2=list1[-3::]+list1[:3]+[10,20,30,40,50]
print(list2)

print("=================================================")

from random import randint,choice

list2=[11,12,45,78,100,99,34,55,6]
