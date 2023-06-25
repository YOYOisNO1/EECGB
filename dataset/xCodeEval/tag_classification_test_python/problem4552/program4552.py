def program4552():
    n,x,y=map(int,input().split())
    print(["YES","NO"][(x==n/2 or x==n/2+1) and (y==n/2 or y==n/2+1)])