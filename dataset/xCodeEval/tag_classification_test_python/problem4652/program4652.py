def program4652():
    from time import time
    
    n, k = map(int, input().split())
    g = input()
    
    e = [-1] * 26
    
    for i in range(n):
        e[ord(g[i]) - 65] = i
    curS = 0
    f = 1
    met = [0] * 26
    for i in range(n):
        if not met[ord(g[i]) - 65]:
            curS += 1
            met[ord(g[i]) - 65] = 1
        if curS > k:
            f = 0
            break
        if i == e[ord(g[i]) - 65]:
            curS -= 1
    
    if f: print("NO")
    else: print("YES")