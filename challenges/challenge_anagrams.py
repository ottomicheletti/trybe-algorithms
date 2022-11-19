def bubble_sort(arr):
    array = arr
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return array


def is_anagram(first_string, second_string):
    first_array = list(first_string.lower())
    second_array = list(second_string.lower())
    first_array_sorted = bubble_sort(first_array)
    second_array_sorted = bubble_sort(second_array)

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
