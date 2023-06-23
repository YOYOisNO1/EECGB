    #!/usr/bin/python
    
def memoize(f):
        cache= {}
    def memf(*x):
            if x not in cache:
                cache[x] = f(*x)
            return cache[x]
        return memf
    
    import sys
    
def Ni(): return tuple(map(int, sys.stdin.readline().split()))
    
    n, k, d = Ni()
    M = 10**9 + 7
    
    @memoize
def count(n, haveD):
        #print n, haveD
        if n == 0:
            return 1 if haveD else 0
    
        return sum(count(n - i, haveD or i >= d) for i range(1, min(n, k) + 1)) % M
    
    print count(n, False)