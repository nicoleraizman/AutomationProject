
def list_filling(list1):

    for i in range(20):
        from random import randint
        i = randint(1,100)
        list1.append(i)
    return list1

def number_in_list(list1,number):
    return list1.count(number)




list1=[]
print(list_filling(list1))
number=int(input("Enter a number: "))
print(number_in_list(list1,number))