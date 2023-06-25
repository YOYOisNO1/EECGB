def program3812():
    n, d = input().split()
    n = int(n)
    d = int(d)
    a = input().split()
    for i in xrange(0, n):
    	a[i] = int(a[i])
    m = int(input())
    a.sort()
    res = 0
    if (m <= n):
    	for i in xrange(0, m):
    		res += a[i]
    else:
    	for i in xrange(0, n):
    		res += a[i]
    	res -= d * (m - n)
    print(res)