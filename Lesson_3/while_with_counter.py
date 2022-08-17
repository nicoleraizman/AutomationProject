# print "Hello!" 10 times

count=0

while count<10:
    print("Hello!")
    count+=1

# while count<=10:
#     print("Hello!")
#     count+=1
# with <= it will print Hello 11 times!!!
print("==========================================================================")
for i in range(10):
    print("Hello!")

print("==========================================================================")
# 3,5,7,9,11,13 - 2(jumps)
for i in range(3,15,2):
    print(i)

print("==========================================================================")
for i in range(10,0,-1):
    print(i)

print("==========================================================================")
# print all number from 100 to 1 that are divided by 3
for i in range(100,0,-1):
    if i%3==0:
        print(i)

print("==========================================================================")
# print all number from 100 to 1 that are divided by 3
for i in range(99,0,-3):
    print(i)

print("==========================================================================")
for i in range (10,101,10):
    print(i)
print("==========================================================================")
for i in range(10,101):
    if i%10==0:
        print(i)