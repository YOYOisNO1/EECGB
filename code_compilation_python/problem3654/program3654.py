def program3654():
    n, m = map(int, input().split())
    a = [input() for i in xrange(n)][::-1]
    r = 0.5
    
    if a[0] == 'halfplus':
        r = 1
    
    for i, v in enumerate(a[1:]):
        if v == 'halfplus':
            r = r * 2 + 0.5
        else:
            r = r * 2
    
    ans = 0
    for i, v in enumerate(a):
        if v == 'halfplus':
    
        else:
            ans *= 1