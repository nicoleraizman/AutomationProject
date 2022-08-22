from random import randint
#
# numbers=[]
# for i in range(20):
#     numbers.append(randint(1,50))
# print(numbers)

numbers = [randint(1,50) for i in range(20)]
print(numbers)

print("=============================================================")

numbers= [int(input("Enter a number: ")) for i in range(5)]
print(numbers)

print("=============================================================")

numbers = [i for i in range(1,11)]
print(numbers)

print("=============================================================")