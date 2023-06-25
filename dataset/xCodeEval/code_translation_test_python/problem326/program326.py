def program326():
    x,y=map(int,input().split())
    s=x//y
    r=x%y
    while(r!=0):
        x=y
        y=r
        s=s+x//y
        r=x%y
    print(s)