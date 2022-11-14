import math
import sys


def main(radius):
    radius = int(radius)
    for y in range(2*radius-1):
        for x in range(2*radius-1):
            distance_x_square = (x-radius+1)**2
            distance_y_square = (y-radius+1)**2
            dist = math.sqrt(distance_x_square + distance_y_square)
            if (dist < radius):
                print("*", end=""),
            else:
                print(" ", end=""),
        print("")


# can validate squares of arbitrary size, but every numeric number should
# between 1 and 9. cannot detect whether it is two digits or not
def test(n):
    r = []
    x = 0
    res_c = 0
    res_cc = 0
    n = int(n)
    q = True
    for i in range(n):
        r.append(list(input()))
        r[i] = [int(element) for element in r[i]]
    for i in range(n):
        x += r[0][i]
        res_c += r[i][i]
        res_cc += r[i][n-1-i]
    for i in range(n):
        if (q is True):
            res_h = 0
            res_v = 0
            for j in range(n):
                res_h += r[i][j]
                res_v += r[j][i]
            if (res_h != x or res_v != x):
                q = False
    if q is False:
        print("Not a magic square!")
    else:
        print("This is a magic square!")


test(sys.argv[1])
# main(sys.argv[1])
