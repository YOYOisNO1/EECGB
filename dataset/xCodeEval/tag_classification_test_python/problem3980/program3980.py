def program3980():
    w, m = map(int, input().split())
    
    ans = True
    for i in xrange(101):
        k = m % w
        if k == 1:
            m -= 1
        elif k == w-1:
            m += 1
        elif k == 0:
            pass
        else:
            ans = False
        m /= w
    print("YES") if ans else "NO" 