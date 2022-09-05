def average(num1:int,num2:int):
    if type(num1)!=int or type(num2)!=int:
        print("Invalid argument. Must be int")
        return None
    return (num1+num2)/2
# a method that gets a number and returns if an answer is a valid grade
def valid_grade(grade:str):
    if type(grade)==str:
        if grade.isnumeric():
            grade=int(grade)

    if type(grade) != int:
        return False

    if 0<=grade<=100:
        return True
    else:
        return False

# method/function
# a method that gets one valid grade from the user
def get_grade():
    grade = input("Enter a grade: ")
    while not valid_grade(grade):
        grade = input("Invalid grade, try again: ")
    return int(grade)

# a method that prints a message to the user evaluating the grade
def grade_description(grade:int):
    if type(grade)!=int:
        print("Invalid grade")
        return
# just "return" = "return None"
    if grade<0 or grade>100:
        print("Invalid grade")
        return
    if grade>=90:
        print("Very good!")
    elif grade>=80:
        print("Good!")
    elif grade>=70:
        print("OK")
    else:
        print("Failed")

print("__name__",__name__)
if __name__=="__main__":
    print("trying to get a grade")
    num=get_grade()
