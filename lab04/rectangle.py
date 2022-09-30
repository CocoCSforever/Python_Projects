def main():
    symbol = input("Please enter a single character you \
would like to use as a symbol: ")
    width = int(input("Please enter the width of the rectangle:"))
    while (width < 2):
        width = int(input("Please enter a width which is >= 2:"))
    height = int(input("Please enter the height of the rectangle:"))
    while (height < 2):
        height = int(input("Please enter a height which is >= 2:"))

    for h in range(height):
        if (h == 0 or h == height-1):
            print(symbol * width)
        else:
            print(symbol + " "*(width-2) + symbol)


main()
