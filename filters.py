from random import randint
newlist = [randint(1,50) for x in range (10)]
print(newlist)
evenNos = list(filter(lambda x: x%2==0,newlist)) #filter chose the els of the list where the boolean condition of the lambda returned true
print(evenNos)

def isOdd(n):
    if n%2 == 0:
        return False
    else:
        return True

nextlist = [randint(1,100) for x in range(20)]
print(nextlist)
oddNos = list(filter(isOdd,nextlist)) #filter using a function instead of a lambda
print(oddNos)

anotherList = [randint(1,60) for j in range(10)]
print(anotherList)
divByThree = list(filter(lambda x:x%3==0,anotherList)) #if the first parameter of the filter function (should be a callable parameter like a function or a lambda) returns True, the item is included in the returned list
print(divByThree)