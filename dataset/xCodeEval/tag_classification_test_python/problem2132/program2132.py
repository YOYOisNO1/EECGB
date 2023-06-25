def program2132():
    # http://codeforces.com/problemset/problem/431/C
    
    [n, k, d] = [int(i) for i in input().split(' ')]
    
    dpAll = [[0 for i in range(n + 1)] for i in range(n + 1)]
    dpNone = [[0 for i in range(n + 1)] for i in range(n + 1)]
    
    for i in range(1, k + 1 if k + 1 < n + 1 else n + 1):
        dpAll[1][i] = 1
    for i in range(1, d if d < n + 1 else n + 1):
        dpNone[1][i] = 1
    
    for i in range(2, n + 1):
        for s in range(0, n + 1):
            dpAll[i][s] = sum([dpAll[i - 1][s - j] if s - j >= 0 else 0 for j in range(1, k + 1)]) if k * i >= s and i <= s else 0
    
    for i in range(2, n + 1):
        for s in range(0, n + 1):
            dpNone[i][s] = sum([dpNone[i - 1][s - j] if s - j >= 0 else 0 for j in range(1, d)]) if (d - 1) * i >= s and i <= s else 0
    
    print((sum([dpAll[i][n]) for i in range(1, n + 1)]) - sum([dpNone[i][n] for i in range(1, n + 1)])) % 1000000007