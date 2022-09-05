def grades(grade):
    if 70<=grade<=100:
        return True
    else:
        return False


for grade in range(5):
    grade = int(input("Enter grade: "))
    if grades(grade):
        print("Passed")
    else:
        print("Failed")

# grade1 = int(input("Enter grade 1: "))
# grade2 = int(input("Enter grade 2: "))
# grade3 = int(input("Enter grade 3: "))
# grade4 = int(input("Enter grade 4: "))
# grade5 = int(input("Enter grade 5: "))
