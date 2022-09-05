def three_digits_number(num):
    if 99<num<1000:
        return True
    else:
        return False



num = int(input("Enter a number: "))

if three_digits_number(num):
    print("Your number is three digits number")
else:
    print("Your number is not three digits number")