from typing import Tuple


def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


def is_anagram(first_string: str, second_string: str) -> Tuple[str, str, bool]:
    first_sorted = ''.join(quicksort(list(first_string.lower())))
    second_sorted = ''.join(quicksort(list(second_string.lower())))

    if not first_string or not second_string:
        return first_sorted, second_sorted, False

    if len(first_string) != len(second_string):
        return first_sorted, second_sorted, False

    return first_sorted, second_sorted, first_sorted == second_sorted
