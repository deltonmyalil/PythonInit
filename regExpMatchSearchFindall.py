import re

pattern = r"del" #r"something" means a raw string
if re.match(pattern,"delAntidisbfkjdb"): #string starts with pattern ie r"del"
    print("match fouund")
else:
    print("No match found")

if re.search(pattern,"delAntidisbfkjdb"): #search the string for substring
    print("Substring searched and found")
else:
    print("Substring not found")

if re.findall(pattern,"delAntidisAdelbfkjdb"): #search the string for substring and returns the occurences list of substring
    print("Substring searched and found")
    print("Total occurences of substring:",re.findall(pattern,"delAntidisAdelbfkjdb"))
else:
    print("Substring not found")
