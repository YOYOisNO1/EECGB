def fact(n) :
    	if n <= 1 :
    		return 1
    		return n * fact(n - 1)
    
    
		def c_n_k(k, n) :
    		return fact(n) / (fact(k) * fact(n - k))
    
    
    		n, k = map(int, input().split())
    		ans = 1
    
    		d = [0, 1, 3, 12, 60, 124]
    
    		for i in range(k, 1, -1) :
    			ans += c_n_k(i, n) * (d[i] - d[i] // i)
    
    				print(ans)