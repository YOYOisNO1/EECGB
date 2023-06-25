def program214():
    MOD = 1000000007
    a = map(int, input().split())
    n = int(input()) - 1
    while len(a) < 6:
        a.append(a[-1] - a[-2])
    print((a[n) % 6] + MOD) % MOD