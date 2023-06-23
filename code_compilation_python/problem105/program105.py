def gcd(a,b):
            if(b==0):
                return a
            return gcd(b,a%b)
    
    x=list(map(int,input().split()))
    l=x[0]
    r=x[1]
    i=0
    a=l
    b=0
    y=False
    c=0
    
    for k in range(l,r):
        a=k
        for i in range(k+1,r):
                if(gcd(k,i)):
                    b=i
                    break
    
        if(b==0):
            break
        for j in range(i,r+1):
                if(gcd(b,j)==1 and gcd(a,j)!=1):
                    print(a,b,c,j)
                    y=True
                    c=j
                    break
    
        if(y):
            break
    if(y):
        print(a,b,c)
    else:
        print("-1")