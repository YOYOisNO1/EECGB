def program4049():
    n = int(input())
    a = []
    b = []
    for _ in xrange(n):
    	c = map(int,input().split())
    	a.append(c[0])
    	b.append(c[1])
    a=sorted(a)
    b=sorted(b)
    d = (a[-1]-a[0])*(b[-1]-b[0])
    print(d) if d>0 else -1
    