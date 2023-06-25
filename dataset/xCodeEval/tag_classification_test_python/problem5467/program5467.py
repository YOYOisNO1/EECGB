    import sys
    from array import array  # noqa: F401
    from math import factorial
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    n, h = map(int, input().split())
    
    catalan = [factorial(2 * i) // factorial(i + 1) // factorial(i) for i in range(36)]
    dp = [[-1] * 100 for _ in range(100)]
    dp[0][0] = 1
    
    
def solve(x, h):
        if h <= 1:
            return catalan[x]
        if dp[x][h] != -1:
            return dp[x][h]
    
        res = 0
        for l, r in zip(range(x), range(x - 1, -1, -1)):
            if l >= h - 1:
                res += solve(l, h - 1) * catalan[r]
            if r >= h - 1:
                res += catalan[l] * solve(r, h - 1)
            if l >= h - 1 and r >= h - 1:
                res -= solve(l, h - 1) * solve(r, h - 1)
    
        dp[x][h] = res
        return res
    
    
    print(solve(n, h))