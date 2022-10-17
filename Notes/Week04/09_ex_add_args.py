# Print the sum of space-separated arguments passed to
# the script on the command line. E.g.:

# $ python 09_ex_add_args.py 1 2 3 4 5
# 15

import sys


def main(args):
    print(sum([int(arg) for arg in args]))


main(sys.argv[1:])
