    import math
    from collections import defaultdict
    
    dp = dict()
    fact = dict()
    
def facto(val) :
    	if val not in fact.keys() :
    		fact[val] = math.factorial(val)
    	return fact[val]
    
def hitung(frek, total) :
    	global dp
    	keys = ' '.join(str(x) for x in frek)
    	if keys in dp.keys() :
    		dp[keys] = 0
    		return dp[keys]
    	ans = 0
    	for i in range(1, 10) :
    		if frek[i] > 0 :
    			tmp = facto(total) // facto(frek[i]-1)
    			for j in range(0, 10) :
    				if i!=j and frek[j]>0 :
    					tmp //= facto(frek[j])
    			ans += tmp
    	for i in range(0, 10) :
    		if frek[i]>1 :
    			frek[i] -=1
    			ans += hitung(frek, total-1)
    			frek[i] += 1
    	dp[keys] = ans
    	return ans;
     
    n = int(input())
    if(n<10) :
    	print(1)
    else :
    	tmp = n;
    	frek = [ 0 for _ in range(10)]
    	total = 0
    	while tmp>0 :
    		frek[tmp%10]+=1
    		tmp //= 10
    		total += 1
    	print(hitung(frek, total-1))