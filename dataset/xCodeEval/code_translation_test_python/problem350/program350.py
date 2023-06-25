def program350():
    n= int(input())
    m=abs(n)
    a=[int(x) for x in str(m)]
    if n >= 0:
        print(n)
    else:
        b= list(a)
        a.pop(len(a)-1)
        b.pop(len(b)-2)
        z=[str(i) for i in a]
        x=[str(j) for j in b]
        z=int(''.join(z))
        x=int(''.join(x))
        z=min(z,x)
        if z == 0:
            print(z)
        else:
            print('-'+str(z))