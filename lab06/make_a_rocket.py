import sys


def main(data):
    # get the size of input argvs and call draw function
    if (len(data) == 3):
        draw_default_rocket(int(data[1]), int(data[2]))
    else:
        draw_default_rocket(int(data[1]), int(data[2]), int(data[1]))


def draw_default_rocket(width, length, color=None):
    # draw_default_rockets includes three parts of the rocket
    draw_nose_cone(width)
    draw_fuselage(width, length, color)
    draw_tail(width)


def draw_nose_cone(width):
    start_w = start_nose(width)
    print_incre(start_w, width)


def draw_fuselage(width, length, color):
    for i in range(length):
        if (color is None):
            # is not striped
            print_multi_lines("X"*width, width)
        else:
            # is striped: half "-"(floor half), half"X
            print_multi_lines("-"*width, width//2)
            print_multi_lines("X"*width, (width+1)//2)


def draw_tail(width):
    start_w = start_tail(width)
    # print the narrowing down lines ahead of bottom part
    print_incre(start_w, width)
    # print the bottom two lines
    print_multi_lines("*"*width, 2)


#  helper functions
# generate start_width of nose for even and odd width
def start_nose(number):
    # start_w is the width of the first line in nose part:
    # 2 for even, 1 for odd
    if (number % 2 == 0):
        return 2
    else:
        return 1


# generate start_width of tail for even and odd width
def start_tail(number):
    # start_w is the width of the first line in tail part
    # should be even for even width, odd for odd width
    if (number % 2 == 0):
        return (number//4)*2
    else:
        return (number//4)*2+1


# help print several lines which consist of space and special chars
# numbers of each char will increment or decrement
def print_incre(start, end, increment=2):
    for i in range(start, end, increment):
        space_length = (end-i)//2
        print(" "*(space_length) + "*"*i + " "*(space_length))


# help print the same line for several times
def print_multi_lines(str, number):
    for i in range(number):
        print(str)


main(sys.argv)
