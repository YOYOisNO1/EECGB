def program2339():
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    ans = 0
    for i in xrange(0,k):
        tmp = [0,0,0]
        for y in xrange(0,n/k)
            tmp[data[x*y]] += 1
        ans += min(tmp[1], tmp[2])
    print ans