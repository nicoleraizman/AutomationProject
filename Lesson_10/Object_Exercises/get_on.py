# from random import randint
#
# list_of_numbers = []
# for i in range(6):
#     i = randint(1,46)
#     list_of_numbers.append(i)
#
# print(list_of_numbers)


list1=[1,2,3,4,5]
number = int(input("Guess a number: "))
if number in list1:
    print(number)