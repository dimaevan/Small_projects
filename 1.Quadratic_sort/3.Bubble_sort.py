import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import utils  # noqa:E402


def bubble_sort(arr: list) -> None:
    """ Bubble sorting array """
    N = len(arr)
    while N:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        N -= 1


utils.test(bubble_sort)
utils.sort_and_print(bubble_sort)
