def tuples(dict1):
    list1=[]
    for i in dict1:
        t1=(i,dict1[i])
        list1.append(t1)
    return list1



dict1 = {1:10,2:20,3:30,4:40,5:50}
print(tuples(dict1))