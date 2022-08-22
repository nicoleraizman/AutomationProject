word = "abcdefg"
#        1234567

print(word[2])

print("=============================================================")

word+="ABC"
print(word)

print("=============================================================")

word*=2
print(word)

print("word.index('f')",word.index('f'))
print("len(word)", len(word))
print(max(word))
print(min(word))

print("===========================================================")

print(word[4:6])

if "abc" in word:
    print("abc exists")
else:
    print("abc doesn't exists")

for i in word:
    print(i,end="\t")

print()
print("===========================================================")

text="I am learning Python"
list1= text.split()
print("list1= text.split()",list1)

str1 = " ".join(list1)
print(str1)
print("===========================================================")

print(word.find("F"))

print("========================================================")

number = input("Enter a number: ")
if number.isnumeric():
    number=int(number)
else:
    print("Invalid number")

print(print)
