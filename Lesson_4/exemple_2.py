# list1=[10,20,30,40,"hello",1,2,3,10,20,10]
#
# # if 20 in list1:
# #     print("exists")
# # else:
# #     print("doesn't exists")
# #
# # if 20 not in list1:
# #     print("20 doesn't exists")
# # else:
# #     print("20 exists")
#
# # remove from the list1 all the numbers equal 10
#
# while 10 in list1:
#     list1.remove(10)
#
# print(list1)
#
# # print all the numbers in the list with spaces between them
#
# for i in list1:
#     print(i,end="\t")

#print(*list1)

# go over the list and print only the even numbers

list1 = [11,12,45,78,99,100,42,67]
print(list1)
for i in list1:
    if i%2==0:
        print(i,end=' ')


print("======================================================")

list1=[]
for i in range(5):
    num=int(input("Enter number: "))
    list1.append(num)
    print(list1)
