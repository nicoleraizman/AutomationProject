from random import randint
num=randint(0,100)
guess=randint
count=0

while num!=guess:
    if num<guess:
        guess=str(input("too low"))
        count+=1
    elif num>guess:
        guess=str(input("too high"))
        count+= 1
else:
    num==guess
    guess=str(input("correct!"))
    count+=1

print(count)










