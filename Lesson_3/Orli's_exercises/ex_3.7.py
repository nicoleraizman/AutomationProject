
sum1=0
count=0

for i in range(5):
    num = int(input(f"Enter a number: {i+1}: "))
    num=num%10
    sum1+=num
    count+=1


print("The sum of the last digits is: ", sum1)
