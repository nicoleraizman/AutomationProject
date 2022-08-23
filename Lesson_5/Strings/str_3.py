word = input("Enter a word: ")
letter = input("Enter a letter: ")
# count = 0
#
# for i in word:
#     count+=1
#     if i == letter:
#         print(count)
#         break
# else:
#     print("-1")

for i in range(len(word)):
    if word[i] == letter:
        print("index is", i)
        break
else:
    print(-1)