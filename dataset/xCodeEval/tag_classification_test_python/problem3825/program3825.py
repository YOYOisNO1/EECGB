def program3825():
    n=input()
    v=[map(int,input().split())+[-1] for _ in range(n)]+[[-1],[-1]]
    b={}
    for a in [[v[i],v[j],v[k]] for i,j,k in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0))]:
        for x in a[0]:
            for y in a[1]:
                for z in a[2]:
                    t=0
                    for d in (x,y,z):
                        if d>=0:
                            t=t*10+d
                    b[t]=1
    for x in range(2000):
        if x not in b:
            print(x-1)
            break