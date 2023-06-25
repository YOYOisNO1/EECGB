def program351():
    x=int(input())
    if x>=0:
        print(x)
    else:
        y=str(x)
        z=list(y)
        e=z[len(z)-1]
        z1=list(y)
        z2=list(y)
        z.pop()
        s=int("".join(z))
        z.pop()
        z.append(e)
        s1=int("".join(z))
        if s1>s:
            print(s1)
        else:
            print(s)