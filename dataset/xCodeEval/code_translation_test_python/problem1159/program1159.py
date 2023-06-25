def program1159():
    gcd = lambda a,b: gcd(b%a, a) if a else b
    lcm = lambda a,b: a*b/gcd(a,b)
    
    n=input()
    c=[0]+map(int,input().split())
    v = []
    
    
    o=1
    for i in range(1, n+1):
        if i in v: continue
        x=i
        q=0
        while x not in v:
            v += [x]
            x = c[x]
            q+=1
        if x != i:
            o=-1
            break
        if q%2==0: q/=2
        o=lcm(o, q)
    print(o)