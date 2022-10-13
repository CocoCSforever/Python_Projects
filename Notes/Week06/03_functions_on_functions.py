def main():
    function_caller(f1)
    function_caller_arg(f2, "Hi there!")
    function_caller(f3)
    function_caller(f3())
    # without return value, f3() itself as NoneType object is not callable


def function_caller(foo):
    print("I call a function")
    foo()


def function_caller_arg(foo, arg):
    print("I call a function with an argument")
    foo(arg)


def f4():
    print("I'm function f4")


def f3():
    print("I'm function f3")
    return f4


def f2(some_string):
    print("I'm f2, here's my argument:", some_string)


def f1():
    print("I'm function f1")


main()
