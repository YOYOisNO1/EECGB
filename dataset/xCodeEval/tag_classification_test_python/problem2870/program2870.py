    MOD=10**9+7
def fact(n):
        pdt=1
        for i in range(1,n+1):
            pdt*=i
            pdt%=MOD
        return pdt
def nPr(n,r):
        pdt=1
        for i in range(r):
            pdt*=n
            pdt%=MOD
            n-=1
        return pdt
    
    n,x,pos=[int(x) for x in input().split()]
    
    smallerCnts=x-1
    largerCnts=n-x
    
    requiredSmallerCnts=0
    requiredLargerCnts=0
    
    l=0
    r=n
    while True:
        if l-1==pos: #must move right until right==left
            while l<r:
                m=(l+r)//2
                r=m #a[m] must be > x
                requiredLargerCnts+=1
            break
        m=(l+r)//2
        if m==pos: # a[m] must be x
            l=m+1
        elif m<pos: # a[m] must be <x
            requiredSmallerCnts+=1
            l=m+1
        else: #a[m] must be >x
            requiredLargerCnts+=1
            r=m
    if requiredLargerCnts>largerCnts or requiredSmallerCnts>smallerCnts:
        ans=0
    else:
        remainder=n-1-requiredLargerCnts-requiredSmallerCnts
        ans=nPr(smallerCnts,requiredSmallerCnts)*nPr(largerCnts,requiredLargerCnts)
        ans%=MOD
        ans*=fact(remainder)
        ans%=MOD
    print(ans)