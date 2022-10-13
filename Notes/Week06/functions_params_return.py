import math


def main():
    """
    Runs demo functions(descritions about what the function should do)
    None -> None
    what the input and output is for the function; arguments/return value
    """
    my_null_return_value = hello_function("World!")
    print(my_null_return_value)
    print(double_num(5))
    print(add_nums(5, 7))
    no_arg_no_return()
    x, y, z = multi_value_return()
    # (x, y, z) = multi_value_return()
    print("x is", x)
    print("y is", y)
    print("z is", z)
    my_tuple = 1, 2, 3
    # my_tuple = multi_value_return()
    print(my_tuple)
    if (is_prime(9)):
        print("Nine is prime!")
    else:
        print("Nine is not prime!")


def hello_function(my_argument):
    """
    prints hello message with argument
    String -> None
    print something to the screen instead of returning anything
    """
    print("Hello,", my_argument)


def double_num(number):
    """
    Double a number
    Number -> Number
    """
    return 2 * number


def add_nums(num1, num2):
    """
    Add two numbers
    Number Number -> Number
    """
    return num1 + num2


def no_arg_no_return():
    """
    Print a string
    None -> None
    """
    print("Here's an IO action with no return value")
    # return by its own returns None
    return


def multi_value_return():
    """
    Returns three values
    None -> Character Character Number
    """
    return 'a', 'b', 10.5


def is_prime(num):
    """
    Evaluate whether a number is prime
    Integer -> Boolean
    """
    for d in range(2, int(math.sqrt(num)+1)):
        if not num % d:
            return False
    return True


# # Correct:
# i, submitted, x, y, a, b = 0
# i = i + 1
# submitted += 1
# x = x*2 - 1
# hypot2 = x*x + y*y
# c = (a+b) * (a-b)

# c = (a+b)*(a-b) + (a+b)*(a-b)

# # Wrong:
# i = i+1
# submitted += 1
# x = x * 2 - 1
# hypot2 = x * x + y * y
# c = (a + b) * (a - b)

if __name__ == "__main__":
    main()
