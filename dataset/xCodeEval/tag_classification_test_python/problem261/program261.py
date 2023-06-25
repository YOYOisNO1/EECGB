def program261():
    n, c = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if l[i+1] < l[i]:
            ans = max(l[i]-l[i+1]-c, ans)
    print(ans)