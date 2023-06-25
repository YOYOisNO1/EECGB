    #codeforces 86a: reflection: math
    l,r=map(int,input().split())
    
def digits(x):
    	d=0
    	while (x):
    		d+=1
    		x//=10
    	return d
    
def f(n):
    	return n*(10**digits(n)-1-n)
    	
def maxInDigits(l,r):
    	#print("dealwith",l,r)
    	mid=10**digits(l)//2
    	if (r<=mid): return f(r)
    	if (l>=mid): return f(l)
    	return f(mid)
    
    if (digits(l)==digits(r)): print(maxInDigits(l,r))
    else:
    	ans=max(maxInDigits(l,10**digits(l)-1),maxInDigits(10**(digits(r)-1),r))
    	if (digits(r)-1>digits(l)):
    		ans=max(ans,maxInDigits(10**(digits(r)-2),10**(digits(r)-1)-1))
    	print(ans)
    
    	