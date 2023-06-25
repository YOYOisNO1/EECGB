def program4107():
    Y,B,R=list(map(int,input().split()))
    x=1
    y=2
    z=3
    while(x<Y and y<B and z<R):
        x=x+1
        y=y+1
        z=z+1
    print(x+y+z)