    #      
    import collections
    from functools import cmp_to_key
    #key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )
    import math
    import sys
def getIntList():
        return list(map(int, input().split()))    
    
    import bisect 
    try :
        import numpy
        dprint(=) print(dprint('debug) mode')
    except ModuleNotFoundError:
    def dprint(*args, **kwargs):
            pass
def makePair(z):
        return  [(z[i], z[i+1]) for i in range(0,len(z),2) ]
def memo(func):  
        cache={}  
    def wrap(*args):  
            if args not in cache:  
                cache[args]=func(*args)  
            return cache[args]  
        return wrap
    
    @memo
def comb (n,k):
        if k==0: return 1
        if n==k: return 1
        return comb(n-1,k-1) + comb(n-1,k)
    N, = getIntList()
    
    if N <=100:
        zz0 = set()
        for  a in range(N+1):
            for b in range(N+1):
                for c in range(N+1):
                    if a+b+c >N: continue
                    zz0.add(a*4 + b*9 + c*49)
        #dprint(zz)
        for i in range(100):
            if i not in zz0:
                pass
                #dprint(i)
        print(len(zz0))
        sys.exit()
    outn  = [1,2,3,5,6,7,10,11,14,15,19,23]    
    zz = set( )
    for x in outn:
        zz.add( x + (N-50) * 49)
    for c in range(51):
        for b in range(51):
            for a in range(51):
                if a+b+c >50: continue
                zz.add(a*4 + b*9 + c*49 + (N-50) * 49)
    #dprint(zz)
    r0 = len(zz) +  (N-50) * 49 -12;
    print(r0)
    
     
    