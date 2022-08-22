# num=4
#
# if type(num)==int:
#     print("yes")
#

list1=[10,20,30,4.5,"hello"]
#      0  1  2  3     4
print(list1)
print("list1",list1[1])

list1[0]+=list1[2]
list1.append(100)
print(list1)

print("list1+=[1,2,3]")
print(list1)

list1+=[44]
print("list1+=[44]")
print(list1)

list1*=2
print("list1*=2")
print(list1)

list1.index("hello")
print("list1.index('hello')",list1.index('hello'))

list1.count(20)
print("list1.count(20)",list1.count(20))

print(list1)

list1.remove(4.5)
print("list1.remove(4.5)",list1.remove(4.5))

print(list1)







