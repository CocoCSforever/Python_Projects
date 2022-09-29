# A program implementing the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula

import math


def main():
    a = float(input("Enter the coefficient of x squared: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant: "))

    # Use the quadratic formula to compute the roots.
    # Assumes a positive discriminant.

    discriminant = b**2 - (4 * a * c)
    root1 = ((-b) + math.sqrt(discriminant)) / (2 * a)
    root2 = ((-b) - math.sqrt(discriminant)) / (2 * a)

    print("Root #1:", round(root1, 3))
    print("Root #2:", round(root2, 3))


main()

# Test with
# 1, 3, -4
# 2, -4, -5
# 1, -1, -3
