def program3260():
    
    n = int(input())
    exp = 1
    t = 1
    ans = 1
    while t <= n:
        if n % t == 0:
            ans = t
        exp += 1
        t = (2 ** exp - 1) * (2 ** (exp - 1))
    print(ans)