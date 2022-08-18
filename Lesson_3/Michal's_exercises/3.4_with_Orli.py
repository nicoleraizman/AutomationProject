from random import randint

input("Think of a number between 0 and 100. Press enter when ready")

count=1
low=0
high=100

num = randint(0,100)
answer = input(f"My guess is: {num}. If too high, press h, too low - l, correct - c: ")

while answer != "c":
    if answer == "l":
        low = num+1
        num = randint(low,high)
    elif answer=="h":
        high=num-1
        num = randint(low,high)
    else:
        print("Invalid answer")
        answer = input(f"My guess is: {num}. If too high, press h, too low - l, correct - c: ")
        continue
    answer = input(f"My guess is: {num}. If too high, press h, too low - l, correct - c: ")
    count += 1

print(f"Game over. Number of trials: {count}")

