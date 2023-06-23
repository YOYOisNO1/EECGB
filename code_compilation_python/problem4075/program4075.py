    #! /usr/bin/python2
    
    import sys
    import math
    
    n = int(input())
    s = ""
    for i in input().split():
        s = s + i
        
    ans = {'':False}
def ok(a):
        if (len(a) == 2):
            return True
        if (a in ans):
            return ans[a]
        if (a[-1] == a[-3] or a[-2] == a[-4]):
            if (ok(a[0 : len(a) - 4] + a[-2] + a[-1])):
                ans[a] = True
                return True
        if (len(a) > 7 and (a[-1] == a[-7] or a[-2] == a[-8])):
            if (ok(a[0: len(a) - 8] + a[-2] + a[-1] + a[-4:-1])):
                ans[a] = True
                return True
        ans[a] = False
        return False
    
    if (ok(s)):
        print("YES")
    else:
        print("NO")