import sys


def main(number):
    # we define odd and even integer as (2n-1) and (2n)
    # use // to get the integer quotient, n is number of lines for first half
    n = (number+1)//2

    # from line 1 to line n
    # for each line with i as index, we have (n-i) whitespaces on each side
    # and (2*i-1) "*" in the middle.
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))

    # from line n+1 to line (2n-1) or (2n)
    # start is the number of lines for second half
    start = number//2
    for i in range(start, 0, -1):
        print(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))


main(int(sys.argv[1]))
