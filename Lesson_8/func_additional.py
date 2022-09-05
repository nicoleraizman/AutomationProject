def print_details(name,age,*children,**additional_details):
    """get a person's name, age and other details (optional)
    and the method will print the details"""
    returned_str = f"name: {name}, age: {age}\n"
    returned_str+=f"Children:,{children}\n"

    for key in additional_details:
        returned_str+=(f"{key}: {additional_details[key]}")

    return returned_str
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# children = input("Enter names of your children, if you have ones: ")
# additional_details = input("Enter additional details: ")

print_details("Moshe", 41)
print(print_details("Moshe", 41, "Dani", "Gali", "Miki", Phone="0525381648", Email="moshe@abc.com"))
