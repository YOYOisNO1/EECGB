def program3753():
    a=[1,1,3,19,225,3441,79259,2424195]
    n=map(int,input().split())[0]
    if n%2 == 0: print 0
    else: 
    	r=reduce( lambda x,y:x*y, [i for i in xrange(1,n+1)])*n*a[n/2]
    	print r % (10**9+7)