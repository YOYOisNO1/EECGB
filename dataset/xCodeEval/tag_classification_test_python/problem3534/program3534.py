def pos(j):
        k = (j / 50) % 475
        a = []
        for i in xrange(25):
            k = (k * 96 + 42) % 475
            a.append(k + 26)
        return a
    
    p, x, y = map(int, input().split())
    ans = 0
    find = 0
    while (True):
        j = x
        while (j >= y):
            #print(pos(j),) p
            if p in pos(j):
                find = 1
                break;
            j -= 50
        if find:
            break
        x += 100
        ans += 1
        #print(x)
    print(ans)
        