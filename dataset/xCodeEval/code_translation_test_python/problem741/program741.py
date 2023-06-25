    import sys
    from math import *
    readints=lambda:map(int, input().strip('\n').split())
    
    la,ra,ta=readints()
    lb,rb,tb=readints()
    
    
    k=(la-lb)/gcd(ta,tb)
    klo=floor(k)
    khi=ceil(k)
    
def intersection(ax,ay,bx,by):
        # print(ax,ay,bx,by)
        l,r=max(ax,bx),min(ay,by)
        if l>r: return 0
        return r-l+1
    
    # print(klo,khi)
    
    
    ans = 0
    for dk in [klo,khi]:
        df=lb-la + dk*gcd(ta,tb)
        bx=la+df
        by=bx+(rb-lb)
        #print(ax,ay,'df',df)
        ans = max(ans, intersection(la,ra,bx,by))
    
    
    
    print(ans)