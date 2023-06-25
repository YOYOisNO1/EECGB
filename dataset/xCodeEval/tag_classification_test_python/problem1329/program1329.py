def program1329():
    n,k,m,d=map(int,input().split())
    ans=min(n,m)
    for i in range(1,d+1):
        xmin=n/(i*k)
        if n%(i*k)>xmin:
            xmin+=1
        xmax=n/(k*(i-1)+1)
       # print(i,xmin,xmax,m)
        if xmin>m or xmin>xmax:
            continue
        ans=max(ans,i*min(xmax,m))
    print(ans)
        