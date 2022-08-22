amount = int(input("enter how many numbers in fibonacci series (at least 2): "))

fibonacci_list=[0,1]

# [0 1] - values
#  0 1 - indexes

for i in range(2,amount):

    num=fibonacci_list[i-1]+fibonacci_list[i-2]
    fibonacci_list.append(num)

print(fibonacci_list)

