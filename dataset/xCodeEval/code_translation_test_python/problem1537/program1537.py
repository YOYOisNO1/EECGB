    
    n,m=map(int,input().split())
    
    x,y=n/m,n%m
    
def ctx(a,b,m):
        if a==0 or b==0:
            return 0
        ct=0
        for i in range(1,a+1):
            for j in range(1,b+1):
                if (i*i+j*j)%m==0:
                    ct+=1
        return ct
    
    print(x*x*ctx(m,m,m)+2*x*ctx(m,y,m)+ctx(y,y,m))
    exit()
    