def quick_sort(list_: list) -> None:
    """
        Алгоритм сортировки Тони Хоара.
        Рекурнтно делить массив относительно браьерного элемента.
    """
    n = len(list_)
    if n < 2:
        return list_

    middle = n // 2
    left_list = list_[:middle-1]
    right_list = list_[middle:]

    print(*left_list,middle, *right_list)

print(quick_sort([7,2,5,4]))