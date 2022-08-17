count_invalid=0

grade=int(input("Enter the grade: "))

while grade < 0 or grade > 100:
    count_invalid+=1
    if count_invalid==5:
        print("Too many trials!")
        break
    print("Invalid grade, must be between 0 and 100")
    grade=int(input("Enter grade: "))

else:
    if 70<=grade:
        print("Passed")
    else:
        print("Failed")