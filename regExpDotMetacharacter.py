import re
pattern = r"Del.on"
if re.match(pattern,"Deleon"):
    print("Match found")
else:
    print("No match with Del<anyChar>on")