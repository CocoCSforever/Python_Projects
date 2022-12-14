def add_list(num_list):
    """Add up a list of numbers recursively
    List -> Number"""
    # if len(num_list) > 0:
    #     return num_list.pop(0) + add_list(num_list)
    # else:
    #     return 0
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + add_list(num_list[1:])


def add_list_tr(num_list, index, total):
    """Add up a list of numbers tail recursively
    List Number Number -> Number"""
    """Tail recursion: all of the operations that need to happen
    are going to happen before the recursive call."""
    if (len(num_list) == index):
        return total
    else:
        total += num_list[index]
        return add_list_tr(num_list, index+1, total)


print("Add list non-tail recursive")
print(add_list([1, 2, 3, 4, 5]))

print("Add list tail recursive")
print(add_list_tr([1, 2, 3, 4, 5], 0, 0))
