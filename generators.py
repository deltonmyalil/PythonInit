def fun():
    counter = 0
    while counter<5:
        yield counter
        counter+=1

for x in fun():
    print(x)