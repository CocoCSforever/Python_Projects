import re

regex = "^([A-Za-z0-9]| )+$"

p = re.compile(regex)

str = input("string: ")
if (re.search(p, str)):
    print(True)
else:
    print(False)
