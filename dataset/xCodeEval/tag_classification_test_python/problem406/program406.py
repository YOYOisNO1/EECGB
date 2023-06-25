    # -*- coding: utf-8 -*-
    """
    Created on Mon Dec 19 14:26:28 2016
    
    @author: Chandak
    """
    
    import sys
    sys.setrecursionlimit(10000)
    
    r = lambda : map(int, input().split())
    
    l, a, b, c = r()
    x = sorted([a, b, c])
    a, b, c = x
    rec = [ -1 for i in xrange(4000 + 1) ]
    rec[0] = 0
    
def dp(l):
        global a, b, c, rec
        if rec[l] != -1 :
            return rec[l]
        if l < 0 :
            return float('-inf')
        elif l == 0 :
            return 0
        else :
            rec[l] = max(dp(l-a)+1, dp(l-b)+1, dp(l-c)+1)
            return rec[l]
            
        
    print(dp(l))
        
    
    
    
        