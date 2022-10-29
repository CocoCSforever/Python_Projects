def main():
    size = int(input("Input cube size (multiple of 2): "))
    draw_cube(size)


def draw_cube(n):
    draw_1st_line(n)
    draw_part2(n)
    draw_part3(n)
    draw_part4(n)
    draw_last_line(n)


def draw_1st_line(n):
    """
          +--------------------+
    """
    print(" "*(n//2+1) + "+" + "-"*(2*n) + "+")


def draw_part2(n):
    """
         /                    /|
        /                    / |
       /                    /  |
      /                    /   |
     /                    /    |
    +--------------------+     |
    """
    for i in range(n//2):
        print(" "*(n//2-i) + "/" + " "*(2*n) + "/" + " "*i + "|")
    print("+" + "-"*(2*n) + "+" + " "*(n//2) + "|")


def draw_part3(n):
    """
    |                    |     |
    |                    |     |
    |                    |     |
    |                    |     |
    |                    |     +
    """ 
    for i in range(n//2-1):
        print("|" + " "*(2*n) + "|" + " "*(n//2) + "|")
    print("|" + " "*(2*n) + "|" + " "*(n//2) + "+")


def draw_part4(n):
    """
    |                    |    /
    |                    |   /
    |                    |  /
    |                    | /
    |                    |/
    """
    for i in range(n//2):
        print("|" + " "*(2*n) + "|" + " "*(n//2-1-i) + "/")


def draw_last_line(n):
    """
    +--------------------+
    """
    print("+" + "-"*(2*n) + "+")


main()
