def program6430():
    n = int(input())
    s = input() 
    
    mat = [[[int(0),int(0),""] for _i in range(n+1)] for _j in range(n+1)]
    
    
    
    
    for i in range(2*n):
    	digit = int(s[i])
    	toIter = min(i,n)
    
    	minh = max(i-n,0)
    	maxh = min(n,i)
    
    	for m in range(minh,maxh+1):
    		h = i - m
    		v = mat[h][m]
    
    		if h < n:
    			#add current symbol to homer
    			vnext = mat[h+1][m];
    			sumhmn = vnext[0]*pow(10,(2*n-h-2)) + vnext[1]*pow(10,(2*n-m-1));
    			sumhm = (v[0]*10+digit)*pow(10,(2*n-h-2)) + v[1]*pow(10,(2*n-m-1));
    			if sumhm >= sumhmn :
    				vnext[0]=v[0]*10+digit
    				vnext[1]=v[1]
    				vnext[2]=v[2]+'H'
    		if m < n:
    			#add current symbol to marge
    			vnext = mat[h][m+1];
    			sumhmn = vnext[0]*pow(10,(2*n-h-1)) + vnext[1]*pow(10,(2*n-m-2));
    			sumhm = v[0]*pow(10,(2*n-h-1)) + (v[1]*10+digit) * pow(10,(2*n-m-2));
    			if sumhm >= sumhmn :
    				vnext[0]=v[0]
    				vnext[1]=v[1]*10+digit
    				vnext[2]=v[2]+'M'
    	
    
    
    print(mat[n][n][2])
    			
    
    