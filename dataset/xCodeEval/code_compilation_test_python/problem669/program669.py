def program669():
    n,k,t=map(int,input().split())
    s=0
    a=[]
    for i in range(t):
        if i+1<=k:
            s+=1
            a.append(s)
        elif i+1>n-k and i+1<=n:
            a.append(s)
        else:
            s-=1
            a.append(s)
    print(a[t-1])