# similar with SQL
# the key has to be a unique number - there cannot be 2 sa,e keys in one dictionary!
# the key can be every type but list
# the value may be every number
d1={1:10,2:20,3:30,4:40,5:50,2:200,6:50}
print(d1)

grades={"Dan":30, "Gal":70, "Sarit":100, "Gali":75, "Hadar": 68}
print(grades)

print('the grade of ["Dan"] is: ',grades["Dan"])

print("==========================================")
# update of key Gal
grades["Gal"]=77
print('grades["Gal"]=77')
print(grades)

print("==========================================")
# add a new key:value
grades["David"] = 99
print(grades)

print("==========================================")

# delete key:value
del grades["Sarit"]
print('del grades["Sarit"]')
print(grades)

# del works in list as well, but instead of key you put index
print("==========================================")
if "Gal" in grades:
    print("Gal exists")
else:
    print("Gal doesn't exists")

print("==========================================")

print("len(grades)",len(grades))


# to get the keys
for i in grades:
    print(i)

# to get the grades
for i in grades:
    print(i, grades[i])


for name in grades:
    grades[name]*=1.1
    if grades[name]>100:
        grades[name]=100
print(grades)

print("==========================================")

print("Print higher than 80:")
for name in grades:
    if grades[name]>80:
        print(name, grades[name])

print("==========================================")

print("grades.values()",grades.values())
print("grades.values()",list(grades.values()))
print("==========================================")
print("grades.keys()",grades.keys())
print("grades.keys()",list(grades.keys()))
print("==========================================")
# .items makes a dictionary list_of_tuples
print("grades.items()",grades.items())
print("==========================================")

# add a couple of new keys_and_values in the existing dictionary
grades.update({"aaa":60, "bbb":70, "ccc":80})
print("grades.update()",grades)



