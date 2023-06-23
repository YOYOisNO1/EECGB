    a,b,p,x = list(map(int, input().strip().split()))
    
    
def brute(a,b,p,x):
        for n in range(1, x+1):
            if (n*pow(a,n,p)) % p == b:
                print(n)
    
    #brute(a,b,p,x)
    
    sols = 0
    
    inva = pow(a,p-2,p)
    
    a2 = 1
    b2 = b
    s = 0
    d1 = -b
    while s < p-1:
        k = (d1 + s) % p
        u = k
        while (p-1)*u + s <= x:
            n = (p-1)*u + s
            #print(s, k, n)
            #print(n*pow(a,n,p) % p, b)
            sols += 1
            u += p
        d1 = (d1 * inva) % p
        s += 1
    
    print(sols)
            
    
            
        
    