def program810():
    n=int(input())
    ans=0
    i=1 
    while(i<=n+1):
        ans+=n-i+1
        i*=10
    print(ans)