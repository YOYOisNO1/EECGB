def program1257():
    l = []
    t = int(input())
    for _ in range(t):
        m,n = map(int,input().split())
        l.append((m,n))
    x = []
    y = []
    
    for i,j in l:
        x.append(i)
        y.append(j)
    z1 = sum(x)
    z2 = sum(y)
    q = False
    if(z1%2==0 and z2%2==0):
        print(0)
        quit()
    elif(z1%2!=0 and z2%2!=0):
        for i,j in l:
            if(i!=j and i%2!=j%2):
                q=True
    else:
        print(-1)
        quit()
    if(q):
        print(1)
    else:
        print(-1)