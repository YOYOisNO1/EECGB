    t=int(input())
    res=[]
def gcd(x,y):
        s=max(x,y)
        k=min(x,y)
        if min(x,y)==0:
            return max(x,y)
        if s%k==0:
            return k
        return gcd(k,s%k)
    for i in range(t):
        k=int(input())
        
        res.append(int(100/gcd(100-k,k))
    for i in res:
        print(i)
    