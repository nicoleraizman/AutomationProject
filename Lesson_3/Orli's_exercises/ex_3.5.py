grade=int(input("Enter grade: "))
sum1=0
count1=0


while 0<=grade<=100:
    if grade>=60:
        sum1+=grade
        count1+=1
    grade=int(input("Enter grade: "))
print(f"Average of the Passed grades is: {sum1/count1}")
