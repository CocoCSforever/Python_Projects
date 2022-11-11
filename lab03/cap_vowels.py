import re


# in_string = input("Please enter a string: ")
# low_in_string = in_string.lower()
# res = low_in_string.replace("a", "A")
# res = res.replace("e", "E")
# res = res.replace("i", "I")
# res = res.replace("o", "O")
# res = res.replace("u", "U")
# print(res)

m = ", asdf ,"
m = m.replace(',', 'COMMA')
m = "Mrunichr(257)"
m = "goodunichr(257)"
m = re.sub(r'([A-Z]([a-z]+)?)unichr\(257\)', r'\1.', m)
# print(re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
#        r'static PyObject*\npy_\1(void)\n{',
#        'def myfunc():'))
z = "$#%^&"
z = re.sub(r'#', r'.', z)
print(z)
# print(re.match(r'([A-Z][a-z]+)unichr(257)', m))