from linked_list import LinkedList


def main():
    my_linked_list = LinkedList("ABC")
    my_linked_list.extend('D')
    my_linked_list.extend('E')

    print("Here's the list as a string\n")
    print(my_linked_list)

    print("Here's the list as a repr string\n")
    print(repr(my_linked_list))

    # contains is not yet implemented
    print("List contains B:", my_linked_list.contains('B'))  # True
    print("List contains H:", my_linked_list.contains('H'))  # False


main()
