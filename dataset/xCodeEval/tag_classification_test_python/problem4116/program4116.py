def program4116():
    from __future__ import division
    from sys import stdin
    
    n, p, t = map(float, stdin.readline().split())
    n, t = int(n), int(t)
    mem = [[0] * (n + 1) for _ in range(t + 1)]
    
    for i in range(1, t + 1):
        for j in range(1, n + 1):
            mem[i][j] = p * (mem[i - 1][j - 1] + 1) + (1 - p) * mem[i - 1][j]
    
    print(mem[t][n])