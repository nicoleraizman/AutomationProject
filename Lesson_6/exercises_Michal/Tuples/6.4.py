from random import randint
randint(0,100)
list1 = []

for i in range(10):
    numbers = randint(0,100)
    list1.append(numbers)
print(tuple(list1))


num = (int(input("Enter a number: ")),)

tup1 = tuple(list1)
tup1+=(num)
print(tup1)

tup2 = tup1[:4]+tup1[7:]
print(tup2)

tup2=list(tup2)
del tup2[0]
print(tup2)

