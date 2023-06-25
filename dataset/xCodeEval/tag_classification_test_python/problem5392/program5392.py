def program5392():
    mod=10**9+7
    
    for _ in range(int(input())):
        n,k=map(int,input().split())
        total=pow(2,n,mod)
        h=pow(2,n-1,mod)
        if k==0:
            print(1)
            continue
        if n%2==0:
            c=0
            t=1
            p={}
            prev=1
            for i in range(k+1):
                p[i]=prev
                prev=(prev*total)%mod
    
            for i in range(k):
                c+=t*p[k-i-1]
                c%=mod
                t=(t*(h-1))%mod
            c+=t
            c%=mod
            print(c)
        else:
            print(pow(h+1,k,mod))
    
    