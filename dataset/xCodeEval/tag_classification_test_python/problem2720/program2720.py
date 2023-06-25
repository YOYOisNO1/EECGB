def program2720():
    a,b,k=map(int,input().split())
    ans=max(a*(b/(k+1)),b*(a/(k+1)))
    if k>=a:
        ans=max(ans,b/(k-a+2))
    if k>=b:
        ans=max(ans,a/(k-b+2))
    if ans==0:
        print(-1)
    else:
        print(ans)