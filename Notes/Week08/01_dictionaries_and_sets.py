my_empty_dictionary = {}

my_fruit_counter = {
    "banana": 7,
    "fig": 1,
    "orange": 10,
    "kumquat": 5
}
# we can have different type of keys in the same dictionary
# such as 20: "pear", but we cannot sort such dictionary
my_fruit_counter["banana"] += 1
print(my_fruit_counter)
print(my_fruit_counter.items())
# dict_items([('banana', 7), ('fig', 1), ('orange', 10), ('kumquat', 5)])
# a tuple of two items in a pair
print(my_fruit_counter.keys())
# dict_keys(['banana', 'fig', 'orange', 'kumquat'])
# sth like a list, can be converted to a list
print(my_fruit_counter.values())
# dict_values([7, 1, 10, 5])

print(my_fruit_counter["orange"])  # value for the key orange

my_list = [5, 3, 2, 4]
print(sorted(my_list))  # standard ordering for numbers: from smallest to larger
print(sorted(my_list, reverse=True))


# can also use function to replace lambda
def second_element(my_tuple):
    return my_tuple[1]


# wantit ordered by the second element
# key is the particular basis we want to order things
# lambda is a keyword in python
fruits_by_count = sorted(
    my_fruit_counter.items(),
    key=lambda x: x[1],
    # key=second_element, only need to pass the name of the function
    reverse=True
)
print(fruits_by_count)


# TypeError: '<' not supported between instances of 'str' and 'int'
# my_mixed_up_list = [5, "hello", ("mytuple", 3), 1, "a"]
# print(sorted(my_mixed_up_list))


my_food_type = {
    "vegetables": [],
    "meats": [],
    "fruits": []
}
# if we have the same key when declaring, the second one overwrite
# the first one, get reassigned/updated

# add new item
my_food_type["a new type"] = ("tuple1", "tuple2")
my_food_type["vegetables"].append("celery")
my_food_type["vegetables"].append("zucchini")
my_food_type["vegetables"].append("carrot")
print(my_food_type)
for food in my_food_type["vegetables"]:
    print(food)

for food_type in my_food_type.items():
    print(food_type)
# should not assume any particular order in dictionary before
# but now technically it has default ordering as the sequence of adding

# set is for immediate check whether one is in the collection
# unordered but not really random
my_fruit_set = {"banana", "fig", "apple"}

my_empty_set = set()


def check_for_fruit(fruit, fruit_set):
    if fruit in fruit_set:
        print("We have a", fruit)
    else:
        print("We don't have a", fruit)


check_for_fruit("banana", my_fruit_set)
check_for_fruit("berry", my_fruit_set)
my_fruit_set.add("berry")
check_for_fruit("berry", my_fruit_set)
my_fruit_set.add("fig")
check_for_fruit("fig", my_fruit_set)
print(my_fruit_set)
