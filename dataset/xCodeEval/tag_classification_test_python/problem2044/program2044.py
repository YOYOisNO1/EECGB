def program2044():
    import math
    n,k,d = map(int,input().split())
    s = [[0,0] for _ in xrange(n+1)]#0-->=d 1--><d
    s[0][0]=1
    s[0][1]=0
    e = 1000000007
    for i in xrange(1,n+1,1):
    	for j in xrange(1,k+1,1):
    		if i<j:
    			break
    		if j<d:
    			s[i][0]=(s[i][0]+s[i-j][0])%e
    			s[i][1]=(s[i][1]+s[i-j][1])%e
    		else:
    			s[i][1]=(s[i][1]+s[i-j][0])%e
    			s[i][1]=(s[i][1]+s[i-j][1])%e
    print(s[n][1]%e)
    