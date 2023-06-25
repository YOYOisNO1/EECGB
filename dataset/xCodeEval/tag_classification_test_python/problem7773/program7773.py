    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    x, y, n, d = map(int, input().split())
    vector = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * (d * 2 + 1) for _ in range(d * 2 + 1)]
    
    for i in range(d * 2 + 1):
        for j in range(d * 2 + 1):
            if (i - d) ** 2 + (j - d) ** 2 > d**2:
                dp[i][j] = 1
    
    
def solve(x, y):
        if dp[x][y] != -1:
            return dp[x][y]
    
        for dx, dy in vector:
            if 0 <= x + dx <= 2 * d and 0 <= y + dy <= 2 * d and solve(x + dx, y + dy) == 0:
                dp[x][y] = 1
                return 1
    
        dp[x][y] = 0
        return 0
    
    
    if solve(x + d, y + d):
        print('Anton')
    else:
        print('Dasha')