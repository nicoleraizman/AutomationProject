dic1 = {1:10,2:20,3:30,4:40,5:50,6:50,7:50,8:50,9:50,10:50}
dic2 = {}

for key in dic1:
    if dic1[key] not in dic2.values():
        dic2.update({key:dic1[key]})
print(dic2)






