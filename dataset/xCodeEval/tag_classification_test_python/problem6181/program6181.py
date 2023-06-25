def program6181():
    x1,y1,x2,y2=map(int,input().split())
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    print(2) - int(dx==0 or dy==0)
    if(x1+y1)%2!=(x2+y2)%2:
        print(0)
    else:
        print(2-int(dx==dy))
    print(max(dx,dy))