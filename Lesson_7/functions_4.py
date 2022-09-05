def f1(a,b):
   b+=1
   print(b)
   pass
# pass is a command that doesn't do anything
# it just takes the place of the command

def f2(c:list):
    print("inside f2",id(c))
    c.append(5)
    print("inside f2 after changing",id(c))
    print(c)

aa = 5
f1(aa,50)
print(aa)
print("==================================================")

list1=[1,2,3]
print("before f2", id(list1))
f2(list1)
print("after f2", id(list1))
print(list1)


