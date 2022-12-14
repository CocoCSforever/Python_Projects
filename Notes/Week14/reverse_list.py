def rev_list(num_list):
    """Reverse a list recursively"""
    if len(num_list) == 1:
        return num_list
    else:
        # append won't return anything, which make list = None
        # list = rev_list(num_list[1:]).append(num_list[0])
        list = rev_list(num_list[1:])
        list.append(num_list[0])
        return list


def rev_list_s(num_list):
    """Sample solution: Reverse a list recursively"""
    if len(num_list) == 1:
        return num_list
    else:
        # Append: Using concatenate list + list
        return rev_list_s(num_list[1:]) + [num_list[0]]


def rev_list_tr(num_list, index, len):
    """index start from len-1,reverse one by one"""
    if index < 0:
        return num_list[len:]
    else:
        num_list.append(num_list[index])
        return rev_list_tr(num_list, index-1, len)


def rev_list_tr_s(input, output, length):
    """Sample solution: index start from len-1,reverse one by one"""
    if len(output) == length:
        return output
    else:
        return rev_list_tr_s(input[1:], [input[0]]+output, length)


print("Reverse list non-tail recursive")
print(rev_list([4, 5]))
print(rev_list([1, 2, 3, 4, 5]))

print("Sample Solution: Reverse list non-tail recursive")
print(rev_list_s([4, 5]))
print(rev_list_s([1, 2, 3, 4, 5]))

print("Reverse list tail recursive")
print(rev_list_tr([4, 5], 1, 2))
print(rev_list_tr([1, 2, 3, 4, 5], 4, 5))

print("Sample Solution: Reverse list tail recursive")
print(rev_list_tr_s([4, 5], [], 2))
print(rev_list_tr_s([1, 2, 3, 4, 5], [], 5))
