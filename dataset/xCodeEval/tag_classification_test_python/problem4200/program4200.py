    r2=lambda:map(int,input().split())
    r3=lambda:list(map(int,input().split()))
    n,k=r2()
    lst=r3()
def ceil(x):
        if(int(2*x)==2*int(x)):
            return x
        else:
            return x+1
    s=sum(lst)*1.0
    v=(s)/n
    c=0
    
    if(ceil(v)<k):
        while(ceil(v)<k):
            n=n+1
            s=s+k
            v=s/n
            c=c+1
            
            
    print(c)
        