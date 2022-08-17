grade=int(input("Enter grade: "))
count_grades=0

while 0<grade<100:
    count_grades+=1
    if count_grades==5:
        print("You have entered enough grades")
        break

    grade = int(input("Enter grade: "))
else:
    print("Invalid grade, must be between 0 and 100")