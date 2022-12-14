def binary_search(num_list, value):
    """Best: Recursively binary search
    using non-tail recursion"""
    if len(num_list) == 0:
        return -1

    mid = len(num_list)//2
    if num_list[mid] == value:
        return mid
    elif num_list[mid] > value:
        return binary_search(num_list[:mid], value)
    elif num_list[mid] < value:
        index = binary_search(num_list[mid+1:], value)
        return mid + 1 + index if index > -1 else index


def binary_search_s(num_list, value):
    """Recursively binary search
    using non-tail recursion"""
    mid = len(num_list)//2
    if num_list[mid] == value:
        return mid
    elif len(num_list) == 1:
        return -1
    elif num_list[mid] > value:
        return binary_search_s(num_list[:mid], value)
    elif num_list[mid] < value:
        index = binary_search_s(num_list[mid:], value)
        return mid + index if index > -1 else index


def binary_search_tr(num_list, value, left, right):
    """Recursively binary search using tail recursion"""
    if left > right:
        return -1
    mid = left + (right-left)//2
    if num_list[mid] == value:
        return mid
    elif num_list[mid] > value:
        return binary_search_tr(num_list, value, left, mid-1)
    elif num_list[mid] < value:
        return binary_search_tr(num_list, value, mid+1, right)


def binary_search_tr_s(num_list, value, lower):
    """Recursively binary search using tail recursion
    lower is the index of the first element of the current list
    so we can add it to the total index later"""
    mid = len(num_list)//2
    # mid must be within the range
    # num_list cannot be empty
    if num_list[mid] == value:
        return lower + mid
    elif len(num_list) == 1:
        return -1
    elif num_list[mid] > value:
        return binary_search_tr_s(num_list[:mid], value, lower)
    elif num_list[mid] < value:
        return binary_search_tr_s(num_list[mid:], value, lower+mid)


def binary_search_tr_m(num_list, value, lower):
    """Best:
    Recursively binary search using tail recursion
    lower is the index of the first element of the current list
    so we can add it to the total index later"""
    if len(num_list) == 0:
        return -1

    mid = len(num_list)//2
    if num_list[mid] == value:
        return lower + mid
    elif num_list[mid] > value:
        return binary_search_tr_m(num_list[:mid], value, lower)
    elif num_list[mid] < value:
        return binary_search_tr_m(num_list[mid+1:], value, lower+mid+1)


print("*Yijia Binary search non-tail recursion")
print(binary_search([1, 2, 3, 4, 5], 1))
print(binary_search([1, 2, 3, 4, 5], 4))
print(binary_search([1, 2, 3, 4, 5], 6))

print("Sample solution: Binary search non-tail recursion")
print(binary_search_s([1, 2, 3, 4, 5], 1))
print(binary_search_s([1, 2, 3, 4, 5], 4))
print(binary_search_s([1, 2, 3, 4, 5], 6))

print("Binary search tail recursion")
print(binary_search_tr([1, 2, 3, 4, 5], 1, 0, 4))
print(binary_search_tr([1, 2, 3, 4, 5], 4, 0, 4))
print(binary_search_tr([1, 2, 3, 4, 5], 6, 0, 4))

print("Sample solution: Binary search tail recursion")
print(binary_search_tr_s([1, 2, 3, 4, 5], 1, 0))
print(binary_search_tr_s([1, 2, 3, 4, 5], 4, 0))
print(binary_search_tr_s([1, 2, 3, 4, 5], 6, 0))

print("*Yijia solution: Binary search tail recursion")
print(binary_search_tr_m([1, 2, 3, 4, 5], 1, 0))
print(binary_search_tr_m([1, 2, 3, 4, 5], 4, 0))
print(binary_search_tr_m([1, 2, 3, 4, 5], 6, 0))
