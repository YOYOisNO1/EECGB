    from math import *
def div(x):
        s=0
        for i in range(2,floor(sqrt(x))+1):
            if x%i==0:s+=1
            if x%(x//i)==0 and i!=x//i:s+=1
        if x==1:return s+1
        return s+2
    d=[-1]*(1000001)
    a,b,c=map(int,input().split());ans=0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                if d[i*j*k]==-1:d[i*j*k]=div(i*j*k)
                ans=(ans+d[i*j*k])
    print(ans)