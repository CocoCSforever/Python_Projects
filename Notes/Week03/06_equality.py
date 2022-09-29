a = "Hello Wiggly World"[:5]
b = "Hello Wild World"[:5]

print(a)
print(b)

# Evaluate equality
if (a == b):
    print("These strings are equal")
else:
    print("These strings are not equal")

if (a is b):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

a = b

if (a is b):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

e = "Hello, new string"
f = "Hello, new string"

if (e is f):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

g = f[:]

if (f is g):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

h = ''.join(f)

print(h)

if (f is h):
    print("These strings are IDENTICAL, i.e. the same object")
else:
    print("These strings are two separate objects")

my_join = '--'.join("Seattle")
print(my_join)










