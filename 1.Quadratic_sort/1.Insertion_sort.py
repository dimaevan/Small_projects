import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import utils  # noqa:E402


def insertion_sort(arr: list) -> None:
    for x in range(1, len(arr)):
        k = x
        while k > 0 and arr[k] < arr[k-1]:
            arr[k], arr[k-1] = arr[k-1], arr[k]
            k -= 1


def insertion_sort_2(arr: list):
    for i in range(1, len(arr)):
        for k in range(i, 0, -1):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]


utils.test(insertion_sort)
utils.test(insertion_sort_2)
utils.sort_and_print(insertion_sort)
utils.sort_and_print(insertion_sort_2)
