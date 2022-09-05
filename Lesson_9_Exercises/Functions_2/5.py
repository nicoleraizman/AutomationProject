def listing(list1):
    list1=[]
    for i in another_type:
        if type(another_type) == dict or type(another_type) == set or type(another_type) == str or type(another_type) == tuple:
            list1.append(i)
    return list1

another_type = {5:50}
another_type = (4,4,4)
another_type = "abcdef"
another_type = {7,8,9}
list1=[]
print(listing(list1))
