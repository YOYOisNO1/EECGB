def program821():
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[0]*n
    for i in range(len(a)):
        c[a[i]-1]=1
    for j in range(len(b)):
        c[b[j]-1]=2
    for i in c:
        print(i,endl=" ")