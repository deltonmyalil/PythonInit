from itertools import count
for x in count(3): #count(i) starts counting from i to infinity
    print(x)
    if x ==20:
        break

from itertools import accumulate,takewhile

numbers = list(accumulate(range(8)))#keeps adding the result to the current value ie accumulation
print(numbers)

print(list(takewhile(lambda x: x<=6,numbers))) #take items from a list when condition ie lambda returns true