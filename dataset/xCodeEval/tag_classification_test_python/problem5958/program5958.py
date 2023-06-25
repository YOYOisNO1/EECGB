def program5958():
    from fractions import gcd
    
    n=int(input())
    temp=input().split()
    p=[int(k)-1 for k in temp]
    
    if len(set(p))<len(p):
    	print("-1")
    else:
    	cl=[]
    	ind=[False for i in range(n)]
    	left=n
    	itr=0
    	while left>0:
    		l=1
    		while ind[itr]:
    			itr+=1
    		ind[itr]=True
    		left-=1
    		i=p[itr]
    		while i!=itr:
    			l+=1
    			ind[i]=True
    			left-=1
    			i=p[i]
    		cl.append(l)
    	for i in range(len(cl)):
    		if cl[i]%2==0:
    			cl[i]=int(cl[i]/2)
    	ans=1
    	for i in range(len(cl)):
    		ans=int(ans*cl[i]/gcd(ans,cl[i]))
    	print(ans)