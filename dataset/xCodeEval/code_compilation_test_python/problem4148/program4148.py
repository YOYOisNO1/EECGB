def program4148():
    n=input()
    m=int(input())
    
    l=len(n)
    a=[int(i) for i in n]
    n=long(n)
    
    ans=0
    
    mod=n%m
    ans = mod
    
    base=10**(l-1)
    base %= m
    
    #print base
    #print mod
    
    #for i in range(l-1, -1, -1):
    for i in range(l):
        mod = ((mod - a[i] * base % m) % m) + m
        mod %= m
        mod = (mod *10 + a[i]) % m
    
        if a[i] != 0:
            ans = min(ans, mod)
        #print mod
    
    print ans