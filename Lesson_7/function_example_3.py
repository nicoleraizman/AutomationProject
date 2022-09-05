# a method that gets 2 nums and returns their average
#import functions from another file/package
from Functions_exercises.FUNCTIONS import *

print("First grade: ")
grade1 = get_grade()
grade_description(grade1)
print("Second grade: ")
grade2 = get_grade()
grade_description(grade2)
print(type(grade1),type(grade2))

if valid_grade(grade1) and valid_grade(grade2):

    avg=average(grade1,grade2)
    print(avg)

    if average(grade1,grade2) >=70:
        print("Passed")
    else:
        print("Failed")
else:
    print("Invalid grade")
