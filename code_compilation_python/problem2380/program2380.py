def program2380():
    x=int(input())
    y=int(input())
    if x>0 and y>0:
        print(0,(x+y),(x+y),0)
    if x<0 and y>0:
        print((x-y),0,0,-(x-y))
    if x<0 and y<0:
        print((x+y),0,0,(x+y))
    if x>0 and y<0:
        print(0,-(x-y),x-y,0)
    return 0    