list1=[]
from random import randint

for i in range(10):
    num=randint(1,100)
    list1.append(num)

print(list1)

# go over the list and for each item multiply by 2

for i in list1:
    i*=2
    print(i)

# print(list1)

for i in range(len(list1)):
    list1[i]*=2
print(list1)


list1[0]=0
print(list1)





