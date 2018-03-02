import re
pattern = r"^d....n$" # any str that starts with d and have 4 chars in between and ends with n

if re.match(pattern,"delton"):
    print("Match")

print(pattern)