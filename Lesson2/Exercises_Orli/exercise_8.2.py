day=int(input("Enter day: "))
month = int(input("Enter month: "))

if month==(1 or 3 or 5 or 7 or 8 or 10 or 12):
    print (1<=day<=31)
    if month==(2 or 4 or 6 or 9 or 11):
    print(1<=day<=30)
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
