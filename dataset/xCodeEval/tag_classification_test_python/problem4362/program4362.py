def program4362():
    x, y, l, r = map(int, input().split())
    years = []
    
    for a in xrange(70):
        xa = pow(x, a)
        if xa > r:
            break
        for b in xrange(70):
            yb = pow(y, b)
            if xa + yb > r:
                break
            if xa + yb >= l:
                years.append(xa + yb)
    
    ans = 0
    years.append(l-1)
    years.append(r+1)
    years.sort()
    for i in xrange(len(years)-1):
        ans = max(ans, years[i+1] - years[i] - 1)
    print(ans)