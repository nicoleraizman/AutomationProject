# get prices of 5 products. print the total and the average price.
# if the total prices reaches 200, we skip the current product

prices=""
total=0
count=0

for i in range(5):
    price = int(input(f"Enter price: {i+1}: "))
    if total+price>200:
        print("This product is too expensive!")
        continue
    prices = prices + str(price)+" "
    total+=price
    count+=1
# instead of continue you can write else:

print("total:",total)
print("prices:",prices)
print("average:",total/count)