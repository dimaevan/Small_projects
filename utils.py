import random


def make_massive(length: int = 10) -> None:
    return [random.randint(0, 10) for x in range(length)]


def sort_and_print(sort):
    x = make_massive()
    print(f"Input {x}")
    sort(x)
    print(f"Output {x}")
    print()


def test(sort_func):
    a = [5, 4, 3, 1, 2]
    b = [1, 2, 3, 4, 5]
    sort_func(a)
    assert a == b, "Test failed"
    print("Test passed!")
