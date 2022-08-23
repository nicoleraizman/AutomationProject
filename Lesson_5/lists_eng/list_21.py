from random import randint

digits_str = ""

for i in range(4):
    digit = randint(0,9)
    while str(digit) in digits_str:
        digit = randint(0, 9)
    digits_str+=str(digit)

print(digits_str)


guess = input("Enter 4 digits: ")
while guess != digits_str:
    bool_count = 0
    hit_count = 0
    for i in range(len(guess)):
        if guess[i] == digits_str[i]:
            bool_count+=1
            if guess[i]!=digits_str[i] and guess[i] in digits_str:
                hit_count+=1
    print("bool", bool_count)
    print("hits", hit_count)
    guess = input("Enter 4 digits: ")

print("Correct guess!")




