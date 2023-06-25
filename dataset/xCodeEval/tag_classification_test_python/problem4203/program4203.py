    r1=lambda:input()
    #from math import *
    r2=lambda:map(int,input().split())
    r3=lambda:list(map(int,input().split()))
    n,k=r2()
    lst=r3()
    s=sum(lst)*1.0
    v=(s*1.0)/n
    c=0
def ceil(x):
        if(int(2*x)==2*int(x)):
            return x
        else:
            return x+1
    if(ceil(v)<k):
        while(ceil(v)<k):
            #print(v)
            s=s+k
            n=n+1
            v=s/n
            c=c+1
            #print(v)
            
    print(c)
        