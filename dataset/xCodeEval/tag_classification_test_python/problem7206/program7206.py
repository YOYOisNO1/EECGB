    #!/usr/bin/python
    
    import sys
    import math
    import string
    
    #define long long long
    M = 1000000007 
    F = dict()
    
def f(n):
    	if n in F: 
    		return F[n];
    	k = n/2;
    	if n%2==0:
    		F[n] = (f(k)*f(k) + f(k-1)*f(k-1)) % M
    		return F[n]
    	else:
    		F[n] = (f(k)*f(k+1) + f(k-1)*f(k)) % M
    		return F[n]
    
def total(n):
    	ans = 2;
    	res = 1;
    	for i in range(64):
    		if ((1 << i) & n) != 0:
    			res = (res * ans) % M
    		ans = (ans * ans) % M
    	return res
    
def solve(n,k,l,m): 
    	ans = 1
    	no = f(n+1)
    	yes = total(n) - no
    	#//cout << yes << " " << no << endl;
    	for i in range(l):
    		if ((1L << i) & k):
    			ans = (ans * yes) % m
    		else:
    			ans = (ans * no) % m
    	
    	for i in range(l,64):
    		#cout << "i " << i << endl;
    		if ((1L << i) & k) != 0:
    			return 0
    	return ans
    
    if __name__ == "__main__":
    	#n = int(sys.stdin.readline())
    	n, k, l, m =  map(int, sys.stdin.readline().split())
    	M = m
    	F[0]=F[1]=1;
    	print(solve(n,k,l,m)) % M