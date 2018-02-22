##List Slicing
numbers = [0,100,200,300,400,500,600]
print(numbers[2:5]) # return items from index two to (five-1)
print(numbers[:4]) # returns items before index 4(excluded) ie upto 3(included)
print(numbers[4:]) # returns items from index 4(included)
print(numbers[1:7:2]) # returns items from index 1(included) to 7(excluded) skipping every second entry as the intervavl is 2
print(numbers[::-1]) # when the interval is specified as -1, it prints in reverse
print(numbers[::-2]) # prints from the last in reverse order skipping every second entry