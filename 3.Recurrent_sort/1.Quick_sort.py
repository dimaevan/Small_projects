def quick_sort(list_: list) -> None:
    """
        Алгоритм сортировки Тони Хоара.
        Рекурнтно делить массив относительно браьерного элемента.
    """
    n = len(list_)
    if n < 1:
        return list_

    middle = n // 2
    left_list = list()
    right_list = list()
    middle_list = list()

    for x in list_:
        if x < list_[middle]:
            left_list.append(x)
        elif x > list_[middle]:
            right_list.append(x)
        else:
            middle_list.append(x)

    return (quick_sort(left_list) + middle_list + quick_sort(right_list))


print(quick_sort([7, 2, 5, 4]))
