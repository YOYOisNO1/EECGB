def f(l,r,n,i):
        if(l==r):
            return n
        mid=(l+r)/2
        if(i==mid):
            return n%2
        if(i<mid):
            return f(l,mid-1,n/2,i)
        if(i>mid):
            return f(mid+1,r,n/2,i)
    n,l,r=map(int,input().split())
    if(n==0):
        print('0')
    else:
        if(n==1):
            print('1')
        else:
            ln=1
            x=n
            ans=0
            while x>1:
                x/=2
                ln=2*ln+1
            for i in range(l,r+1):
                ans+=f(1,ln,n,i)
            print(ans)