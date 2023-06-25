    import math
    x, y = map(int, input().split())
    ans = {}
    mod = 10 ** 9 + 7
    if y%x !=0:
    	print(0)
    else:
    	a=y/x
    	factors=[]
    	for i in xrange(2, int(math.floor(math.sqrt(a))+1)):
    		if a%i==0:
    			factors.append(i)
    			a!=i*i and factors.append(a/i)
    	factors.sort()
    	ans[1]=1
	def getAns(f):
    		if f in ans:
    			return ans[f]
    		res=pow(2,f-1,mod)
    		res=(res+mod-1)%mod
    		for i in factors:
    			if i>=f:
    				break
    			if f%i==0:
    				res+=(mod-getAns(i))
    				res%=mod
    
    		ans[f]=res
    		return res
    	print(getAns(a))