def solve(i,n,s,a):
    	if(i==n-1):
    		if(s=="QAQ"):
    			return 1
    		return 0
    	if(s=="QAQ"):
    		return 1
    	return solve(i+1,n,s,a)+solve(i+1,n,s+a[i],a)
    
    a=input()
    n=len(a)
    z=''
    print(solve(0,n,z,a))