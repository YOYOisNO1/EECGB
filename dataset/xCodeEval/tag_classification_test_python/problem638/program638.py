def program638():
    n,m=map(int,input().split())
    d=dict()
    for i in range(1,8):
        d[i]=set()
    for i in range(m):
        a,b=map(int,input().split())
        d[a].add(b)
        d[b].add(a)
    
    mn=100
    if n<7:
        print(m)
    else:
        for i in range(1,7):
            for j in range(i+1,8):
                s=d[i]&d[j]
                if len(s)<mn:
                    mn=len(s)
    
        print(m-mn)
        