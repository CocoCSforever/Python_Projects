def main():
    print("Enter a magic number")
    # use res_c and res_cc to represent two corner-to-corner sum
    res_c = 0
    res_cc = 0
    res = True

    new_list = []
    for _ in range(3):
        num_list = list(input())
        num_list = [int(element) for element in num_list]
        new_list.append(num_list)

    # Can also be a general solution for squares of arbitrary size
    for i in range(3):
        if (res is True):
            res_h = 0
            res_v = 0
            res_c += new_list[i][i]
            res_cc += new_list[i][2-i]
            for j in range(3):
                res_h += new_list[i][j]
                res_v += new_list[j][i]
            if (res_h != 15 or res_v != 15):
                res = False
    if (res_c != 15 or res_cc != 15):
        res = False

    if res is False:
        print("Not a magic square!")
    else:
        print("This is a magic square!")


main()
