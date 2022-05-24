def binary_search(arr: list, key):
    arr.sort()
    return left_barrier(arr, key), right_barrier(arr, key)


def left_barrier(arr: list, key):
    left = -1
    right = len(arr)

    while (right - left) > 1:
        middle = (right + left) // 2
        if arr[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_barrier(arr: list, key):
    left = -1
    right = len(arr)
    while (right - left) > 1:
        middle = (right + left) // 2
        if arr[middle] <= key:
            left = middle
        else:
            right = middle
    return right


x = [1, 2, 2, 2, 2, 2, 4, 5, 1]

print(binary_search(x,99))
