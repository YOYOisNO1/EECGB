def program2573():
    n = int(input()) + 1
    mod = 10 ** 9 + 7
    prev = 0
    ans = 1
    for i in range(n-1):
        ans *= 3
        ans %= mod
        prev = (ans - prev)%mod
    print((ans - prev)%mod)