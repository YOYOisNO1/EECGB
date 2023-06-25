def program1499():
    # -*- coding: utf-8 -*-
    """
    Created on Wed Sep 14 00:39:11 2016
    
    @author: sigmoidguo
    """
    
    l1, r1, l2, r2, k = map(int, input().split())
    
    ll = max(l1, l2)
    rr = min(r1, r2)
    if k >= ll and k <= rr:
        lr = max(0, rr-ll)
    else:
        lr = max(0, rr-ll+1)
    
    print(lr)
    
    