from Lesson_11.Person import Person

class Bus_Person:
    def __init__(self,bus_size:int):
        if type(bus_size)!=int:
            raise TypeError("Invalid num of seats. Must be int!")

        if bus_size<=0:
            raise ValueError("Invalid num of seats: must be positive")
            bus_size=10

        self.seats = []
        self.passengers = 0
        for i in range(bus_size):
            self.seats.append(None)


    def __str__(self):
        return f"Number of seats {self.seats}, Number of passengers {self.passengers}"

    def getOn(self,person:Person):
        # get a person and put the person in the bus in the first free seat
        if type(person) != Person:
            raise TypeError("Invalid parameter name: must be of type Person")

        if None not in self.seats:
            print(f"The bus is full. The passenger {name} did not get on the bus")
            return

        # check if the person already exists on the bus
        if person in self.seats:
            print(f"A person with id: {person.id} is already on the bus")

        free_index = self.seats.index(None)
        self.seats[free_index] = person
        self.num_of_passengers+=1

        # for i in range(len(self.seats)):
        #     if self.seats[i] == "Free":
        #         self.seats[i] = name
        #         self.passengers+=1
        #         break
        # else:
        #     print(f"The bus is full. The passenger {name} did not get on the bus")

    def getOff(self,person:Person):
        """Get a person and remove it from the bus list. Put None instead"""
        if person not in self.seats:
            print(f"{person.name} in not on the bus")
            return

        person_index = self.seats.index(name)
        self.seats[person_index] = None
        self.num_of_passengers -= 1

        # if name in range(len(self.seats)):
        #     for seat in self.seats:
        #         if seat == name:
        #             self.seats[seat] = "Free"
        #             self.passengers-=1
        #             break
        # else:
        #     print(f"The passenger {name} is not on the bus")


bus_size = int(input("Enter a number of seats in the bus: "))
bus_details = Bus_Person(bus_size)

number_of_action = int(input("Enter a number of action (0-2): "))

while number_of_action != 0:
    if number_of_action == 1:
        id1 = int(input("Enter id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        p1 = Person(id1,name,age)
        bus_details.getOn(p1)
    elif number_of_action == 2:
        id1 = int(input("Enter id: "))
        p1 = Person(id1)
        bus_details.getOff(p1)
    else:
        print("Enter a valid number")
    number_of_action = int(input("Enter a number of action (0-2): "))

print(bus_details)









