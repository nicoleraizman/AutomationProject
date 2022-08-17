day=int(input("Enter Day: "))
month=int(input("Enter Month: "))
year=int(input("Enter Year: "))

print(f"{day}/{month}/{year//10%10}{year%10}")

