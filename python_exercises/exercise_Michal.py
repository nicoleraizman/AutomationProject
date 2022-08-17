# exercise 1.4

name=str(input("Enter Your Name: "))
current_salary=float(input("Enter Your Current Salary: "))
raise_percentage=float(input("Enter Your Raise Percentage: "))
raised_salary=(current_salary*raise_percentage/100)+current_salary

print(f"After the Raising Your Salary will be: {raised_salary}")