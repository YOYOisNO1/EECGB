def program3749():
    from collections import Counter
    a,b=Counter(list(input())),Counter(list(input()))
    ans=10**6
    for i in range(10):
        if a[str(i)]==0 or i in[2,5,6,9]:continue
        ans = min(ans, b[str(i)]/a[str(i)])
    if a['6']or a['9']:ans=min(ans,(b['6']+b['9'])/(a['6']+a['9']))
    if a['2']or a['5']:ans=min(ans,(b['2']+b['5'])/(a['2']+a['5']))
    print(ans)