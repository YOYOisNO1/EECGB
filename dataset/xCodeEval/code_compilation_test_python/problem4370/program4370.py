def program4370():
    n,t = map(int, input().split())
    a = map(int, input().split())
    #print n,t,a
    m = min(t,n)
    b = a*m
    c = []
    c += [a[0]]
    for i in b[1:]:
        if i>=c[-1]:
    	c += [i];
        else:
    	j = len(c) - 2
    	while j>=0:
    	    if c[j]<i:
    		break
    	    j-=1
    	c[j+1] = i
        #print c
    l = len(c)
    #print l
    ans = l
    if t>n:
        ans += t-n
    print ans