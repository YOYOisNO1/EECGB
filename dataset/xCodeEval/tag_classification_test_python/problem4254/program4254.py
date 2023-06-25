def program4254():
    n,m=map(int,input().split())
    l=[]
    f=[]
    for j in range(n):
        l.append(1)
    b=list(map(int,input().split()))
    for i in b:
        for j in range(i-1,n):
            l[j]=0
            f.append(i)
            n=n-1
    f.sort()
    print(*f,sep=' ') 