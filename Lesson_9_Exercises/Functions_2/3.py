def finding(list1:list,number:int,index = 0):
    """"function which finds an index without using the index function"""
    for i in range(index,len(list1)+1):
        if list1[i] == number:
            return i



list1=[20,30,40,50,60,70,80,90]
number=90
index = 0
print(finding(list1,number,index))



