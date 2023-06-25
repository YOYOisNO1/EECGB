    #coding=utf-8
    
    n,x,y,c=map(int,input().split())
    
    
def f(k):
    	return 1+2*k*(k+1) 
def f2(k):
    	return k*k
    
def f3(k):
    	return k*(k+1)/2
    
def s(n,x,y,c):
    	l,r,u,d=x-c,x+c,y-c,y+c
    	#print("("),l,r,u,d,")"
    	S = f(c)
    	#print("{"),S,
    	if l <= 0: 
    		S-=f2(-l+1)
    	if u <= 0: 
    		S-=f2(-u+1)
    	if r >n: 
    		S-=f2(r-n)
    	#	print(-f2(r-n),)
    	if d >n: 
    		S-=f2(d-n)
    	#	print(-f2(d-n),)
    	if c >= x		+y: 		S+= f3(c - (x+y)+1)
    	if c >= n-x+1	+y: 		S+= f3(c - (n-x+1+y)+1)
    	if c >= x		+n-y+1: 	S+= f3(c - (x+n-y+1)+1)
    	if c >= n-x+1	+n-y+1: 	S+= f3(c - (n-x+1+n-y+1)	+1)
    	#print("}")
    	return S
    
    l,r= 0,2*n
    ans = 2*n
    while l <= r:
    	mid = (l+r)/2
    	#print("!!!"),l,r,mid,s(n,x,y,mid)
    	if s(n,x,y,mid)>=c:
    		ans = mid
    		r = mid-1
    	else:
    		l = mid+1
    print(ans)
    		
    	
    		
    
    	