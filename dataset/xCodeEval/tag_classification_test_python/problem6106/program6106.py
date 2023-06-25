def program6106():
    import math
    x=input()
    print((0,1)[(1<<int(math.log(x*6,2)))-x*3<6])