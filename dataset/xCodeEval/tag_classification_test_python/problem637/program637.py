def program637():
    mp = [9*[0] for i in range(9)]
    l = [[] for i in range(9)]
    n, m = map(int, input().split())
    ans=0
    for i in range(m):
        a, b = map(int, input().split())
        mp[a][b]=1
        mp[b][a]=1
        l[a].append(b)
        l[b].append(a)
    if n<7:
        ans=m
    else:
        for i in range (1,n+1):
            e=m-len(l[i])
            t=0
            for j in range(1,n+1):
                if j==i:
                    continue
                h=0
                for k in l[i]:
                    h+=(mp[j][k]==0)
                t=max(t,h)
            ans=max(ans,e+t)
    print(ans)