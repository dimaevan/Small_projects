"""
Eat moar memory
"""


def merge_sort(arr_: list) -> list:
    if len(arr_) <= 1:
        return arr_

    middle = len(arr_) // 2
    left = arr_[:middle]
    right = arr_[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(first: list, second: list) -> list:
    i = n = 0
    res = list()
    while i < len(first) and n < len(second):
        if first[i] <= second[n]:
            res.append(first[i])
            i += 1
        else:
            res.append(second[n])
            n += 1
    if i < len(first):
        res.extend(first[i:])
    elif n < len(second):
        res.extend(second[n:])
    return res


def test() -> None:
    assert merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5]
    print(merge([1, 2, 3], [3, 4, 5]))

    assert merge_sort([2, 3, 4, 5, 1]) == [1, 2, 3, 4, 5]
    print(merge_sort([2, 3, 4, 5, 1]))


test()
