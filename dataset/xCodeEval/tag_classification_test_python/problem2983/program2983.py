    import sys,bisect
    from math import floor,ceil
    input = sys.stdin.readline
    import operator as op
    from functools import reduce
    
def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom
    
    mod = 998244353
    ############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
        return(int(input().rstrip()))
def inlt():
        return(list(map(int,input().rstrip().split())))
def insr():
        s = input().rstrip()
        return(s[:len(s) - 1])
def invr():
        return(map(int,input().rstrip().split()))
    ################################################################
    ############ ---- THE ACTUAL CODE STARTS BELOW ---- ############
    
    n,m,k = invr()
    result = (m * pow(m - 1,k,mod))%mod
    
    print((result * ncr(n - 1, k))%mod)