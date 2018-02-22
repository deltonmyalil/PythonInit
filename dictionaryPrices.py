products = {
    "book":30,
    "pen":20,
    "eraser":5,
    "calculator":800,
    "glasses":1500,
    "wallet":1750
}
flag = True
while(flag):
    thing = input("Enter the item to check price>>>")
    if thing in products:
        print("price of the {0} is {1}".format(thing,products.get(thing)))
    else:
        print("Not Found, would you like to add it?(y/n)")
        response = input()
        if response == "y":
            value = int(input("Enter the price of {0}".format(thing)))
            products.update({thing:value})
    cont = input("Would you like to continue?(y/n)")
    if cont == "n":
        flag = False
print("Thank you")

'''products.update({"apple":40})
print(products)
'''