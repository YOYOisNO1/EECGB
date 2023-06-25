    #!/usr/bin/env python3
    from math import *
    
    
def ri():
        return map(int, input().split())
    
    n, m, k, sr, sc = ri()
    
    if n == 1:
        t = k//m
    else:
        t = k//(n*m+(n-2)*m)
    F = [[0]*(m+1) for i in range(n+1)]
    
    for rr in range (1, n+1):
        for cc in range(1, m+1):
            if n == 1:
                F[rr][cc] = t
                continue
            if rr == 1 or rr == n:
                F[rr][cc] = t
            else:
                F[rr][cc] = t*2
    
    if n == 1:
        count = k%m
    else:
        count = k%(n*m+(n-2)*m)
    for rr in range(1, n+1):
        for cc in range(1, m+1):
            if count == 0:
                break
            F[rr][cc] += 1
            count -= 1
        if count == 0:
            break
    if count:
        for rr in range(n-1, 1, -1):
            for cc in range(1, m+1):
                if count == 0:
                    break
                F[rr][cc] += 1
                count -= 1
            if count == 0:
                break
    if n == 1:
        print(F[1][1], F[n][m], F[sr][sc])
    else:
        print(max(F[1][1], F[2][1], F[n-1][1]), F[n][m], F[sr][sc])
    