def program5465():
    
    n, m, k, x, y = map(int, input().split())
    
    c = [[0 for j in range(m)] for i in range(n)]
    
    s = (m + (n - 2) * m * 2 + m) if n > 1 else m
    
    for i in range(n):
        for j in range(m):
            c[i][j] = k / s
            if i not in {0, n - 1}:
                c[i][j] *= 2
    
    k %= s
    
    for i in range(n) + range(n - 2, 0, -1):
        for j in range(m):
            if k > 0:
                c[i][j] += 1
                k -= 1
            else:
                break
    
    print('%d %d %d') % (max(map(max, c)), min(map(min, c)), c[x - 1][y - 1])