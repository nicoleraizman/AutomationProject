# list1=[]
# list2=[]
# count1=0
# count2=0
#
#
# grade=int(input("Enter a grade: "))
# if grade < 0 or grade > 100:
#     print("Enter a valid grade!")
# else:
#     for grade in range(10):
#         if 60 >= grade <= 100:
#             list1.append(grade)
#             count1 += 1
#             print(f"{len(list1)} students had passed the exam")
#         elif grade < 60:
#             list2.append(grade)
#             count2 += 1
#             print(f"{len(list2)} students had failed the exam")
# grade = int(input("Enter a grade: "))


from random import randint

grades=[]
for i in range(10):
    grades.append(randint(1,100))
print(grades)

count_pass=0
count_fail=0

for grade in grades:
    if grade>=60:
        count_pass+=1
    else:
        count_fail+=1

print("passed",count_pass)
print("failed",count_fail)
