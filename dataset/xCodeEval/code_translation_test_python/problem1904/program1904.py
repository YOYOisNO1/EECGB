def program1904():
    #-*-coding=utf8-*-
    debug = False
    
    a,b,m = map(int, input('').split(' '))
    vx,vy,vz = map(int, input('').split(' '))
    
    A,B,C,D = 0,1,0,0
    x0,y0,z0 = a/2.0, m, 0
    t = (-A*x0-B*y0-C*z0-D)/float(A*vx+B*vy+C*vz)
    xi,yi,zi = x0+t*vx, y0+t*vy, z0+t*vz
    xi,yi,zi = abs(xi)%(2*a), abs(yi)%m, abs(zi)%(2*b)
    if xi>a:
        xi = abs(xi-2*a)
    
    if zi>b:
        zi = abs(zi-2*b)
    
    if not debug:
        print("%.10f %.10f" % (xi,zi))