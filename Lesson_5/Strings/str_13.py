sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")

#I am learning Python and I am not learning Java and I am happy

# solution1

new_sentence = sentence.replace(letter,letter.upper())
print(new_sentence)

print("==================================================")
# solution2
new_sentence = ""
for i in sentence:
    if i==letter:
        new_sentence+=i.upper()
    else:
        new_sentence+=i

print(new_sentence)

