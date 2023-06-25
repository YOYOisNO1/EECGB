def program4602():
    n, k = map(int, input().split())
    g = tuple(map(ord, input()))
    
    e = [-1] * 91
    
    for i in range(n):
        e[g[i]] = i
    curS = 0
    f = 1
    met = [0] * 91
    for i in range(n):
        if met[g[i]]:
            if i == e[g[i]]:
                curS -= 1
            continue
        curS += 1
        met[g[i]] = 1
        if curS > k:
            f = 0
            break
        if i == e[g[i]]:
            curS -= 1
    
    if f: print("NO")
    else: print("YES")