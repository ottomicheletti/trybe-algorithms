# Inspired by https://www.geeksforgeeks.org/python-program-for-quicksort/
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array


def is_anagram(first_string, second_string):
    first_array = list(first_string.lower())
    second_array = list(second_string.lower())
    first_array_sorted = quick_sort(first_array, 0, len(first_array) - 1)
    second_array_sorted = quick_sort(second_array, 0, len(second_array) - 1)

    if first_string == "" or second_string == "":
        return (
            "".join(first_array_sorted),
            "".join(second_array_sorted),
            False,
        )

    return (
        "".join(first_array_sorted),
        "".join(second_array_sorted),
        first_array_sorted == second_array_sorted,
    )
