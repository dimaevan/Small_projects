import pprint

def lcs(A, B):
    F = [[0]*(len(B)+1) for x in range(len(A)+1)]
    for i in range(1,len(A)+1):
        for j in range(len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    pprint.pprint(F) 


lcs("abcdef", "cdcdej")