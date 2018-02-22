numbers = [4, 5, 6]
newString = "Numbers - {0},{1},{2}".format(numbers[0], numbers[1], numbers[2])
print(newString)

# raw format
newString1 = "The numbers are - {0},{1},{2}".format(1, [2,3,4,5,6], 3) #here always give the placeholders as {0}{1}{2}... that is they start with 0 as placeholder number one
print(newString1)
#start placeholder index as 0 with curly brackets, arguments to format function can be anything including lists

#useful for mentioning dates
date = "Today's date is {0}/{1}/{2}".format(12,"Feb",2018)
print(date)

print("Or rather directly print without a intermediate variable as today's date is {0}/{1}/{2}".format(12,"Feb",2018))
#this is somewhat equivalent to using %d,%u%f%s%c etc in C

x = int(input("Enter x>>>"))
y = int(input("Enter y>>>"))
3print("What you will get is {0}/{1}".format(x,y))
print ("Another example {a}++{b}".format(b=10,a=20)) # will return 20++10 as the order of the variables are mentioned as a++b in the placeholders