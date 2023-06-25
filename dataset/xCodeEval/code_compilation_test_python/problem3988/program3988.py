def program3988():
    n,a,b,c = map(int,input().split())
    r = 0
    for i in xrange(a+1):
    	if i*0.5>n:
    		break
    	for j in xrange(b+1):
    		if i*0.5+j<=n and (n-i*0.5-j)%2==0 and (n-i*0.5-j)/2<=c:
    			r+=1
    		if i*0.5+j>n:
    			break
    print r