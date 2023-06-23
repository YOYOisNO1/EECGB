def program1674():
    import bisect
    n,m = map(int,input().split())
    a = map(int,input().split())
    A = []
    for i in range(n):
    	ac = a[:i]
    	item = sum(ac) + a[i] - m
    	ans = 0
    	# print ac,item,a[i]
    	while sum(ac) > (m - a[i]) and item>0:
    		ix = bisect.bisect_left(a,item,0,i-1)
    		item = sum(ac) + a[i] - m
    		ac[ix] = 0
    		ans+=1
    		ac.sort()
    	A.append(ans)
    for i in A:
    	print i,