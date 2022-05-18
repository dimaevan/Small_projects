import random

massive = [random.randint(0, 10) for x in range(10)]

def insertion(arr: list):
    for i in range(1,len(arr)):
        for k in range(i, 0, -1):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]

print(massive)
insertion(massive)
print(massive)