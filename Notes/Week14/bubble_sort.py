# def bubble_sort(num_list):
#     swap = False
#     for j in range(1, len(num_list)):
#         if num_list[j] < num_list[j-1]:
#             num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
#             swap = True

#     if not swap:
#         return
#     else:
#         print(num_list[:-1])
#         bubble_sort(num_list[:-1])

def bubble_sort(num_list):
    swap = False
    for j in range(1, len(num_list)):
        if num_list[j] < num_list[j-1]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
            swap = True

    if not swap:
        return num_list
    else:
        # print(num_list[:-1])
        return bubble_sort(num_list[:-1]) + [num_list[-1]]


def bubble_sort_tr(num_list, index):
    """no return value"""
    swap = False
    for j in range(1, index+1):
        if num_list[j] < num_list[j-1]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
            swap = True

    if not swap:
        return
    else:
        # print(num_list[:-1])
        bubble_sort_tr(num_list, index-1)


def bubble_sort_trr(num_list, index):
    swap = False
    for j in range(1, index+1):
        if num_list[j] < num_list[j-1]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
            swap = True

    if not swap:
        return num_list
    else:
        # print(num_list[:-1])
        bubble_sort_tr(num_list, index-1)


array = [50, 20, 14, 5, 2, -10, -25, -30]
bubble_sort_tr(array, 7)
print(array)

print(bubble_sort(array))
print(bubble_sort_trr(array, 7))
