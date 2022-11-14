print("-------Sort List&Dictionary-------")
my_fruit_counter = {
    "banana": 8,
    "fig": 1,
    "orange": 10,
    "kumquat": 5
}


my_list = [5, 3, 2, 4]
print("Sorted list:")
print(sorted(my_list))  # standard ordering for numbers: from smallest to larger
print("Sorted list in reverse order:")
print(sorted(my_list, reverse=True))
print("Sort function doesn't change original list:")
print(my_list)

# wantit ordered by the second element
# key is the particular basis we want to order things
# lambda is a keyword in python
print("----------------------------------")
print("Dictionary before sorted by count:")
print(my_fruit_counter)
fruits_by_count = sorted(
    my_fruit_counter.items(),
    key=lambda x: x[1],
    # key=second_element, only need to pass the name of the function
    reverse=True
)
print("----------------------------------")
print("Sorted return a list after sorting dictionary by count:")
print(fruits_by_count)

# TypeError: '<' not supported between instances of 'str' and 'int'
# my_mixed_up_list = [5, "hello", ("mytuple", 3), 1, "a"]
# print(sorted(my_mixed_up_list))
print("----------------------------------")


# can also use function to replace lambda
def second_element(my_tuple):
    return my_tuple[1]
