def program3706():
    n,m = map(int,input().split())
    p = map(int,input().split())
    s = [map(int,input().split()) for x in xrange(m)]
    y = sorted([x for x in enumerate(p)],key = lambda i:i[1])
    print(' ').join([str(x[2]) for x in sorted([list(y[x]) + [x%2] for x in xrange(n)])])