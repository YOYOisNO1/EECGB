def program782():
    from math import *
    a=[int(i) for i in input().split()]
    l=((a[1]-a[3])**2+(a[2]+a[4])**2)**0.5
    print(ceil(l/(2*a[0]))