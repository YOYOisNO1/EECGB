def program1086():
    from itertools import *
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    
    
    
    res_max = 0
    for i in range(len(A)):
        res_max += min(A[i], B[(i + 1) % len(A)])
    
    possible_pairs = [(0, 0), (0, 2), (1, 1), (1, 0), (2, 2), (2, 1)]
    res_min = float('inf')
    for pairs in permutations(possible_pairs):
        tempA, tempB = A[:], B[:]
        for a, b in pairs:
            temp = min(tempA[a], tempB[b])
            tempA[a] -= temp
            tempB[b] -= temp
        res_min = min(res_min, sum(tempA))
    
    print(res_min, res_max)