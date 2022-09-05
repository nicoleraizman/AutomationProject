class Person:
    def __init__(self, id1, name = "no name", age=0, address="no address"):
        self.id = id1
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, age: {self.age}, address: {self.address}"

# str is a standard function: not always there is a list of objects
# we can use both of the functions - str and repr - if we want to print
    # the objects differently

    def __repr__(self):
        print("inside repr")
        return f"id: {self.id}, name: {self.name}, age: {self.age}"



    # eq = p.1__eq__(p4) --------------> p1==p4, returns only booleans
    def __eq__(self, other):
        if other == None:
            return False

        if self.id == other.id:
            return True
        else:
            return False

# grater func: >
    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False

# Operators overloading:
# == __eq__
# != __ne__
# > __gt__
# < __lt__
# >= _ge__
# <= __le__

if __name__ == '__main__':
p1 = Person(12,"Dani",25,"Bugrashov, 24, Tel Aviv")
p2 = Person(13,"Gila",2,"aaaaaaaaaaaaaaaaaaaaaaa")
p3 = Person(14,"David",36,"bbbbbbbbbbbbbbbbbbbbbbb")
p4 = Person(12,"Dani",25,"Bugrashov, 24, Tel Aviv")

print(p1)
list1 = [p3, p2, p1]

print(list1)

list1[0].address = "cccccccccccccccccccccccccc"
# the address in the memory will be the same one
# in order to change the address of the object we have to enter into the cell of the list and make some changes, such as:
# list1[0] = *something else*

print("p1",p1)

# will print True
print(p1 in list1)

# will print False, because it will have another address in the memory
print(p4 in list1)

p1=p4
# will print False, False, because it works with addresses in the memory
print("p1",p1)
print("p4",p4)

print("p1 in list1", p1 in list1)
print("p4 in list1", p4 in list1)

# to check whether the person (and not the address of the memory) exists in the list
# we may improve the "in" func ---- see equal (__eq__) above
p4 = Person(12,"Daniel",25,"Bugrashov, 29, Tel Aviv")
print("p1==p4",p1==p4)
# print(p1.__eq__(p4))

print("p1 is p4",p1 is p4)
# will print False, because even the "is" func checks the addresses in the memory

# __eq__ will make the index of p4 equal to the index of p1
print(list1.index(p4))

print(p1>p2)
print(p1.__gt__(p2))

# will use the __gt__ func!!!
print(max(list1))