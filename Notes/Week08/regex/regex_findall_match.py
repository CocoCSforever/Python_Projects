import re

a = "555 Hello World 1212"
b = re.findall(r"[0-9]\s(\w+)\s", a)
d = re.findall(r"[0-9]\s(\w+)", a)
print(b)  # ['Hello']
print(d)  # ['Hello']
c = "5 Hello "
