def list_filling(list1):
    for i in range(2,41):
        if i%2==0:
            list1.append(i)
    return list1

list1=[]
print(list_filling(list1))