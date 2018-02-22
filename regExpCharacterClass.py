import re

pattern = r"[A-Z][A-z][0-9]" #for <LETTER><LETTER or letter><Number> 3 length strs

if re.match(pattern,"Ac1"):
    print("Match")