def program785():
    n, m = map(int, input().split(' '))
    mod = 10**9+7
    tmp = (1 + m - 1) * (m - 1) / 2
    tmp2 = (1 + n) * n / 2
    ans = (tmp * n % mod + m * tmp * tmp2 % mod) % mod
    print(ans)