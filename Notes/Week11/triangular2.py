import sys


def main(number):
    # Print out the triangular number for
    # number (sum of integers from 0 to number)
    print(triangular(number, 0, 0))


# Define a recursive function called 'triangular'
# to calculate the number
def triangular(n, count, total):
    if count <= n:
        count += 1
        total += count
        return triangular(n, count, total)
    return total


main(int(sys.argv[1]))
