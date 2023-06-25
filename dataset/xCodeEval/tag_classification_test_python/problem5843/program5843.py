def program5843():
    a=map(int, input().split())
    b=map(int, input().split())
    c,d=a[0]*a[1],b[0]*b[1]
    cc2,cc3,cd2,cd3,ans=0,0,0,0,0
    while c%2==0:
        c/=2
        cc2+=1
    while c%3==0:
        c/=3
        cc3+=1
    while d%2==0:
        d/=2
        cd2+=1
    while d%3==0:
        d/=3
        cd3+=1
    if c!=d:
        print(-1)
        exit(0)
    while cc3 > cd3:
        if a[0]%3 == 0:
            a[0]/=3
            a[0]*=2
        else:
            a[1]/=3
            a[1]*=2
        cc3-=1
        cc2+=1
        ans+=1
    while cd3 > cc3:
        if b[0]%3 == 0:
            b[0]/=3
            b[0]*=2
        else:
            b[1]/=3
            b[1]*=2
        cd3-=1
        cd2+=1
        ans+=1
    while cc2 > cd2:
        if a[0]%2 == 0: a[0]/=2
        else: a[1]/=2
        cc2-=1
        ans+=1
    while cd2 > cc2:
        if b[0]%2 == 0: b[0]/=2
        else: b[1]/=2
        cd2-=1
        ans+=1
    print(ans)
    print(a[0],) a[1]
    print(b[0],) b[1]