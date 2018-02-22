numbers = {
    #key:value
    1:"one",
    2:"two",
    3:"three"
}
print(1 in numbers) #in returns boolean ie true or false. Here we can check if the key 1 is in numbers, if it is, it returns True
print(2 in numbers) #will return false
print(numbers[2]) #to retrieve the value contained with key - 2
#print(numbers[5]) - this is what dictName[key] cannot do - it will return an error if the key is not in dictName
#get function is used to get the value associated with a key in dict
print(numbers.get(3))
print(numbers.get(5)) # - this is the adv of get over dictName[key] - even if the key value is not in list, it will return NONE without any error halting

numbers.update({4:"four",
                5:"five"}) #this is how you add new item to a dictionary
print(numbers)