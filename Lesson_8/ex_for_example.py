from random import randint

def rand_numbers(numbers:list,size=10,low=1,high=100):
    """Gets an empty list and inserts random numbers to the list
    the default size of the list: 10, default range - 1-100"""
    for i in range(size):
        numbers.append(randint(low,high))



list1=[]
rand_numbers(list1)
print(list1)

#default_size = 5
list1=[]
rand_numbers(list1,5)
print(list1)

list1=[]
rand_numbers(list1,low=30,high=70)
print(list1)