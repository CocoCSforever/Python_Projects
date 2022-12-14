class Sort:
    """Implements two sorting algorithms:
selection sort and bubble sort"""

    @staticmethod
    def selection_sort(array):
        """Sort a list of numbers using selection sort"""
        # Each iteration of this outer for-loop puts one element into its
        # proper place. After n iterations, every element is in its proper
        # place, i.e., the array is sorted
        for i in range(len(array)):
            # Find the index of the smallest element in the
            # remaining unsorted portion of the array
            min_index = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            # Swap the ith element and the minimum element
            array[i], array[min_index] = array[min_index], array[i]

            print(i, ": ", array)
        return array

    @staticmethod
    def bubble_sort(array):
        """Sort a list of numbers using bubble sort"""
        # Each iteration of this outer for-loop puts *at least* one element
        # into its proper place(the current largest one to the last).
        # Thus, at most n iterations must be executed to sort the array.
        # I.e., it's possible for the array to be sorted
        # in fewer than n iterations
        for _ in range(len(array)):
            swapped = False
            for j in range(1, len(array)):
                if array[j-1] > array[j]:
                    array[j-1], array[j] = array[j], array[j-1]
                    swapped = True
            print(_, ": ", array)

            # If we went through the whole array and never swapped anything
            # then the array must be sorted and we can exit early
            if not swapped:
                return
