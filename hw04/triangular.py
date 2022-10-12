import sys


def main(number):
    # use triangular formula that sum = (1+n)*n/2 instead of a for loop to add
    sum = int((1+number) * number/2)
    print(f"The triangular number of {number} is {sum}")


main(int(sys.argv[1]))
