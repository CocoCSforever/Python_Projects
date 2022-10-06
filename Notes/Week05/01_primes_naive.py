import math
import sys


# naive: unapproachable to sth that not be optimized or thought to be nuang
def main(max_val):
    # doc string:
    # internal documentation, more formal than comment
    # anytime you want to define a function, should write doc string
    """
    Print out prime numbers
    from 2 to max_val
    """
    START_VAL = 2
    START_DIVISOR = 2

    print(START_VAL)

    candidate = START_VAL + 1
    while (candidate <= max_val):
        is_prime = True
        div = START_DIVISOR

        while (div < candidate):
            # % remainder operator
            # interpret nonboolean to boolean: 0 to falsy value
            # which behaves like false
            if (not (candidate % div)):
                is_prime = False
            div += 1

        if (is_prime):
            print(candidate)
        candidate += 1


main(int(sys.argv[1]))
