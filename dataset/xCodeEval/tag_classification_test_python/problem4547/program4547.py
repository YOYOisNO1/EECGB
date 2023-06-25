def proB(n,k):
        mod=1e9+7
        ans=1
        while(k):
            ans=int(ans*n%mod)
            k-=1
        return ans
    t=int(input())
    for i in range(t):
        n,k=list(map(int,input().split()))
        print(proB(n,k))