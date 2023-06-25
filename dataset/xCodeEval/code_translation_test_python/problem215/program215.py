def program215():
    r,x,y,z,t = map(int, input().strip().split())
    d = complex(z-x, t-y)
    st = int(abs(d))
    if d.real*d.real + d.imag*d.imag == st*st and st % (2*r) == 0:
        print(st/(2*r))
    else:
        s = abs(d)/(2*r)
        st = int(s)
        print(st) + 1
    