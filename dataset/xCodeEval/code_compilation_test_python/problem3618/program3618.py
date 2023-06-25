def program3618():
    n,m=list(map(int,input().split()))
    a=[[0 for i in range(m)] for i in range(m)]
    s=0
    for i in range(m):
        for j in range(m):
            a[i][j]=(i+1)**2+(j+1)**2
            if a[i][j]%m==0:
                a[i][j]=1
            else:
                a[i][j]=0
            s=s+a[i][j]
    s=s*((n//m)**2)
    b=n%m
    for i in range(b):
        s=s+sum(a[i][:n])
    for i in range(b):
        for j in range(n):
            s=s+a[i][j]
    for i in range(b):
        for j in range(b):
            s=s+a[i][j]
    print(s)