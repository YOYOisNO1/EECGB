    
    
def dist(x, y):
        return (x ** 2 + y ** 2) ** 0.5
    
    
    x0, y0, n, d = map(int, input().split())
    mvs = []
    for _ in range(n):
        mvs.append(map(int, input().split()))
    
    dp = [[False] * (2 * d + 1) for _ in range(2 * d + 1)]
    for i in range(2 * d, -1, -1):
        for j in range(2 * d, -1, -1):
            x = i - d
            y = j - d
            if dist(x, y) <= d:
                for dx, dy in mvs:
                    x1 = x + dx
                    y1 = y + dy
                    if dist(x1, y1) <= d and not dp[x1 + d][y1 + d]:
                        dp[i][j] = True
    if dp[x0 + d][y0 + d]:
        print('Anton')
    else:
        print('Dasha')