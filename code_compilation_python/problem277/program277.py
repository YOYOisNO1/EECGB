def program277():
    n = int(input())
    x = map(int, input().split())
    l = a[:n]
    r = a[n:]
    l.sort()
    r.sort()
    
    if l[0] > r[0]:
        left, right = right, left
    
    for i in xrange(n):
        if not l[i] < r[i]:
            break
    else:
        print 'YES'
        exit()
    
    print 'NO' 
    