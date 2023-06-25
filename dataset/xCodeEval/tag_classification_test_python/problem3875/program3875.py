def program3875():
    a, k = map(int, input().split())
    a = list(str(a))
    b = ''
    while a:
        pos = a.index(max(a[:k+1]))
        b += a[pos]
        k -= pos
        a.pop(pos)
    print(b)