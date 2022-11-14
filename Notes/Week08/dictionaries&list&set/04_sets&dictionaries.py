print("----------Set&Dictionary----------")
print("------------Dictionary------------")
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
print("my_food_type after adding new items:")
print(my_food_type)

print("---------------------")
print("Items in my_food_type[\"vegetables\"]:")
for food in my_food_type["vegetables"]:
    print(food)

print("---------------------")
print("Items in my_food_type:")
for food_type in my_food_type.items():
    print(food_type)
# should not assume any particular order in dictionary before
# but now technically it has default ordering as the sequence of adding
print("----------------------------------")


# set is for immediate check whether one is in the collection
# unordered but not really random
print("--------------Set-----------------")
my_fruit_set = {"banana", "fig", "apple"}
my_empty_set = set()


def check_for_fruit(fruit, fruit_set):
    if fruit in fruit_set:
        print("We have a", fruit)
    else:
        print("We don't have a", fruit)


print("Items in set:")
print(my_fruit_set)
print("---------------------")
print("Check for fruit:")
check_for_fruit("banana", my_fruit_set)
check_for_fruit("berry", my_fruit_set)
print("Added berry and fig to set:")
my_fruit_set.add("berry")
check_for_fruit("berry", my_fruit_set)
my_fruit_set.add("fig")
check_for_fruit("fig", my_fruit_set)
print("---------------------")
print("Items in set:")
print(my_fruit_set)
print("----------------------------------")
