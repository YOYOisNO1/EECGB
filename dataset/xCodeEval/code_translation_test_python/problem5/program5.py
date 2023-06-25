def program5():
    x,y,xx,yy=map(int,input().split())
    dy=abs(yy-y)
    dx=abs(x-xx)
    print((dx/2+1)*(dy/2+1)+(dx/2)*dy/2)