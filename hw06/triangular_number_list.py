def triangular_number(num):
    # use triangular formula that sum = (1+n)*n/2 instead of a for loop to add
    return int((1+num) * num/2)


def main():
    list = []
    command = input("Enter a number, or enter 'done': ")
    while (command != "done"):
        list.append(triangular_number(int(command)))
        command = input("Enter a number, or enter 'done': ")
    print(list)


main()
