def rev_list(num_list):
    # print(num_list)
    if len(num_list) == 1:
        return num_list
    else:
        # append won't return anything, which make list = None
        # list = rev_list(num_list[1:]).append(num_list[0])
        list = rev_list(num_list[1:])
        list.append(num_list[0])
        return list


def rev_list_tr(num_list, index, len):
    if len == index:
        return num_list[index:]
    else:
        num_list.append(num_list[index])
        print(num_list)
        return rev_list_tr(num_list, index+1, len)


ls = [4, 5]
m = ls[1:]
m.append(l[0])
print(l)
print(m)

print("reverse list non-tail recursive")
print(rev_list([4, 5]))
print(rev_list([1, 2, 3, 4, 5]))


def linear_search(num_list, value, index):
    res = linear_search(num_list, value, index+1)
    if res == -1:
        return num_list[index] == value
    else:
        return
