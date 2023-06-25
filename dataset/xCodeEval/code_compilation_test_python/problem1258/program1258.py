def program1258():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    #a.sort()
    l=[]
    for i in range(n):
        l.append((a[i],i+1))
    l.sort()
    cnt=0
    p=[]
    s=0
    for i in range(n):
        s=s+l[i][0]
        if s=<m:
            cnt+=1
            p.append(l[i][1])
        else:
            print(cnt)
            print(*p)
    
            