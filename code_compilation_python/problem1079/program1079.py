def program1079():
    n,a,b=[int(x) for x in input().split()]
    j=n//2
    k=min(a,b)
    c1=k//j
    s=[]
    while(k>0):
        s.append(c1)
        k=k-c1
    l=n-j
    m=max(a,b)
    c2=m//l
    while(m>0):
        s.append(c2)
        m-=c2
    print(min(s))
    
    
        