fruits = ["apple", "banana", "cranberry", "durian",
          "etrog", "fig", "guava", "honeydew"]


print(fruits[1:5])

#list comprehension
#first character for each fruit in fruits
first_letters=[fruit[0] for fruit in fruits]

print(first_letters)

my_string ="Hi there, I'm a string"
print(list(my_string))

words=my_string.split(" ")
print(words)

join_words='__'.join(words)

print(join_words)

my_num_string="123456"

my_num_list = [int(element) for element in my_num_string]

print(my_num_list)


list_of_lists = [
                    ['a', 'b', 'c', 'd'],
                    [1, 2, 3, 4, 5, 6, 7, 8, "hi there!"],
                    ["apple", "banana", "cranberry"]
                ]


print(len(list_of_lists))
print(len(list_of_lists[1]))
print(list_of_lists[1][-1][3])


new_list = []
new_list.append("cheese")
new_list.append("tomato")
new_list.append("egg")
new_list.append("milk")

print(new_list)

new_list.insert(0, "First element")
new_list.insert(2, "Third element")

print(new_list)

numbers = [1, 2, 3, 4, 5]

print(sum(numbers))