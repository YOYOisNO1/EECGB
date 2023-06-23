def solve(i, z, k):
        if i >= n:
            return 0
        if dp[i][z][k] != -1:
            return dp[i][z][k]
        o = solve(i+1, z, k)
        c = s[i] != t[0]
        if k >= c:
            o = max(o, solve(i+1, z+1, k-c))
        c = s[i] != t[1]
        if k >= c:
            o = max(o, solve(i+1, z+(t[0] == t[1]), k-c) + z)
        dp[i][z][k] = o
        return o
    
    n, k = map(int, input().split())
    s = input()
    t = input()
    
    dp = [[[-1] * (n+1) for _ in [0] * n for _ in [0]*n]
    
    print(solve(0, 0, k))