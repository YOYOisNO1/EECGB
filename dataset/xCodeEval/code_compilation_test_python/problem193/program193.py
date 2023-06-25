def program193():
    u,v=map(int,input().split())
    if u>v:
        print(-1)
        exit(0)
    if u==0 and v==0:
        print(0)
        exit(0)
    if u==v:
        print(1)
        print(u)
        exit(0)
    
    binary=[2**i for i in range(61)]
    p=[0]*60
    d=v-u
    v-=u
    for i in range(60-1,-1,-1):
        p[i]+=u//binary[i]
        u%=binary[i]
    answer=[]
    for i in range(60-1,0,-1):
        if v>=binary[i]:
            p[i-1]+=2
    f=True
    print(max(p))
    while True:
        f=False
        k=0
        for i in range(60-1,-1,-1):
            if p[i]>0:
                f=True
                p[i]-=1
                k+=binary[i]
        if f:
            print(k,end=" ")