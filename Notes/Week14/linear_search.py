def linear_search(num_list, value):
    """Find index of val recursively"""
    if len(num_list) == 0:
        return -1
    elif num_list[0] == value:
        return 0
    else:
        index = linear_search(num_list[1:], value)
        return 1+index if index > -1 else index


def linear_search_tr(num_list, value, index):
    """Find index of val using tail recursion"""
    if index == len(num_list):
        return -1
    elif num_list[index] == value:
        return index
    else:
        return linear_search_tr(num_list, value, index+1)


print("Linear search non-tail recursive:")
print(linear_search([1, 2, 3, 4, 5], 1))
print(linear_search([1, 2, 3, 4, 5], 4))
print(linear_search([1, 2, 3, 4, 5], 6))

print("Linear search tail recursive:")
print(linear_search_tr([1, 2, 3, 4, 5], 1, 0))
print(linear_search_tr([1, 2, 3, 4, 5], 4, 0))
print(linear_search_tr([1, 2, 3, 4, 5], 6, 0))
