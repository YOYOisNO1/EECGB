def program5394():
    import sys
    input = sys.stdin.readline
    
    
    mod = 10 ** 9 + 7
    for _ in range(int(input())):
        n, k = map(int, input().split())
        ans = 0
        x = pow(2, n - 1, mod)
        if n % 2:
            ans = pow(x + 1, k, mod)
            print(ans)
        else:
            cur = 1
            for i in range(k):
                r = k - i - 1
                ans += pow(pow(2, r, mod), n, mod) * cur % mod
                ans %= mod
                cur = cur * (x - 1) % mod
            print((ans + cur) % mod)