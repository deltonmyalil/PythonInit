def add2(x):
    return x+2
newlist = [x*10 for x in range(1,6)]

add2list = list(map(add2,newlist)) #here, the function add2 will be applied to each element of the list
print(add2list)

mul10list = list(map(lambda x:x*10,newlist)) #using lambda instead of function
print(mul10list)

from random import randint
randomlist = [randint(1,100) for x in range (10)] #generating a random list
print(randomlist)
sub10list = list(map(lambda x:x-10,randomlist)) #using lambda in a map to sub 10 from the els of the list
print(sub10list)