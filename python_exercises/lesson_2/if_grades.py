# get a name of a student and the grade
# print if a student passed or failed
# only Dan and Dana can pass
# a Passed grade is at least 70

name = input("Enter Student Name: ")
grade = int(input("Enter Grade: "))
# if grade>=70

# If the grade is empty, put zero in the grade
if grade=="":
    grade=0
else:
    grade=int(grade)

if 0<=grade<=100:
    if grade >= 70 and (name == "Dan" or name == "Dana"):
        print("Passed")
    else:
        print("Failed")
else:
    print("Invalid Grade")







