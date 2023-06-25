    n,m = (int(i) for i in input().split(" "))
    
    edges = [0] * ((n + 5) ** 2)
    
    for it in range(m):
        u,v = (int(i) for i in input().split(" "))
        u -= 1; v -= 1;
        edges[u * n + v] = 1
        edges[v * n + u] = 1
    
    if n == 1:
        print("Yes")
        print("a")
        exit(0)
    
    if n == 2:
        print("Yes")
        print("ac") if m == 0 else "aa"
        exit(0)
    
def findPair():
        for i in range(n):
            for j in range(i + 1, n):
                if edges[i * n + j] == 0:
                    return (i, j)
        return (None, None)
    
    
    (ai, ci) = findPair()
    if ai is None:
        print("Yes")
        print("a") * n
        exit(0)
    
    #print(ai,) ci
    
    a = set()
    a.add(ai)
    b = set()
    c = set()
    c.add(ci)
    
    for i in range(n):
        if i == ai or i == ci: continue
        isAll = True
        aedge = edges[i * n + ai]
        cedge = edges[i * n + ci]
        if not aedge and not cedge:
            print("No")
            exit(0)        
        for j in range(n):
            if i == j: continue
            if not edges[i * n + j]:
                isAll = False
        if isAll:
            b.add(i)
        else:
            if aedge and cedge:
                print("No")
                exit(0)
            if aedge:
                a.add(i)
            else:
                c.add(i)
    
    for i in range(n):
        if i in b: continue
        if i in a:
            for j in range(i + 1, n):
                if (edges[i * n + j] == 0) != (j in c):
                    print("No")
                    exit(0)
        else:
            for j in range(i + 1, n):
                if (edges[i * n + j] == 0) != (j in a):
                    print("No")
                    exit(0)
    
    result = ""
    for i in range(n):
        if i in a:
            result += 'a'
        elif i in b:
            result += 'b'
        elif i in c:
            result += 'c'
        else:
            print("No")
            exit(0)
    
    print("Yes")
    print(result)
    exit(0)