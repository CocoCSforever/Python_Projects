print("------------Dictionary-------------")
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
print("---------------------")
print("Items in Dictionary:")
for i in my_fruit_counter.items():
    print(i)

print("---------------------")
print("my_fruit_counter:")
print(my_fruit_counter)

print("---------------------")
print("my_fruit_counter.items():")
print(my_fruit_counter.items())
# dict_items([('banana', 7), ('fig', 1), ('orange', 10), ('kumquat', 5)])
# a tuple of two items in a pair
print("---------------------")
print("my_fruit_counter.keys():")
print(my_fruit_counter.keys())
# dict_keys(['banana', 'fig', 'orange', 'kumquat'])
# sth like a list, can be converted to a list
print("---------------------")
print("my_fruit_counter.values():")
print(my_fruit_counter.values())
# dict_values([7, 1, 10, 5])
print("---------------------")
print("my_fruit_counter[\"orange\"]:")
print(my_fruit_counter["orange"])  # value for the key orange
print("----------------------------------\n")
