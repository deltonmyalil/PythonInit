# list comprehension is used to create a list automatically
list1 = [x for x in range(10)] # a list of numbers is automatically made
print(list1)
listsquares = [x**2 for x in range(10)] # a list of squares of numbers is automaticaclly made
print(listsquares)
listcubes = [x**3 for x in range(10)] # a list of cubes of numbers is automatically made
print(listcubes)
list2 = [x*2+3 for x in range(10)]
print(list2)
listWithCondition = [x**2 for x in range(10) if (x**2)%2==0] # here the if condition is also evaluated along with the list generation - only even squares of numbers will be generated
print(listWithCondition)