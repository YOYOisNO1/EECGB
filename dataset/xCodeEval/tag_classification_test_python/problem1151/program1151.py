    import sys
    import math
    import heapq
    import collections
def inputnum():
        return(int(input()))
def inputnums():
        return(map(int,input().split()))
def inputlist():
        return(list(map(int,input().split())))
def inputstring():
        return([x for x in input()])
def inputstringnum():
        return([ord(x)-ord('a') for x in input()])
def inputmatrixchar(rows):
        arr2d = [[j for j in input().strip()] for i in range(rows)] 
        return arr2d
def inputmatrixint(rows):
        arr2d = []
        for _ in range(rows):
            arr2d.append([int(i) for i in input().split()])
        return arr2d
        
    a = inputnum()
    b = inputnum()
    c = inputnum()
    d = inputnum()
    e = inputnum()
    f = inputnum()
    ans = 0
    if e > f:
        ans += e*(min(a, d))
        d -= min(a, d)
        ans += f*(min(b, min(c, d)))
        print(ans)
    else:
        ans += f*(min(b, min(c, d)))
        d -= min(b, min(c, d))
        ans += e*(min(a, d))
        print(ans)
        