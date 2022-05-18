import random

massive = [random.randint(0, 10) for x in range(10)]

def choise_sort(arr: list) -> None:
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

        


print(massive)
choise_sort(massive)
print(massive)

