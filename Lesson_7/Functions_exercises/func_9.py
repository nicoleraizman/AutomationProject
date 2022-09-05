def age_groups(age):
    if 0<=age<=18:
        return "Child"
    elif 19<=age<=60:
        return "Adult"
    elif 61<=age<=120:
        return "Senior"
    elif 0 > age or age > 120:
        print("Invalid age")
        input("Enter a valid age: ")


age1 = int(input("Enter age 1: "))
print(age_groups(age1))
age2 = int(input("Enter age 2: "))
print(age_groups(age2))
age3 = int(input("Enter age 3: "))
print(age_groups(age3))
age4 = int(input("Enter age 4: "))
print(age_groups(age4))
age5 = int(input("Enter age 5: "))
print(age_groups(age5))