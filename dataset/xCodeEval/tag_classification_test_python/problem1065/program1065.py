def program1065():
    t = int(input())
    r = 0
    a,b,c = input().split()
    d,e,f = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    if c > e + f:
        r += c - e - f
    elif a > d + f:
        r += a - d - f
    elif b > e + d:
        r += b - e - d
    print(r , min(a,e) + min(b,f) + min(c,d))