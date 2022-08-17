grade=int(input("Enter the grade: "))

if 0<=grade<=100:
    if 70<=grade:
        print("Pass")
    else:
        print("Failed")
else:
    print("Invalid grade")