def program5247():
    from itertools import permutations
    n,k=map(int,input().split())
    ar=[input() for i in range(n)]
    ans=float('inf')
    for p in permutations(range(k)):
        mx=0
        mn=float('inf')
        for e in ar:
            cur=0
            for i in p:
                cur=10*cur+(int(e[i]))
            mx=max(mx,cur)
            mn=min(mn,cur)
        ans=min(ans,mx-mn)
    print(ans)