# get prices of 5 products. print the total and the average price.
# if the total prices reaches 200, we stop shopping

prices=""
total=0
count=0

for i in range(5):
    price = int(input(f"Enter price: {i+1}: "))
    prices = prices + str(price)+" "
    #total=total+price
    total+=price
    count+=1
    if total >= 200:
        print("Too expensive! I'm living")
        break

print("total:",total)
print("prices:",prices)
print("average:",total/count)