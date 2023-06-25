def program1168():
    
    x,y,z=map(float,input().split())
    maxx=0
    k=0
    list1 = ['x^y^z', 'x^z^y','(x^y)^z', '(x^z)^y','y^x^z','y^z^x', '(y^x)^z', '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
    if(maxx<x**y**z) :
        maxx=x**y**z
        k=1
    if(maxx<x**z**y) :
        maxx=x**z**y
        k=2
    if(maxx<x**(y*z)) :
        maxx=x**(y*z)
        k=3
    if(maxx<x**(y*z)) :
        maxx=x**(y*z)
        k=4
    if(maxx<y**x**z) :
        maxx=y**x**z
        k=5
    if(maxx<y**z**x) :
        maxx=y**z**x
        k=6
    if(maxx<y**(x*z)) :
        maxx=y**(x*z)
        k=7
    if(maxx<y**(x*z)) :
        maxx=y**(x*z)
        k=8
    if(maxx<z**x**y) :
        maxx=z**x**y
        k=9
    if(maxx<z**y**x) :
        maxx=z**y**x
        k=10
    if(maxx<z**(x*y)) :
        maxx=z**(x*y)
        k=11
    if(maxx<z**(x*y)) :
        maxx=z**(x*y)
        k=12
    print list1[k-1]