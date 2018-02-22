from random import randint
price = randint(60,100)


def studentDiscount(p):
    discount = .1*p
    return p-discount

def regularDiscount(p):
    discount = .05*p
    return p-discount

while True:
    print("Cost of the item =",price)
    type = input("Enter type of customer\nStudent:s\nNon Student:n")
    if type == "s":
        print("Student gets 10% discount")
        newprice = studentDiscount(price)
        print("Discounted price is ",newprice)
        regular = input("Is the customer a regular buyer?(y/n)>>>")
        if regular == "y":
            print("Regular buyers get additional Discount of 5%")
            newprice = regularDiscount(newprice)
            print("Final discounted price is ",newprice)
        else:
            print("Final discounted price is ", newprice)
    else:
        print("Non students need to pay full amount of ",price)
    response = input("Do you want to continue?>>>")
    if response == "n":
        break