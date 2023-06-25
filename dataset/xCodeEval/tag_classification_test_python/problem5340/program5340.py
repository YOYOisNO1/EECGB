def solve(n, mod):
        a = [0]*(n-1) + [1]
        b = [0]*(n-1) + [1]
        for i in range(n-2, -1, -1):
            a[i], m = b[i+1], 2
            s = (i+1) * m - 1
            while s < n:
                e = min((i+2) * m - 2, n - 1)
                a[i] = (a[i] + b[s] - b[e] + a[e]) % mod
                m += 1
                s = (i+1) * m - 1
            b[i] = (b[i+1] + a[i]) % mod
        return a[0]
    
    n, m = map(int, input().split())
    print(solve(n, m))