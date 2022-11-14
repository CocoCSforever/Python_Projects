import re

m = ", asdf ,"
m = m.replace(',', 'COMMA')
m = "Mrunichr(257)"
m = "goodunichr(257)"
m = re.sub(r'([A-Z]([a-z]+)?)unichr\(257\)', r'\2.', m)
# print(re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
#        r'static PyObject*\npy_\1(void)\n{',
#        'def myfunc():'))
z = "$#%^&"
z = re.sub(r'#', r'.', z)
print(z)
# print(re.match(r'([A-Z][a-z]+)unichr(257)', m))
