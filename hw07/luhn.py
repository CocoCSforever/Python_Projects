def main():
    number = input("Please enter the account number for validation: ")
    validate_number(number)


def validate_number(number):
    number = [int(n) for n in number]
    if (is_valid(number)):
        print("The number is valid.")
    else:
        print("The number is not valid")


def is_valid(number):
    for i in range(len(number)-2, -1, -2):
        number[i] = number[i]*2
        if (number[i] >= 10):
            number[i] = number[i] - 9

    # Add the sum of modified digits and skipped digits
    sum = 0
    MODULUS = 10
    for n in number:
        sum += n
    if (sum % MODULUS == 0):
        return True
    return False


main()
