def main():
    width = int(input("Please enter the width of chrismas_tree:"))
    while (width < 3 or width % 2 == 0):
        width = int(input("Please enter an odd number which is >= 3:"))
    n = int(width/2)
    print(" " * n + "*" + " " * n)
    for h in range(1, n):
        print(" "*(n-h) + "/" + " "*(2*h-1) + "\\")
    print("/" + "_"*(width-2) + "\\")


main()
