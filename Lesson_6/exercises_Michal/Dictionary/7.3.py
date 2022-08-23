dic1 = {1:10,2:20,3:30}
dic2 = {}
for i in dic1:
    print(i, dic1[i])
    dic2.update({dic1[i]:i})
print(dic2)

# solution b)

d1={1:10,2:20,3:30,4:40,5:40}
for i in dic1:
    dic2[dic1[i]]=i
print(dic2)


