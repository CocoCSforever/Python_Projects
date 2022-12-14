from search import Search
from sort import Sort


def main():
    #####################
    #  Search examples  #
    #####################

    # Searching unsorted (binary won't work)
    demo_search([50, 20, 14, 5, 2, -10, -25, -30], -10, "linear")
    demo_search([50, 20, 14, 5, 2, -10, -25, -30], 50, "linear")
    demo_search([50, 20, 14, 5, 2, -10, -25, -30], 100, "linear")

    # Binary search is not *always* faster than linear!
    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], -50, "linear")
    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], -50, "binary")

    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], -20, "linear")
    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], -20, "binary")

    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], 120, "linear")
    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], 120, "binary")

    # # # Worst case, we fail to find
    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], 100, "linear")
    demo_search([-50, -20, 0, 5, 14, 69, 120, 121], 100, "binary")

    ###################
    #  Sort examples  #
    ###################

    # Totally unsorted (strictly reverse order)
    demo_sort([50, 20, 14, 5, 2, -10, -25, -30], "selection")
    demo_sort([50, 20, 14, 5, 2, -10, -25, -30], "bubble")

    # # Partially sorted
    demo_sort([-50, 2, 14, 20, 40, -30, -25, -10], "selection")
    demo_sort([-50, 2, 14, 20, 40, -30, -25, -10], "bubble")

    # # Already sorted
    demo_sort([-82, -28, 3, 21, 25, 67, 81], "selection")
    demo_sort([-82, -28, 3, 21, 25, 67, 81], "bubble")


def demo_search(array, value, search):
    """Run the chosen search algorithm"""
    print("=======", search, "search")
    print(array)
    print("Searching for", value)
    if (search == "linear"):
        found = Search.linear_search(array, value)
    elif (search == "binary"):
        found = Search.binary_search(array, value)
    else:
        print("Invalid argument")

    if found >= 0:
        print("Found", value, "at index:", found)
    else:
        print("Failed to find", value)

    print("\n")


def demo_sort(array, sort):
    """Run the chosen sorting algorithm"""
    print("=======", sort, "sort")
    print("Before sorting:")
    print(array)
    if (sort == "selection"):
        Sort.selection_sort(array)
    elif (sort == "bubble"):
        Sort.bubble_sort(array)
    else:
        print("Invalid argument")

    print("After sorting:")
    print(array)

    print("\n")


main()
