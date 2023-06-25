def program1994():
    n, k, d = map(int, input().split())
    v = [1] #all
    for i in range(1,n+1):
        s = 0
        for j in range(max(0, i-k),i):
            s += v[j]
        v.append(s)
    a = [1] #except
    for i in range(1,n+1):
        s = 0
        for j in range(max(0,i-d+1),i):
            s+=a[j]
        a.append(s)
    print((v[len(v)-1]-a[len(a)-1])%1000000007)