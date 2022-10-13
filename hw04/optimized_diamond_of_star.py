import sys
import math


def main(number):
    # we define odd and even integer as (2n-1) and (2n)
    # we get n for (2n-1), (2n+1)/2 for 2n
    midline = (number+1)/2

    for i in range(1, number+1):
        distance = int(abs(i-midline))
        index = int(midline - distance)
        print(" "*distance + "*"*(2*index-1) + " "*distance)


main(int(sys.argv[1]))
