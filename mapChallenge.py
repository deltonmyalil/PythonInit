from random import randint
def discount10(x):
    return x - .1*x
priceList = [randint(50,100) for x in range(10)]
print("Price list is ",priceList)
discountList = list(map(discount10,priceList))
print(discountList)