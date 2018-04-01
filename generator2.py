def evenNos(x):
    for i in range(x):
        if i%2==0:
            yield i  ##just returns

print(list(evenNos(21)))