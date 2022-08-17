# we get names of the students
# for every student we get a grade and check if it passed or failed
# when we get an empty name, we stop the input


name = input("Enter student name: ")

while name!="":
    grade = int(input(f"Enter grade for {name}: "))

    if grade >=70:
        print("Passed")
    else:
        print("Failed")

    name = input("Enter student name: ")
