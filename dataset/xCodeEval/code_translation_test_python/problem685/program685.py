def program685():
    n,m=map(int,input().split(" "))
    x=map(int,input().split(" "))
    y=map(int,input().split(" "))
    d=dict()
    for i in range(10):
        d[i]=-1
    for i in y:
        d[i]=1
    for i in x:
        if d[i]==1:
            print(i,)