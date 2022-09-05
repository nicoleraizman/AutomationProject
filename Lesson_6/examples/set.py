# in set there are no similar values
# there is no importance to the indexes order
set1={10,20,30, 40, "abc",10}
print(set1)

# sum of 2 sets: set1|set2 (not with +!!!!!!!!!!)
# create an empty set
set1=set()

set1={10,20,30, 40, "abc",10}
# add function
set1.add(50)
print(set1)

set1.add(20)
print(set1)

# remove an existing item from the set
set1.remove('abc')
print(set1)
# if you remove an item which doesn't exist there will be an error
# if you want to remove an item which doesn't exist - discard
set1.discard(100)
print(set1)

# update function
set2={11,12,13}
set1.update(set2)
print('set1.update',set1)

set2=set1
print(set2)
set2.add(200)
print(set1)
print(set2)

# pop a random item
print(set1.pop())
print(set1)

list1=[10,11,12,13,10,11,15,16]
print(set(list1))
print(list(set(list1)))

if 12 in set1:
    print("12 exists")
else:
    print("12 does not exists")

for i in set1:
    print(i)

# you can put into set a tuple, but not dictionary and list