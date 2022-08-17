sum1=0
count=0

for i in range(6):
    number = int(input(f"Enter number: {i+1}: "))
    sum1+=number
    count+=1
print("Sum:",sum1)
print("Average",sum1/count)
