set1 = {10,20,30,40}
set2 = {30,40,50,60}
set3 = set1|set2
print(set3)

set3.remove(60)
print(set3)
print("max:",max(set3), "min:",min(set3), "lengh:",len(set3))
set5 = {60,70,80}
set4 = set3.copy()|set5

print(set4)

set1.clear()
set2.clear()
print(set1,set2)