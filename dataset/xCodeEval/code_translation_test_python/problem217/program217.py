    import decimal,math
    # from decimal import Decimal as co
    from collections import Counter,defaultdict
    from fractions import gcd
    from bisect import bisect_right,bisect_left
    decimal.getcontext().prec = 10
def primeFactors(n): 
    	d=Counter()
    	while n % 2 == 0: 
    		d[2]+=1 
    		n = n / 2
    		  
    	for i in range(3,int(math.sqrt(n))+1,2): 
    		  
    		while n % i== 0: 
    			d[i]+=1 
    			n = n / i 
    	if n > 2: 
    		d[n]+=1
    	return d
     
    n,b=map(int,input().split())
    d=primeFactors(b)
    mn=10**21
    for i in d:
    	tt=n
    	power=i
    	ans=0
    	while tt/power:
    		ans+=(tt/power)
    		power*=i
    	mn=min(mn,ans/d[i])
    print(mn)
    		
# def findPowerOfP(n,p):
    # 	count=0  		
    # 	r=p
    # 	while(r<=n):
    # 		count+=(n/r)
    # 		r=r*p	
    # 	return count	  
    # a=[] 
    # n,b = map(int,input().split())
    # pp =  primeFactors(b)
    # print(pp)
    # ans= 10**20
    # for i in pp:
    # 	ans=min(ans,findPowerOfP(n,i)/pp[i])
    # print(ans)	