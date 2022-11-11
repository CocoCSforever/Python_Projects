import sys


def main():
    # file_name = sys.argv[1]
    char_counts = {}
    total_count = 0

    try:
        f = open("corpse_bride.txt")
    except FileNotFoundError:
        print("Can't find", "corpse_bride.txt")
        return
    list = []

    # for line in f:
    #     # for line will read the empty line in the middle
    #     # but won't read the last trailing new line
    #     list.append(line.strip().split(','))
    print(" ggasfih asfaf  asfasfh ".split())
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())  # print('')
    list = f.readline().strip().split(',')
    print(list)
    # print(list[3])
    print("     ".split(","))


main()
