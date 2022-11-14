import re

a = "Mei Kumo"
b = "Lena S. Park"
c = "J. Ellery Gray"
d = "Fionn MacCumhaill"
e = "Anne Marie Blake"
f = "Jan Marcus Antonius Van Beek"
g = [a, b, c, d, e, f]
for i in g:
    print(re.findall(r"^\w(?:\.|\w+)\s(\w)(?:\.|\w+)\s\w+$", i))
# print(re.findall(r"^[A-Z](?:\.|\w+)\s(\w)(?:\.|\w+)\s\w", b))
# print(re.findall(r"^[A-Z](?:\.|\w+)\s(\w)(?:\.|\w+)\s\w", c))
# print(re.findall(r"^[A-Z](?:\.|\w+)\s(\w)(?:\.|\w+)\s\w", d))
# print(re.findall(r"^[A-Z](?:\.|\w+)\s(\w)(?:\.|\w+)\s\w", e))
# print(re.findall(r"^[A-Z](?:\.|\w+)\s(\w)(?:\.|\w+)\s\w", f))
