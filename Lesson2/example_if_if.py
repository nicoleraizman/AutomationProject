num=int(input("Enter Number: "))

# check if num is a valid number
# must be between -100 and 100

if -100<num>100:
    print("Invalid Number")
if -100<=num<=100:
    print("Valid Number")
    if num > 0:
        print("positive")
        num += 1
    elif num < 0:
            print("negative")
            num -= 1
    else:
            print("zero")

    print("num", num)
else:
    print("Invalid Number")

# if num >= -100 and num<=100: may be written as
# -100<=num<=100:



