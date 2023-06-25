def HCF(x, y):
       while(y):
           x,y=y,x%y
       return x
    
    
    x=input().split()
    t=int(x[0])
    w=int(x[1])
    b=int(x[2])
    LCM=(w*b)/HCF(w,b)
    fact=int(t/LCM)
    ans=fact*min(w,b)
    limit=fact*LCM
    left=t-limit
    ans+=min(left,min(w,b)-1)
    gcd=HCF(ans,t)
    ans/=gcd
    t/=gcd
    print(str(ans)+"/"+str(t))