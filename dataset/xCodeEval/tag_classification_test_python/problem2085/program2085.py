    
    dic = {}
    
    dic[False] = {}
    dic[True] = {}
    
    mod = int(10**9 + 7)
def foo(n,d,k,satisfied):
    	if (d>n and not satisfied):
    		return 0
    	elif n==0 and satisfied:
    		return 1
    	elif n==0 and not satisfied:
    		return 0
    	elif n<0:
    		return 0
    	else:
    		if n in dic[satisfied]:
    			return dic[satisfied][n]
    		else:
    			dic[satisfied][n] = 0
    			for i in range(1,k+1):
    				dic[satisfied][n] =  (foo(n-i, d, k, satisfied or i>=d)%mod + dic[satisfied][n]%mod)%mod
    			return dic[satisfied][n]
    
    n1,k1,d1 = map(int, input().strip().split(" "))
    
    print(foo(n1,d1,k1,False))