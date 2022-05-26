import pprint

def finder(x: int, y:int, x1: int, y1:int):
    res = [[1 if j == 0 or i == 0 else 0 for j in range(x) ] for i in range(y)]
    for y2 in range(1,y):
        for x2 in range(1,x):
            res[y2][x2] = res[y2-1][x2] + res[y2][x2-1]


    # pprint.pprint(res)
    print(res[y1][x1])

def test():
    finder(10,10,3,4)

test()