    from math import hypot as hy
def sign(i): return 1 if i < 0 else 0
    x,y = map(int,input().split())
    r=hy(x, y)
    r2=x*x+y*y
    print(['white','black'][r2) in [i*i for i in xrange(1001)] or (int(r)+sign(x)+sign(y))%2==0]