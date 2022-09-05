def removing(list1:list,number):
    list2=[]
    if number in list1:
        for i in list1:
            if i != number:
                list2.append(i)
        list1.clear()
        list1.append(list2)
    else:
        print("Error")

list1=[9,1,9,2,9,3,4,9,5,6,9,7,8,9]
number = 9
removing(list1,number)
print(*list1)



