import sys


def main(number):
    list = []
    # set the two default start of Fibonacci numbers
    list.append(0)
    list.append(1)

    # each Fibonacci number is the sum of two preceding numbers(i-1) and (i-2)
    for i in range(2, number):
        list.append((list[i-2] + list[i-1]))
    print(list)


main(int(sys.argv[1]))
