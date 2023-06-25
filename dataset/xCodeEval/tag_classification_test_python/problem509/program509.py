    n,k=map(int,input().split())
    
def f(v,k):
        s,res=1,0
        while s<=v:
            res+=v/s
            s*=k
        return res
    
    a,b=1,1000000000
    while a<b:
        mid=(a+b)/2
        if f(mid,k)>=n:
            b=mid
        else:
            a=mid+1
    print(a)