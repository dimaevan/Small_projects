def generate_permutations(N:int, M:int=-1, prefix=None):
    M = M if M != -1 else N
    prefix = prefix or []
    if M == 0:
        print(*prefix, end = ', ', sep='')
        return
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(N, M-1,prefix)
        prefix.pop()

generate_permutations(9,3)



