import sys


def main(height):
    for row in range(1,height+1):
        print("*"*row)


main(int(sys.argv[1]))
