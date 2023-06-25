def program129():
    n = int(input());
    s=[]
    t=0
    nums=[int(i) for i in range(1,n+1)]
    
    for i in range(1,n+1):
        d = sum(nums[:i])
        if(d<=n):
            t=nums[:i]
            
    
        
    t[-1]+=(n-sum(t))
    
    print(len(t))
    print(*t)
    
    
    
    
    
    
    