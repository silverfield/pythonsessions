__author__ = 'Fero'

# ---------------------------------------------------------------
# Constants
# ---------------------------------------------------------------

MAX_LENGTH_FOR_QUADRATIC = 10000

# ---------------------------------------------------------------
# Interface
# ---------------------------------------------------------------


def binary_search(numbers, number):
    """Binary search

    Locates the number in the list of sorted numbers. Looks at the middle element, and proceeds recursively to the left
    or to the right, depending on whether the number was smaller or bigger, respectively

    Returns the position of the found number, or the position at which the number should be inserted to preserve order

    Time complexity T(n) = O(log n)
    Space complexity S(n) = O(log n)
    """
    def bin_search(a, b):
        """a and b are inclusive indices"""
        if a == b:
            return a if number <= numbers[a] else a + 1
        middle = (a + b) // 2
        if number <= numbers[middle]:
            return bin_search(a, middle)
        else:
            return bin_search(middle + 1, b)

    return bin_search(0, len(numbers) - 1)


def selection_sort(nums):
    """Selection sort implementation

    In-place sort that builds the final sorted sequence from left to right, by looking for the minimum element in the
    unsorted-yet part
    """
    if len(nums) > MAX_LENGTH_FOR_QUADRATIC:
        raise Exception("sequence too long for the algorithm")

    n = len(nums)
    for i in range(n):
        # find the minimum from i-th position to the right
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        # swap the found minimum to the i-th position
        tmp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = tmp


def input_by_user():
    """Loads numbers from the standard input (one number per line) until an empty line is encountered"""
    print("Please provide numbers (end with an empty line): ")
    inp = input()
    numbers = []
    while inp != "":
        numbers.append(int(inp))
        inp = input()

    return numbers


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def main():
    numbers = [10, 1, 0, -1, 5, 47, 7, 100, 8]
    #numbers = input_by_user()
    n = len(numbers)

    selection_sort(numbers)
    print("Sorted list is:")
    for i in numbers:
        print(i)

    print()
    print("Position of 47 is/would be: " + str(binary_search(numbers, 47)))
    for i in range(0, 102):
        print("Position of " + str(i) + " would be: " + str(binary_search(numbers, i)))

if __name__ == "__main__":
    main()