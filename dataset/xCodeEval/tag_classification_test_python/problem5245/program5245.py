def program5245():
    
    
    from itertools import *
    
    n,k=map(int,input().split())
    a=[]
    
    for i in range(n):
    	a.append([i for i in input()])
    
    l=[]
    
    for i in range(k): l.append(i)
    
    perm=permutations(l)
    
    ans=10**9
    
    for now in perm:
    	curr=list(now)
    
    	mx=0
    	mn=10**9
    
    	for i in a:
    		d=""
    		for j in range(k):
    			d+=i[curr[j]]
    
    		mx=max(mx,int(d))
    		mn=min(mn,int(d))
    	ans=min(ans,mx-mn)
    
    print(ans)
    