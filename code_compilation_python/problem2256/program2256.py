def program2256():
    A,B=map(int,input().split(" "))
    x,y,z=map(int,input().split())
    cy=2*x+y
    cb=3*z+y
    ans=max(0,cy-A)
    ans+=max(0,cb-B)
    print(ans