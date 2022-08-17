age=int(input("Enter age: "))

while 0<=age<=120:
    if 0<=age<=18:
        print("Child")
        age = int(input("Enter age: "))
        if 19<=age<=60:
            print("Adult")
            age = int(input("Enter age: "))
            if 61<=age<=120:
                print("Senior")
                age = int(input("Enter age: "))
age=int(input("Enter age: "))
