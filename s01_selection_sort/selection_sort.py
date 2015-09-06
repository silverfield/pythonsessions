__author__ = 'Fero'


def selection_sort(numbers):
    """Selection sort implementation

    In-place sort that builds the final sorted sequence from left to right, by looking for the minimum element in the
    unsorted-yet part
    """
    n = len(numbers)
    for i in range(n):
        # find the minimum from i-th position to the right
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        # swap the found minimum with the item at i-th position
        tmp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = tmp

# define a list
l = [45, 32, 6, 7, 9, 100, -1]
selection_sort(l)
print("Sorted list is: ")
for i in l:
    print(i)


