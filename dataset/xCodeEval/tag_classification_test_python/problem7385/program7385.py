    #filename 623A Codeforce AIM Tech Round (Div. 1)
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = n * [False]
    for i in range(0,n):
        a[i] = n * [False]
    s = n * ['0']
    adj = n * [0]
    for i in range(0,m):
        u, v = input().split()
        u = int(u)-1
        v = int(v)-1
        a[u][v] = True
        a[v][u] = True
        adj[u] += 1
        adj[v] += 1
def dfs(u):
        #print(u)
        global res
        if adj[u] == n - 1:
            s[u] = 'b'
            return
        if s[u] == 'a':
            change = 'c'
        else:
            change = 'a'
            s[u] = 'c'
        for i in range(0,n):
            if not a[u][i] and i != u:
                if s[i] == s[u]:
                    res = 'No'
                    return
                else:
                    s[i] = change
                    #print(i)
            else:
                if i != u and s[i] == change:
                    res = 'No'
    res = 'Yes'
    for i in range(0,n):
        if res == 'Yes':
            dfs(i)
    print(res)
    if res == 'Yes':
        for i in s:
            print(i,end= "")
    
                