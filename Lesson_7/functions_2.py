# a method that gets 2 nums and returns their average


def average(num1,num2):
    avg = (num1+num2)/2
    return avg
# a method that gets a number and returns if an answer is a valid grade
def valid_grade(grade):
    if 0<=grade<=100:
        return True
    else:
        return False

# method/function
# get 2 grades from the user and check if they are average, passed or not (>=70)
# the program will use a method that will get 2 numbers and return their average
# the word "return" stops the function (like "break" in loop)

grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))

if valid_grade(grade1) and valid_grade(grade2):
    avg=average(grade1,grade2)
    print(avg)

    if average(grade1,grade2) >=70:
        print("Passed")
    else:
        print("Failed")
else:
    print("Invalid grade")
