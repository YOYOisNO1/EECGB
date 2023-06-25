    M = 10
    
    l = set()
    r = set()
    
def genl(i, s):
        if (i == M):
            l.add(s)
            return
    
        genl(i + 1, s - a[i])
        genl(i + 1, s)
        genl(i + 1, s + a[i])
    
    
def genr(i, s):
        if (i == M):
            r.add(s)
            return
    
        genr(i + 1, s - b[i])
        genr(i + 1, s)
        genr(i + 1, s + b[i])
    
    
    w, n = map(int, input().split())
    
    if w == 2:
        print("YES")
        exit(0)
    
    a = []
    for i in range(M):
        a.append(w ** i)
    
    b = []
    for i in range(M):
        b.append(w ** (M + i))
    
    genl(0, 0)
    genr(0, 0)
    
    for e in l:
        if (n - e) in r:
            print("YES")
            exit(0)
    
    print("NO")