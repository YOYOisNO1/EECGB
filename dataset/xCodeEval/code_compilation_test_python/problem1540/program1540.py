def program1540():
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @Time    : 2017/3/22 12:59
    # @Author  : mazicwong
    # @File    : 227A 叉积.py
    
    '''
    本题输入三个点坐标，考察叉积，若大于0则right，小于0则left，等于0则towards
    '''
    
    a = input().split(' ')
    b = input().split(' ')
    c = input().split(' ')
    xa = int(a[0])
    ya = int(a[1])
    xb = int(b[0])
    yb = int(b[1])
    xc = int(c[0])
    yc = int(c[1])
    x1=xb-xa
    y1=yb-ya
    x2=xb-xc
    y2=yb-yc
    ans=x1*y2-x2*y1
    if ans>0:
        print("RIGHT")
    elif ans<0:
        print("LEFT")
    else:
        print("TOWARDS")