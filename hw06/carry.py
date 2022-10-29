def main():
    MAX = 10
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")
    result, carry_list, carry = calculate_sum_carry(list(number1),
                                                    list(number2),
                                                    MAX)
    print(f"{number1} + {number2} = {result}")
    print(f"Number of carries: {carry}")


def calculate_sum_carry(number1, number2, MAX):
    """
    Calculate both the sum and carry of two numbers
    Add a feature to have a visible sum process by
    showing positions of every carry in carry_list
    """
    carry = 0
    carry_list = ['0']
    result_list = []
    max_number, min_number = compare_list(number1, number2)
    length_min = len(min_number)
    length_max = len(max_number)

    carry_list, result_list, carry = manual_sum(length_min, max_number,
                                                carry_list, result_list,
                                                carry, MAX, min_number)
    if (carry_list[0] == '0'):
        result_list = max_number[0:length_max-length_min] + result_list
        carry_list[:0] = ['0']*(length_max-length_min)
    else:
        remain = length_max-length_min
        carry_list, result_list, carry = manual_sum(remain, max_number,
                                                    carry_list, result_list,
                                                    carry, MAX)
    return ''.join(result_list), ''.join(carry_list), carry


def manual_sum(length, list1, carry_list, result_list, carry, MAX, list2=None):
    """
    Receive two numbers in list form, implement sum and carry manually
    """
    len1 = len(list1)
    if (list2 is None):
        for i in range(length):
            sum = int(list1[length-1-i]) + int(carry_list[0])
            carry_list, result_list, carry = calculate_carry(sum, MAX,
                                                             carry_list,
                                                             result_list,
                                                             carry)
        if (carry_list[0] == '1'):
            result_list.insert(0, str(1))
    else:
        len2 = len(list2)
        for i in range(len2):
            sum = int(list1[len1-1-i]) + int(list2[len2-1-i]) \
                + int(carry_list[0])
            carry_list, result_list, carry = calculate_carry(sum, MAX,
                                                             carry_list,
                                                             result_list,
                                                             carry)
    return carry_list, result_list, carry


def calculate_carry(sum, MAX, carry_list, result_list, carry):
    """Calculate carry for every adding activity of two digits"""
    if (sum >= MAX):
        carry_list.insert(0, str(1))
        result_list.insert(0, str(sum-MAX))
        carry += 1
    else:
        carry_list.insert(0, str(0))
        result_list.insert(0, str(sum))
    return carry_list, result_list, carry


def compare_list(number1, number2):
    """
    Receive two number_list
    Return the longer list first and then the shorter list
    """
    if (len(number1) >= len(number2)):
        return number1, number2
    else:
        return number2, number1


main()
