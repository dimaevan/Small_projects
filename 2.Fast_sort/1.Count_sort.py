import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import utils  # noqa:E402


def max_in_array(arr: list) -> int:
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


def count_sort(arr: list) -> None:
    array = [0] * (max_in_array(arr) + 1)
    print(array)
    for i in range(len(arr)):
        array[array[i]-1] += 1
    print(array)


# utils.test(count_sort)
# utils.sort_and_print(count_sort)

count_sort([1, 2, 1, 2])
