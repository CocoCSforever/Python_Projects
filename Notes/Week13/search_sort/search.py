class Search:
    """Implements two search algorithms:
linear search and binary search"""

    @staticmethod
    def linear_search(array, value):
        """Search _list for value using linear search"""
        for i in range(len(array)):
            if (array[i] == value):
                print("Comparing:", array[i], "and", value, "are equal")
                return i
            print("Comparing:", array[i], "and", value, "are not equal")
        return -1

    @staticmethod
    def binary_search(array, value):
        """Search _list for value using binary search"""
        left = 0
        right = len(array) - 1
        while (left <= right):
            mid = int((left+right)/2)
            if (value == array[mid]):
                print("Comparing:", array[mid], "and", value, "are equal")
                # We found the index of value in the array
                return mid
            # Search for value in the upper half
            elif (value > array[mid]):
                print("Comparing:", value, "is greater than", array[mid])
                left = mid + 1
            # Search for value in the lower half
            else:
                print("Comparing:", value, "is less than", array[mid])
                right = mid - 1
        # Value does not occur in the array
        return -1
