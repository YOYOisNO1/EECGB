def program1944():
    n,a,b=map(int,input().split())
    x=map(int,input().split())
    y=map(int,input().split())
    z=[0]*(n+1)
    for i in range (0,a):
        z[x[i]]=1
    for i in range (0,b):
        if z[y[i]]==0:
            z[y[i]]=2
    for i in range (1,n+1):
        print(z[i])