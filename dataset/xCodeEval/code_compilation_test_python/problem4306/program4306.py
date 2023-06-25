    #!/usr/bin/python
    
    import sys, resource
    sys.setrecursionlimit(500000)
    resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
    
    n = int(input())
    
def read(i, L, D):
        L.append(map(int, input().split()))
        D.append(L[-1])
        return len(L) == n or read(i+1, L, D)
    
    L = []
    D = []
    read(0, L, D)
    
def memoize(f):
        cache= {}
    def memf(*x):
        def compute(x):
                cache[x] = f(*x)
            (x in cache) or (compute(x))
            return cache[x]
        return memf
    
    @memoize
def rec(i, j, k):
        D[i][j] = min(D[i][j], D[i][k] + D[k][j])
        ((k < n-1 and rec(i, j, k+1))) or \
        ((j < n-1) and rec(i, j+1, 0)) or \
        ((i < n-1) and rec(i+1, 0, 0))
        return True
    
    rec(0, 0, 0)
    
    print max(max(D))