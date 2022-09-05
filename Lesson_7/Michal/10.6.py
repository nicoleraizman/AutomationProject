def print_upper_lower(string):
    count_upper=0
    count_lower=0
    for i in string:
        if i.isalpha():
            if i == i.upper():
                count_upper+=1
            else:
                count_lower+=1
    print("lower: ",count_lower, "upper",count_upper)

print_upper_lower("Today is Sunday")
print_upper_lower("Today 555is ___Sunday")

# solution 2)
def print_upper_lower(string: str):
    count_upper=0
    count_lower=0
    for i in string:
        if i.isupper():
            count_upper+=1
        if i.islower():
            count_lower+=1
    print("lower: ",count_lower, "upper",count_upper)

print_upper_lower("Today is Sunday")
print_upper_lower("Today 555is ___Sunday")
