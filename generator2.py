def evenNos(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(evenNos(21)))