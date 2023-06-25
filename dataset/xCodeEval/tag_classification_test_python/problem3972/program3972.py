    # -*- coding: utf-8 -*-
    __author__ = 'artbataev'
    
def tryWeight(w, m, num):
        if num < 1:
            return False
    
        if m == 1:
            return True
    
        if m % w == 0:
            return tryWeight(w, m // w, num - 1)
        if (m + 1) % w == 0:
            return tryWeight(w, (m + 1) // w, num - 1)
        if (m - 1) % w == 0:
            return tryWeight(w, (m - 1) // w, num - 1)
    
        return False
    
    w, m = list(map(int, input().split()))
    
    if tryWeight(w, m, 101):
        print("YES")
    else:
        print("NO")
    