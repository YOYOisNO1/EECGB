def program251():
    [n, m, L, R] = [int(s) for s in input().split()]
    h = R-L
    mod = 998244353
    ret = 0
    if n%2 and m%2:
        ret = (h+1)**(n*m)
    else:
        x = (h+1)**(n*m/2)
        a = x // 2
        b = (x+1) // 2
        ret = a*a+b*b
    
    print(int(ret%mod))