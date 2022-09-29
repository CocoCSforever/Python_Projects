#######################################
#
# temp_converter.py
#
#######################################


def main():
    # By convention, constants are named with all
    # caps. There is no support in Python for ensuring
    # that constants remain unchanged.
    BASE = 32
    CONVERSION_FACTOR = 5.0/9.0
    TEMP_PRECISION = 2

    # Get input from user.
    fahrenheit_temp = float(input("Input a temperature in Farhenheit: "))

    celsius_temp = (fahrenheit_temp - BASE) * CONVERSION_FACTOR

    # Print/output results.
    print("That would be", round(celsius_temp, TEMP_PRECISION),
            "degrees Celsius")


main()
