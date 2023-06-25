def program394():
    import math
    r,x,y,x1,y1 = map(int,input().split())
    st = math.sqrt((x-x1)**2  + (y-y1)**2)
    print(math.ceil(st/(2*r)))