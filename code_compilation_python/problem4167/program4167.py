def program4167():
    s = input().split()
    a, b, c, mx, up = [], [], [], -1, 0
    for i in xrange(len(s[0])):
        a.append(int(s[0][i]))
        mx = max(mx,a[i])
    for i in xrange(len(s[1])):
        b.append(int(s[1][i]))
        mx = max(mx,b[i])
    p = mx + 1
    for i in xrange(max(len(s[1]),len(s[0]))):
        if a[i] + b[i] + up >= p:    up = 1
        else: up = 0
    print max(len(s[1]),len(s[0])) + up
    
    