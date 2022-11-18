import sys


def main(number):
    # Print out the triangular number for
    # number (sum of integers from 0 to number)
    print(triangular(number))


# Define a recursive function called 'triangular'
# to calculate the number
def triangular(n):
    if (n == 0):
        # base case
        return 0
    else:
        # recursive case
        return n + triangular(n-1)


main(int(sys.argv[1]))
