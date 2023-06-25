    from math import *
    from Queue import *
    from sys import *
    from random import *
    
    
    
def myExp(a,b):
        c = 10**9 + 7
        if b == 0:
            return 1
        if b == 1:
            return a%c
        e = 1
        new = a
        while 2*e < b:
            new = (new*new)%c
            e = 2*e
        return ((new*myExp(a,b-e))%c)
    
    p, k = map(int, input().split())
    if k == 1:
        print(myExp(p,p))
        exit(0)
    if k == 0:
        o = 1
    else:
        o = 1
        n = k
        while n%p != 1:
            o += 1
            n = (n*k)%p
    res = myExp(p,((p-1)/o))
    print(res)