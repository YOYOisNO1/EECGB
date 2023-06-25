    #from math import factorial
    MOD=1000000007
def solve(n,k):
    	if(n%2):#odd
    		ks=pow(2,n-1,MOD)+1
    		return pow(ks,k,MOD)
    	else:#even
    		ks=pow(2,n-1,MOD)-1
    		if(k==0)
    			return 1
    		else:
    			ans=1+ks
    			for i in range(1,k):#1 2 3 4 5 6 ... k-1
    				ans=((ans*ks)%MOD+pow(2,i*n,MOD))%MOD
    				ans%=MOD
    			return ans
    t=int(input())
    for alskfjlakfja in range(t):
    	n,k=[int(i) for i in input().split()]
    	print(solve(n,k))