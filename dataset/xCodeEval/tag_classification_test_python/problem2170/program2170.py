def program2170():
    n = input()
    
    a = map(int, input().split())
    
    b = map(int, input().split())
    
    da = {}
    db = {}
    for i in xrange(1,6):
        da[i] = a.count(i)
        db[i] = b.count(i)
    
    
    c = 0
    fail = False
    for i in xrange(1,6):
        if da[i]==db[i]:
            pass
        else:
            c+=abs(da[i]-db[i])
            if (da[i]+db[i])%2!=0:
                fail = True
    if c%4!=0 or fail:
        print(-1)
    else:
        print(c/4)