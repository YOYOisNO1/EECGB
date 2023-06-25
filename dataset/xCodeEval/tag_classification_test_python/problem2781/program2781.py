def program2781():
    import math
    import time
    n,m,k = map(int,input().split())
    t = m/k	
    mod = 1000000009
    req = t - (n-m) + ((n-m) + m%k)/k  #remove m/k elements.take them to other side include the m%k elements to again combine 
    
    if req < 0:
    	ans = m
    else :
    	ans =  ((m -req*k)%mod + (((pow(2,req+1,mod)%mod - 2)%mod)*k)%mod)%mod
    
    print(ans)
    
    
    
    	
    	