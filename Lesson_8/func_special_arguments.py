def average(a,b,*numbers):
    """The method gets a number and returns the average"""
    print(numbers)
    s=a+b+sum(numbers)
    avg=s/(2+len(numbers))
    return avg

print(average(10,11,1,2,3))
# 1,2,3 - is treaten as a tuple

def valid_grade(grade,*grades):
    """a func that gets a grade and returns if it's valid or not.
    if it gets a few grades, it will return True, if they are all valid.
    If any of the grades is not valid - return False"""

    if grade<0 or grade>100:
        return False
    for i in grades:
        if i<0 or i>100:
            return False

    return True

print(average(5,6))
print(average(10,11,1,2,3))

if valid_grade(80):
    print("Valid grade")
else:
    print("Invalid grade")

if valid_grade(60,70,80,90):
    print("Valid grades")
else:
    print("Not all grades are valid")

if valid_grade(60,70,111,90):
    print("valid grades")
else:
    print("Not all grades are valid")

def f(*args):
    print(args)

f()
f("abc",1,2,3)


def print_details(name, age,**additional_details):
    """get a person's name, age and other details (optional)
    and the method will print the details"""
    print(f"name:{name},age{age}")
    for key in additional_details:
        print(key,additional_details[key])


print_details("Moshe", 41)
print_details("Moshe", 41, phone="0525381648", email="moshe@abc.com")
