v = "This is a global variable"


# can we chang/reassign the global variable in local method?
def main():
    print("main: ", v)
    f1("a", "b")
    print("main: ", v)
    f2("l", "m", "n")
    f2("l", "m")
    f3()
    print("main: ", v)


def f1(x, y):
    v = "F1 re-assigns v"
    print("f1:", v)
    print("f1:", x)
    print("f1:", y)


# set default value for z
def f2(x, y, z="Default value"):
    print("f2:", x)
    print("f2:", y)
    print("f2:", z)
    print("f2:", v)


def f3():
    global v
    v = "F3 re-assigns global v"
    print("f3:", v)


main()
