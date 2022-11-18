def triangular_number(num):
    # use triangular formula that sum = (1+n)*n/2 instead of a for loop to add
    return int((1+num) * num/2)


def main():
    list = []
    command = input("Enter a number, or enter 'done': ")
    while (command != "done"):
        res = triangular_number(int(command))
        print(f"The triangular number for {int(command)} is {res}")
        list.append(res)
        command = input("Enter a number, or enter 'done': ")
    print(list)


main()
