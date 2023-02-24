from functools import cmp_to_key
list = [("aaaa", "aaaa"), ("aaaa", "aaba"), ("aaaa", "aaab"),
        ("ccba", "aaaa"), ("cacc", "aaaa")]

# Test
# print(list[0][0] == list[1][1]);
# print(list[0][0] == list[1][0]);
# print(list[0][1] < list[1][1]);
# print(list[1][0]);
# print(list[1][1]);

print(list)


def cmp(a, b):
    if (a[0] == b[0]):
        return 1 if a[1] < b[1] else -1
    else:
        return -1 if a[0] < b[0] else 1


# sort by lambda function
listr1 = sorted(list,
                key=cmp_to_key(lambda a, b: (1 if a[1] < b[1] else -1)
                               if a[0] == b[0] else (-1 if a[0] < b[0] else 1)),
                reverse=True)
print(listr1)

# sort using helper function
listr2 = sorted(list,
                key=cmp_to_key(cmp),
                reverse=True)
print(listr2)


# sort by first element in ascending order
list2 = [("c", "d"), ("a", "b")]
list2 = sorted(list2,
               key=lambda x: x[0])
print(list2)

# sort by first element in ascending order
list3 = [("c", "d"), ("a", "b")]
list3 = sorted(list3,
               key=cmp_to_key(lambda a, b: -1 if a[0] < b[0] else 1),
               reverse=False)
print(list3)

# sort by first element in ascending order
# if first is same, sort by second element in descending order
list4 = [(2, 4), (2, 5), (5, 1), (3, 1), (4, 2)]
list4 = sorted(list4,
               key=cmp_to_key(cmp),
               reverse=False)  # True in descending order, False in ascending order
print(list4)
