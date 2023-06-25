def program1179():
    c="abcdefgh"
    d="12345678"
    
    f=str(input())
    c=c.index(f[0])
    d=d.index(f[1])
    
    if (c==0 or c==7) and (d==0 or d==7):
        print(3)
    elif c%7 * d%7==0 :
        print(5)
    else:
        print(8)
    