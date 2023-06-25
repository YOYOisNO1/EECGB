def program7033():
    n=input()
    ans=0
    i=1
    n-=1
    while i<=n:
        ans+=((n-i)/(i<<1)+1)*i
        i=i<<1
    print(ans)