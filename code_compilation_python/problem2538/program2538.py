    '''
def soch(n,k):
        r,e=max(k,n-k),min(k,n-k)
        ans=1
        ansv=1
        for i in range(r+1,n+1):
            ans*=i
        for i in range(1,e+1):
            ansv*=i
        return ans//ansv
    n,k=map(int,input().split())
    ans=1
    s=1
    y=k-n//2
    if k<n:
        for i in range(1,min(n//2+(n%2==1)+1,k+1)):
            s=(s*(n-i+1))//i
            ans+=s
            if y>0 and i>=y:
                ans+=s
        if y>0 and i%2==1:
            ans-=s
        print(ans%(10**9+7))
    else:
        print(pow(2,n,10**9+7))