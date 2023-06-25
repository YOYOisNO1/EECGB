def inprod(a, b, c):
        v1 = [b[i] - a[i] for i in range(5)]
        v2 = [c[i] - a[i] for i in range(5)]
        return sum([v1[i] * v2[i] for i in range(5)]
    
    n = int(input())
    points = []
    for _ in range(n):
        a, b, c, d, e = map(int, input().split(' '))
        points.append([a, b, c, d, e])
    if n == 1:
        print 1
        print 1
    elif n == 2:
        print 2
        print 1
        print 2
    elif n > 10:
        print 0
    else:
        for n1 in range(n):
            success = True
            for n2 in range(n):
                for n3 in range(n):
                    if n1 == n2 or n2 == n3 or n1 == n3:
                        continue
                    p1 = points[n1]
                    p2 = points[n2]
                    p3 = points[n3]
                    if inprod(p1, p2, p3) > 0:
                        success = False
                        break
                if not success:
                    break
            if success:
                print 1
                print n1 + 1
                break
        if not success:
            print 0