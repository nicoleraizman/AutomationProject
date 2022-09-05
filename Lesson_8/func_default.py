def age_group(age=0):
    """Get an argument age and return age group"""
    if age>=0 or age<=120:
        if age<=19:
            return "Child"
        elif age<=60:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"

age = int(input("Enter age: "))
print(age_group(age),end=" ")
print(age_group())
# the last one is default. in this case it will always print "Child"
