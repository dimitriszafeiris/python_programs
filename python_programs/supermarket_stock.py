#Supermarket stock
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for x in food:
        if stock[x] > 0:
            total = total + prices[x]
            stock[x] = stock[x] - 1
    return total

#shopping_list = ["banana", "orange", "apple"]
while True:
     product1=input("Choose product1. We have banana,orange, apple or pear:")
     if product1=='banana' or product1=='orange' or product1=='apple' or product1=='pear':
        break
    
while True:
    product2=input("Choose product2. We banana,orange, apple or pear:")
    if product2=='banana' or product2=='orange' or product2=='apple' or product2=='pear':
        break
    
while True:
    product3=input("Choose product2. We banana,orange, apple or pear:")
    if product3=='banana' or product3=='orange' or product3=='apple' or product3=='pear':
        break
    
shopping_list=[product1,product2,product3]
compute_bill(shopping_list)

#print what you have bought...
for x in shopping_list:
    print ("You have bought 1 %s." % x)
    
#print remaing stock after our shopping...
for x in stock:
    print ("We have %s remaining %ss." % (stock[x],x))