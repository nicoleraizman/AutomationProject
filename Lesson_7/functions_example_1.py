def average(num1,num2):
    avg = (num1+num2)/2
    return avg

# method/function
# get 2 grades from the user and check if they are average, passed or not (>=70)
# the program will use a method that will get 2 numbers and return their average

grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))

avg=average(grade1,grade2)
print(avg)

if average(grade1,grade2) >=70:
    print("Passed")
else:
    print("Failed")


list1=[1,2,3]
if len(list1)>0:
    print("len(list1)>0","yes")