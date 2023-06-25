    from sys import stdin,stdout
    
    
    
    
def find(a):
    	if par[a]==a:
    		return a
    	else:
    		par[a]=find(par[a])
    		return par[a]
def union(a,b):
    	a,b=find(a),find(b)
    	if a!=b:
    		if rank[a]>rank[b]:
    			par[b]=a
    		elif rank[b]>rank[a]:
    			par[a]=b
    		else:
    			par[a]=b
    			rank[b]+=1
    
    n,m,k=stdin.readline().strip().split(' ')
    n,m,k=int(n),int(m),int(k)
    
    par=[i for i in range(n)]
    rank=[0 for i in range(n)]
    
    for i in range(n-k+1):
    	l=i;u=i+k-1
    	while l<u:
    		#print(l,u)
    		union(l,u)
    		l+=1;u-=1
    
    for i in range(n):
    	find(i)
    us=len(set(par))
    #print(par)
    print(pow(m,us,1000000007))