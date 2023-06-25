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
def Ns(): return tuple(map(int, sys.stdin.readline().split()))
    
    n, k, d = Ni()
    M = 10**9 + 7
    
    @memoize
def count(n, haveD):
        #print(n,) haveD
        if n == 0:
            if haveD:
                return 1
            else:
                return 0
    
        s = 0
        for i in range(1, min(n, k) + 1):
            s = (s + count(n - i, haveD or i >= d)) % M
    
        return s
    
    print(count(n,) False)