# get prices of 5 products. print the total and the average price.
prices=""
total=0

for i in range(5):
    price = int(input(f"Enter price: {i+1}: "))
    prices = prices + str(price)+" "
    #total=total+price
    total+=price
print("total:",total)
print("prices:",prices)
print("average:",total/5)

