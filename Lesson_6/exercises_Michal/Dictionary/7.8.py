names = ["Yuval","Gaya","Sara","Tamir","Ron"]
grades = [95,100,90,87,61]

dict1={}

for i in names:
    dict1.update({i:grades[names.index(i)]})

print(dict1)

average_grade = sum(grades)/len(grades)
print(average_grade)

list1 = []

for i in dict1:
    if dict1[i] > average_grade:
        list1.append(i)
print(list1)

