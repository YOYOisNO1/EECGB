def program3271():
    n = int(input())
    s = list(input())
    h = 0
    k = 0
    w = []
    while h != n:
        k = k + int(s[h])
        if h == n - 1:
            break
        if int(s[h+1]) == 0:
            w.append(str(k))
            k = 0
        h = h + 1
    w.append(str(k))
    
    w = ''.join(w)
    print(w)