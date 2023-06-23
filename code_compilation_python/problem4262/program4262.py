    #Thanks to http://codeforces.com/profile/ZhouYuChen
    
    
'''def s(x):
    	if(x==0):
    		return 0
    	return x+s(x-1)
    
    
def calc(x):
    	m=1
    	ans=0
    	while(x):
    		ans2=s(x%10)
    		x/=10
    		ans2+=(45*x)
    		ans2*=m
    		ans+=ans2
    		m*=10
    	return ans
    
def bc(x):
    	ans=0
    	while(x):
    		ans+=x%10
    		x/=10
    	return ans
    
def brute(x):
    	ans=0
    	while(x>0):
    		ans+=bc(x)
    		x-=1
    	return ans
    
    a=int((input()))
    print calc(a), brute(a) '''
    
    a=int(input())
    s=(45*(10**101))
    k=(a-s)%a
    print k,(10**101)+k-1
    
    