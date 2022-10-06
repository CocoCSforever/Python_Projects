import math
import sys


# naive: unapproachable to sth that not be optimized or thought to be nuang
# improvement to naive method:
# 1. exclude even number
# 2. don't consider div larger than square root, bc. they are pairs,
# every div larger than sr would be paired to a number less than sr
# which has been considered
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

    # candidate = START_VAL + 1
    # while(candidate <= max_val):

    for candidate in range(START_VAL+1, max_val+1, 2):
        is_prime = True

        div = START_DIVISOR
        while (div <= math.sqrt(candidate) and is_prime):
            # % remainder operator
            # interpret nonboolean to boolean: 0 to falsy value
            # which behaves like false
            if (not (candidate % div)):
                is_prime = False
            div += 1

        if (is_prime):
            print(candidate)
        # candidate += 1
    pass


main(int(sys.argv[1]))
