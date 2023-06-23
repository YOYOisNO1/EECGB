def program254():
    q = 998244353   
    n, m, l, r = map(int, input().split())
    if n * m % 2 == 1:
        print(pow(r - l + 1, n * m, q))
    elif (r - l + 1) % 2 == 0:
        print(pow(r - l + 1, n * m, q) *
              (q + 1) // 2 % MOD)
    else:
        print((pow(r - l + 1, n * m, q) + 1) *
              (q + 1) // 2 % q)