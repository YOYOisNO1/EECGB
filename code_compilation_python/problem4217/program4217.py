def program4217():
    n=int(input())
    i=1%n
    k=2%n
    v=[-1]*n
    v[0]=1
    while not (k==v[i]):
    	v[i]=k
    	i=(i+k)%n
    	k=(k+1)%n
    	if v.count(-1)==0:
    		break
    if v.count(-1)!=0:
    	print 'NO'
    else:
    	print 'YES'