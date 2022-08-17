grade=int(input("Enter the grade: "))
# while the grade is invalid print an error message and get a new grade
# when we get a valid grade we can check if it passed or failed
while grade < 0 or grade > 100:
    print("Invalid grade, must be between 0 and 100")
    grade=int(input("Enter grade: "))
# if you forgot grade=int... you created an infinite
if 70<=grade:
    print("Passed")
else:
    print("Failed")
