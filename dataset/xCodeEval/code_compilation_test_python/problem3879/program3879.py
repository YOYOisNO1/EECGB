def program3879():
    ch=input().split()
    a=int(ch[0])
    b=int(ch[1])
    e=int(ch[2])
    f=int(ch[3])
    ts=e
    ms=f
    while (e!=f):
        if (e>f):
            e=e-f
        else:
            f=f-e
    if (e!=1):
        ts=int(ts/e)
        ms=int(ms/e)
    e=int(a/ts)
    f=int(b/ms)
    print (min(e,f))