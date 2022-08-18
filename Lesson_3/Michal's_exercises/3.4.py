from random import randint

low_end= 0
high_end = 100

success = False
while not success :
    number = randint(low_end,high_end)
    print(number)
    input("Is this your number? ")
    if is_number:
        success = True
        continue
    high_or_low = input("Higher or lower?")
    if high_or_low == "higher":
        low_end = number +1
    else:
        high_end = number -1










