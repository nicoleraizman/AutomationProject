day=int(input("Enter day: "))

if 1<=day<=31:
    month = int(input("Enter month: "))
    if 1<=month<=12:
        year = int(input("Enter year: "))
        if 1950<=year<=2022:
            print(f"{day//10%10}{day%10}/{month//10%10}{month%10}/{year // 10 % 10}{year % 10}")
        else:
            print("Invalid year")
    else:
        print("Invalid month")
else:
    print("Invalid day")

print(1<=day<=31)

