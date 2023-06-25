    from collections import defaultdict
    from fractions import gcd
    from bisect import *
    import sys
    sys.setrecursionlimit(5*10**6)
def sint():
        return int(input())
def sarr():
        return [int(x) for x in input().split()]
def sstr():
        return input()
    
    import time
    t1=time.time()
    tl=320 ## total length 5*30*2=300
    vis=[]
    for i in range(tl):
        vis.append([0]*tl)
    dp=[]
    for i in range(tl):
        tmp2=[]
        for j in range(tl):
            tmp1=[]
            for k in range(8):
                tmp1.append([0]*32)
            tmp2.append(tmp1)
        dp.append(tmp2)
    #print(time.time()-t1)
    xp=[1,1,0,-1,-1,-1,0,1]
    yp=[0,1,1,1,0,-1,-1,-1]
    
def abc(lev,x,y,dir):
        global n,a
        if lev==n:
            return
        if dp[x+(tl/2)][y+(tl/2)][dir][lev]==1: ##start putting firework from the middle of grid
            return
        dp[x+(tl/2)][y+(tl/2)][dir][lev]=1
        xx,yy=0,0
        for i in range(1,a[lev]+1):
            xx=x+xp[dir]*i
            yy=y+yp[dir]*i
            vis[xx+(tl/2)][yy+(tl/2)]=1
        abc(lev+1,xx,yy,(dir+1)%8)
        abc(lev+1,xx,yy,(dir+7)%8)
    
    
    t=1
    for ii in range(t):
        n=sint()
        a=sarr()
        abc(0,0,-1,2)
        r=0
        for i in range(tl):
            for j in range(tl):
                r+=vis[i][j]
        print(r)