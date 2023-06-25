    n = int(input().strip())
    
    a = map(int,input().strip().split(' '))
    for i in range(n):
    	a[i]-=1
    
    vis = [0 for _ in range(n)]
    
def gcd(a, b):
        while b:      
            a, b = b, a % b
        return a
    
def lcm(a, b):
        return a * b // gcd(a, b)
    
def lcmm(args):  
        return reduce(lcm, args)
    
def visit(v,l,s):
    	# print(v,l,s)
    	vis[v]=1
    	if(a[v]==v):
    		if(l==0): return 1
    		return -1
    	if(vis[a[v]]==1):
    		if(a[v]==s):
    			if((l+1)%2==0): return (l+1)/2
    			else: return l+1
    		else:
    			return -1
    	return visit(a[v],l+1,s)
    
    s = []
    
    for i in range(n):
    	vis = [0 for _ in range(n)]
     	r = visit(i,0,i)
     	# print(r,"**")
     	if(r==-1):
     		print(-1)
     		exit(0)
     	else:
     		s.append(r)
    
    print(lcmm(s))