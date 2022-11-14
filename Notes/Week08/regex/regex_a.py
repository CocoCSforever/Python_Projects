import re

regex = "^([A-Za-z0-9]| )+$"

p = re.compile(regex)

str = input("string: ")
if (re.search(p, str)):
    print(True)
else:
    print(False)

a = [{'a', 'b', 'c'}, 5]
g = {'a': 5, 'b': 6, 'c': 7}
print(g['b'] == 6)
# s = a[-1]
# print(s)
a = a[:-1]
print(a)

x = {
    'a': 'b',
    'c': {'d': {'e': 'f'}},
    'g': {'h': 'i'},
    'j': {'k'}
}
print(x['c']['d']['e'])
