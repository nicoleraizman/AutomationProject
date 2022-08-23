# get 5 numbers from the user
# for every number get a value and add to the dictionary

d1={}

# for i in range(5):
#     key = int(input("Enter a key: "))
#     value = int(input(f"Enter a value for the key {key}: "))
#     d1.update({key:value})
# print(d1)

print("===================================================")
for i in range(5):
    key = int(input("Enter a key: "))
    d1[key] = int(input(f"Enter a value for the key {key}: "))

print(d1)