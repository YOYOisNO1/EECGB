def program1572():
    c, d = map(int, input().split())
    n, m = map(int, input().split())
    k = int(input())
    
    s = n*m - k
    res = 0
    while s:
        if c > min(s, n) * d:
            res += min(s,n) * d
        else:
            res += c
        s -= min(s,n)
    print(res)