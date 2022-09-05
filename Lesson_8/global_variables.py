# # 1) def f1():
#     a = 7
#     print(a)
#
# a=5
# f1()
# print(a)

# 2)
# def f1():
#     a+=1
#     print(a)
#
# a=5
# f1()
# print(a)

def f1():
    global a
    a+=1
    print(a)

a=5
f1()
print(a)


