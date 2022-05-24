def fib_slow(n: int):
    if n < 2:
        return n
    else:
        return fib_slow(n-1) + fib_slow(n-2)


def fib_fast(n: int):
    res = [0, 1]
    for x in range(2,n):
        res.append(res[x-1]+res[x-2])
    return res[-1]

def test():
    assert fib_slow(3) == 2
    for x in range(10):
        print(fib_slow(x), end = " ")
    print()
    print(fib_fast(10))

test()