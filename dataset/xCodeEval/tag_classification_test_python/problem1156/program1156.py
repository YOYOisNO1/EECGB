def program1156():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    res = 0
    if e > f:
        x = min(a,d)
        a -= x
        d -= x
        res += x * e
        x = min(b,c,d)
        b-=x
        c-=x
        d-=x
        res += x * f
    else:
        x = min(b,c,d)
        b-=x
        c-=x
        d-=x
        res += x * f
        x = min(a,d)
        a -= x
        d -= x
        res += x * e
    print(res)