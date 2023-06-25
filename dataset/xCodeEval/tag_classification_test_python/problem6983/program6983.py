def program6983():
    from math import *
    a,b,w,x,c = map(int,input().split())
    print([0,int(ceil(c-a+float(b-(c-a)*x)/(x-w)))][c>a])
    