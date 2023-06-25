    mod = 10**9 + 7
    ways = [[0 for j in range(502)] for i in range(502)]
    
    ways[0][0] = 1
    for i in range(1, 501):
        ways[i][0] = 1
        for j in range(1, 501):
            ways[i][j] = (ways[i - 1][j - 1] + ways[i - 1][j]) % mod
    
    n, k = map(int, input().split())
    if n == 1:
        print(1)
        exit(0)
    
def get(r, c):
        total = (r * n) + (c * n)
        common = r * c
        return pow(k - 1, total - common, mod) * pow(k, (n - r) * (n - c), mod)
    
    res = 0
    
    for r in range(n + 1):
        for c in range(n + 1):
            x = 1
            if (r + c) % 2 == 1:
                x *= -1
    
            res += x * get(r, c) * (ways[n][r] * ways[n][c]) % mod
            res %= mod
    
    print(res)