print(",".join(["Apple","Banana","Orange"]))#List items separated with a comma
print(":".join(["Apple","Banana","Orange"]))#List items separated with a colon
print(" and ".join(["Apple","Banana","Orange"]))#List items separated with <space>and<space>
#print(" and ".join([1,2,3,4,5,6,7])) this wont work as join is a string function which expects string arguments

#replace(substring,string) function - replaces a substrinng with another
string = "Hello There"
string2 = string.replace("There","World") #replalcec function does not change the sourcec string but returns a string which you could save to another new string
print(string2)
print(string) # as you can see, the original string is unchanged
#howevver you can directly print it as the return value of the string function replace() is the replaced string
print("Hello Bros".replace("Hello","Goodbye"))

#startswith function checks if a string starts with the given substring. If it does, it will return boolean True
startswithBooleanReturn1 = string.startswith("Hello")
print(startswithBooleanReturn1)
startswithBooleanReturn2 = string.startswith("Goodbye")
print(startswithBooleanReturn2)

#endswith - to check if a string ends with a word
endswithBooleanReturn1 = string.endswith("World")
print(endswithBooleanReturn1)
endswithBooleanReturn2 = string.endswith("There")
print(endswithBooleanReturn2)

#Convert into uppercase - upper()
stringcase = "thIS iS aN AuTiSTiC sTriNG"
upperString = stringcase.upper()
print(stringcase)
print(upperString)#This also does not modify the sourcce string, but just returns an Upperccase string that could be saved to another variable

#Convert autistic string to lowercacse
lowerString = stringcase.lower()
print(lowerString)

#Capitalize the first letter
capitalizedString = lowerString.capitalize()
print(capitalizedString)

multipleSentences = "hi this is the first sentence. this is the second sentence"
capitalizedSentence = multipleSentences.capitalize()
print(capitalizedSentence) #Does not work in capitalizing multiple sentences