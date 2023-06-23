def program2222():
    from math import *
    n,m,k=map(int,input().split())
    r,l=0,0
    
    if k!=n:
        r=n-k
    if k!=1:
        l=k-1
    if l>r:
        S=((1+l)*(l)//2)+((l+n)*r//2)
    else:
        S=((1+r)*(r)//2)+((r+n)*l//2)
    S+=k
    s=max(l,r)+1
    L,R=max(l,r),min(l,r)
    if L-1>R:
        B=False
        L-=1
    else:
        L-=1
        R-=1
        B=True
    
    while S>m:
        s=s-1
        S-=L+R
        S-=1
        if L==0 and R>0 :
            s=s-1
            S-=2
            R-=1
            break
        if L>0:
            L-=1
        if B:
            R-=1
        elif L==R:
            B=True
       
      
    if (m-S)//n!=0:
        s+=(m-S)//n
    if 
    print(s)
    
        
        
    
        