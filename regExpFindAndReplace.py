import re
string = "My name is delton and Hi Im delton"
pattern = r"delton"
newstring = re.sub(pattern,"Antony",string)#sub function takes the input pattern, string to replace and sourcec string variable to operate on. It will return the repllaced string
print(newstring)