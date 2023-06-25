def program3408():
    n = int(input())
    a = map(int, input().split())
    d = [a[i+1] - a[i] for i in range(n-1)]
    m = []
    for i in xrange(n-2):
        c = list(d)
        c[i:i+2] = [d[i]+d[i+1]]
        m.append(max(c))
    print(min(m))