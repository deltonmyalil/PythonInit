import re

pattern = r"(Rep)*a" #0 or multiple repeatitions of "Rep"

if re.match(pattern,"RepRepa"):
    print("Match")
if re.match(pattern,"Repa"):
    print("Match")
if re.match(pattern,"a"):
    print("Match")
