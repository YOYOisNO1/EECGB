def func(x,limit):
        while True:
            if(x < 0):
                x = -x
            elif (x > limit):
                x = 2.0*limit - x
            else:
                return x
    text = input()
    a,b,m = map(int,text.split())
    text = input()
    vx,vy,vz = map(int,text.split())
    dx = a/2.0 + (m*1.0/-vy)*vx
    dz = (m*1.0/-vy)*vz
    dx = func(dx,a)
    dz = func(dz,b)
    print("%.6f %.6f") % (dx,dz)