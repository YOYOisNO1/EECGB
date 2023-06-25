    from fractions import gcd
    n=int(input())
    a=map(int,input().split())
    for i in xrange(n):
    	a[i]-=1
    test=[0]*n
    for i in a:
    	test[i]+=1
    mk=[-1]
def go(p):
    	if test[p]==0:
    		test[p]=1
    		return go(a[p])+1
    	else:
    		mk[0]=p
    		
    		return 0
    if 0 in test:
    	print(-1)
    else:
    	test=[0]*n
    	ans=1
    	flag=True
    	for i in xrange(n):
    		if test[i]==0:
    			l=go(i)
    			if mk[0]!=i:
    				flag=False
    				break
    			if l&1==0:
    				l>>=1
    			ans=ans*l/gcd(ans,l)
    	if not flag:
    		print(-1)
    	else:
    		print(ans)