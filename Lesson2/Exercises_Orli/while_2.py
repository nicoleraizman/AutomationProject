grade=int(input("Enter grade: "))

# while the grades we get from the user are valid, we check if it passed/failed
# when we get an invalid grade, we end the input

while 0<=grade<=100:
    if grade >=70:
        print("Passed")
    else:
        print ("Failed")

        grade=int(input("Enter grade: "))
print("Invalid grade! Input ended")

