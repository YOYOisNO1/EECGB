def program3764():
    l, r = map(int, input().split(' ').strip())
    
    ans = 0
    
    int cnt = 31
    for i in xrange(cnt):
        for j in xrange(cnt):
            cur = 2 ** i * 3 ** j
            if l <= cur and cur <= r:
                ans += 1
    
    print ans