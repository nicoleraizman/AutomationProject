def counting(number:int):
    """func which counts how many times a number appears in a list without using the count function"""
    count=0
    for i in list1:
        if i==number:
            count+=1
    return count


list1=[1,2,3,4,5,6,7,8,9,2,3,2,3,2,3,2]
number=2
print(counting(number))



