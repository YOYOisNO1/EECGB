def program4361():
    x, y, l, r = map(int, input().split())
    yrs = set()
    yrs.add(l-1)
    yrs.add(r+1)
    for a in range(0, 70):
        for b in range(0, 70):
            n = x**a + y**b
            if (n>=l and n<=r):
                yrs.add(n)
    
    yrs = sorted(yrs)
    mx = 0
    for i in range(1, len(yrs)):
        mx = max(mx, yrs[i]-yrs[i-1]-1)
    print(mx)