def program2934():
    p = [tuple(map(int, input().split())) for _ in xrange(3)]
    
    ans = set()
    for i in xrange(3):
        p0 = p[i]
        p1 = p[(i+1)%3]
        p2 = p[(i+2)%3]
        diff = [p0[0] - p1[0], p0[1] - p1[1]]
        new_p = (p2[0]+diff[0], p2[1]+diff[1])
        if new_p not in p:
            ans.add(new_p)
        new_p = (p2[0]-diff[0], p2[1]-diff[1])
        if new_p not in p:
            ans.add(new_p)
    
    print(len(ans))
    for a in ans:
        print(a[0],) a[1]