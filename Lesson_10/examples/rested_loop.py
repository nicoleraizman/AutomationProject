# a method that creates a list that will contain all the numbers between 1-100
# the numbers will be organized in lists of 10 numbers each:
# [1,2,3...10],[11,12,13...20]...[91,92...10]
# the method will return the list

def create_list_100():
    list1=[]
    low = 1
    high = 11
    for i in range(10):
        list2=[]
        for j in range(low,high):
            list2.append(j)
        list1.append(list2)
        low+=10
        high+=10
    return list1

print(create_list_100())

