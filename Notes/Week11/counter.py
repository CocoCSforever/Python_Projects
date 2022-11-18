import sys


def main(number):
    """Print all values from 1 to number to the console.
Without using:
    - lists, sets, or dictionaries
    - list comprehensions
    - built-in functions other than 'print' (e.g. 'range')
    - for loops
    - while loops
    - '=' (assignment operator)
    - '+=' etc (increment operators of any kind)
Okay to use:
    - if statements
    - comparison operators ('==', '<=', '>=')
    - arithmetic operations ('+', '*', '-' etc)
    - helper functions that follow the rules above
"""
    count(1, number)


def count(value, num):
    if value <= num:
        print(value)
        count(value+1, number)


main(int(sys.argv[1]))
