sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

list_index = []
start_index = 0
# you have to find the index of only the first letter in the word
#I am learning Python and I am not learning Java and I am happy


# print(sentence.index(word))
# print(sentence.index(word,3))
# print(sentence.index(word,28))
# print(sentence.index(word,55))

for i in range(sentence.count(word)):
    found_index = sentence.index(word,start_index)
    list_index.append(found_index)
    start_index = found_index+1

print(list_index)

