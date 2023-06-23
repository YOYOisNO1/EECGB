def program253():
    from sys import exit
    
    MOD = 998244353
    
    n, m, l, r = map(int, input().split())
    if l == r:
        print(1)
        exit(0)
    if n * m % 2 == 1:
        ans = pow(r - l + 1, n * m, MOD)
        print(ans)
        exit(0)
    
    a = (r - l + 1) // 2
    b = a
    if (r - l + 1) % 2 == 1:
        b += 1
    
    x = n * m
    
    ans = pow(2, x - 1, MOD)
    if 1 or a == b:
        ans *= pow(b, x, MOD)
        ans %= MOD
        # else:
    if m != 2 and a != b:
        1/0
    
    print(ans)