import math
import sys


def main(radius):
    radius = int(radius)
    for y in range(2*radius):
        for x in range(2*radius):
            distance_x_square = (x-radius)**2
            distance_y_square = (y-radius)**2
            dist = math.sqrt(distance_x_square + distance_y_square)
            if (dist < radius):
                print("*", end=""),
            else:
                print(" ", end=""),
        print("")


main(sys.argv[1])
