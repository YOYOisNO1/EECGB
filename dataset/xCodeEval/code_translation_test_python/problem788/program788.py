def extendedEuclidean(a,b,x,y):
    
        if b==0:
            return a,1,0
    
        d,x1,y1 = extendedEuclidean(b,a%b,x,y)
        
        x,y = y1,x1-y1*(a//b)
    
        return d,x,y
    
    a,b,c = map(int,input().split())
    
    f = [1]*(1+max(a,b,c))
    fi = [1]*(1+max(a,b,c))
    m = 998244353
    
    for i in range(1,1+max(a,b,c)):
        x = (f[i-1]*i)%m
        f[i] = x
        d,x,y = extendedEuclidean(x,m,1,1)
        fi[i] = x%m
    
    
    ab=0
    bc=0
    ca=0
    
    for i in range(min(a,b)+1):
        ab+=(f[a]*fi[a-i]*f[b]*fi[b-i]*fi[i])%m
    
    for i in range(min(b,c)+1):
        bc+=(f[c]*fi[c-i]*f[b]*fi[b-i]*fi[i])%m 
    
    for i in range(min(a,c)+1):
        ca+=(f[a]*fi[a-i]*f[c]*fi[c-i]*fi[i])%m
    
    print((ab*bc*ca)%m)
    
    
    
    