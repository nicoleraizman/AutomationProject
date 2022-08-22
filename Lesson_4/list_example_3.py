from random import randint

numbers=[]
for i in range(20):
    numbers.append(randint(1,50))
print(numbers)


numbers_to_remove=[]
for i in numbers:
    if i%10==0:
        numbers_to_remove.append(i)

for i in numbers_to_remove:
    numbers.remove(i)

print(numbers)

