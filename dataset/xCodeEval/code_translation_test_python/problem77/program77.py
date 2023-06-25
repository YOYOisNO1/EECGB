def program77():
    I=lambda:map(int,input().split())
    n,m=I();a=I();k=b=0
    for i in range(n):
        k+=[0,1][b+a[i]>m]
        b=[b+a[i],a[i]][b+a[i]>m]
    print(k+1)