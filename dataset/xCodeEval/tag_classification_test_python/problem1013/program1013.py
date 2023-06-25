def program1013():
    import sys
    read = lambda: sys.stdin.readline().strip()
    readi = lambda: map(int, read().split())
    from itertools import permutations as pt
    
    n = int(read())
    a = list(readi())
    b = list(readi())
    
    operations = [
        (0, 0),
        (0, 2),
        (1, 1),
        (1, 0),
        (2, 2),
        (2, 1)
    ]
    
    maxWin = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    minWin = float('-inf')
    for perm in pt(operations, 6):
        A = a.copy()
        B = b.copy()
        temp = 0
        for i, j in perm:
            diff = min(A[i], B[j])
            A[i] -= diff
            B[j] -= diff
            temp += diff
        minWin = max(minWin, temp)
    minWin = n - minWin
    print(minWin, maxWin)