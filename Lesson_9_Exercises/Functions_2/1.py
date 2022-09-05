def length(list1:list):
    """function which counts length of a list without using len"""
    count=0
    for i in list1:
        count+=1
    return count

list1=[1,2,3,4,5]
print(length(list1))

