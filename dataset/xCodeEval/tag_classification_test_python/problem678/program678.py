def program678():
    n, m = map(int, input().split())
    if n == 0:
        if m == 0: print(0,) 0
        else: print('Impossible')
        exit()
    if m == 0: print(n,) n
    else: print(max(n,) m), m+n-1