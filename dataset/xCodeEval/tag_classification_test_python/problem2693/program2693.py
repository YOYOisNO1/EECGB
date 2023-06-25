def program2693():
    import math
    n,m=[int(i) for i in input().split()]
    red=2*n
    green=5*n
    blue=8*n
    rred=math.ceil(red/m)
    rgreen=math.ceil(green/m)
    rblue=math.ceil(blue/m)
    print(rgreen+rred+rblue)