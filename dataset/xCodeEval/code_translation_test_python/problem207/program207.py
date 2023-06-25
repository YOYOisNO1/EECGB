def program207():
    ties=int(input())
    scarves=int(input())
    vests=int(input())
    jackets=int(input())
    e=int(input())
    f=int(input())
    ans=0
    if f>e:
        ans+=min(scarves,vests,jackets)*f
        jackets-=min(scarves,vests,jackets)
        ans+=(min(ties,jackets)*e)
    else:
        ans+=min(ties,jackets)*e
        jackets-=min(ties,jackets)
        ans+=min(scarves,vests,jackets)*f
    print(ans)