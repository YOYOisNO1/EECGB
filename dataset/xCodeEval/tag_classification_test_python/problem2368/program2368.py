def program2368():
    n,w=map(int,input().split())
    a=input().split()
    a=[(int(a[i]), i) for i in range(n)]
    a.sort()
    o=[0]*n
    for i in range(n):
        x=(a[i][0]+1)//2
        w-=x
        o[a[i][1]]+=x
        if w<0:print(-1);exit()
    j=n-1
    while j>=0 and w>0:
        x=min(a[j][0]-o[a[j][1]],w)
        w-=x
        o[a[j][1]]+=x
        j-=1
    if w!=0:print(-1);exit()
    print(' '.join(map(str, o)))