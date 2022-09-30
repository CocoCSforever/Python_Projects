import sys


def main(height, width):
    # if we use _ instead of h, it means that we are not
    # using the value in the range
    # solid case
    for _ in range(0, height):
        print('*' * width)

    # print a hollow rect
    for row in range(0, height):
        if (row == 0 or row == height-1 or width == 1):
            print("*"*width)
        elif (width > 1):
            print("*"+" "*(width-2)+"*")


main(int(sys.argv[1]), int(sys.argv[2]))
