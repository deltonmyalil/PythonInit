#similar to list but no duplicates
#use {} instead of []

numbers = {1,2,3,4,5,6}
print(5 in numbers) #returns True
print(0 in numbers) #returns False

#to add elements to set, do
numbers.add(7)
print(numbers)

#to remove fromm set
numbers.remove(1)
print(numbers)

#setOps
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A|B) #| is union
print(A&B) #& is intersection
print(A-B) # - is difference operation

C = {2,2,3,4,4,5,6}
print(C) #multisets will get converted to sets by duplElim