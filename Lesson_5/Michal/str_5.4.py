sentence = input("Enter your sentence: ")

a = len(sentence)
print("a",a)

print("==================================================================")

b = sentence[2:6]
print("b",b)

print("==================================================================")

c = sentence.split()
print(f"c, {c[0]} {c[0]} {c[0]}")

print("==================================================================")


for i in range(len(c)):
    c[i] = c[i].capitalize()
print("d",*c)

print("==================================================================")

print(sentence.title())
