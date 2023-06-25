    from __future__ import division, print_function
    _interactive = False
    
def main():
        n, k = input_as_list()
        print(comb(n, k) * strl2(n, n-k) * (1 if k==0 else 2))
    
    
    # Constants
    INF = float('inf')
    MOD = 998244353
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    
    # Python3 equivalent names
    import os, sys, itertools
    if sys.version_info[0] < 3:
        input = input
        range = xrange
    
        filter = itertools.ifilter
        map = itertools.imap
        zip = itertools.izip
    
    # print-flush in interactive problems
    if _interactive:
        flush = sys.stdout.flush()
    def printf(*args, **kwargs):
            print(*args, **kwargs)
            flush()
    
    # Debug print, only works on local machine
    LOCAL = "LOCAL_" in os.environ
    debug_print(=) (print) if LOCAL else (lambda *x, **y: None)
    
    # Fast IO
    if (not LOCAL) and (not _interactive):
        from io import BytesIO
        from atexit import register
        sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
        sys.stdout = BytesIO()
        register(lambda: os.write(1, sys.stdout.getvalue()))
        input = lambda: sys.stdin.readline().rstrip('\r\n')
    
    # Some utility functions(Input, N-dimensional lists, ...)
def input_as_list():
        return [int(x) for x in input().split()]
    
def input_with_offset(o):
        return [int(x)+o for x in input().split()]
    
def input_as_matrix(n, m):
        return [input_as_list() for _ in range(n)]
    
def array_of(f, *dim):
        return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
    
    from __pypy__.intop import *
    class ModInt(int):
    def __new__(cls, v): return int.__new__(cls, v%MOD)
    def __add__(self, other): return ModInt(int_mod(int_add(self, other), MOD))
    def __sub__(self, other): return ModInt(int_mod(int_sub(self, other), MOD))
    def __mul__(self, other): return ModInt(int_mulmod(self, other, MOD))
    def __div__(self, other): return ModInt(int_mulmod(self, pow(other, MOD-2, MOD), MOD))
        __truediv__ = __floordiv__ = __div__
    def __pow__(self, power, modulo=MOD): return ModInt(int.__pow__(self, power, modulo))
    
    
    # Combinatorics (ModInt)
def fact(n):
        if n < 0: return ModInt(1)
        res = ModInt(1)
        for i in range(1, n+1):
            res *= i
        return res
    
def perm(n, r):
        if r < 0 or n < r: return ModInt(0)
        res = ModInt(1)
        for i in range(n-r+1, n+1):
            res *= i
        return res
    
def comb(n, r):
        if r < 0 or n < r: return ModInt(0)
        if n//2 < r: r = n-r
        return perm(n, r) // fact(r)
    
def comb_rep(n, r):
        return comb(n+r-1, r)
    
def strl2(n, r):
        # strl2(4, 3): 1123, 1223, 1233, 2113, 2123, ...
        # = 3^4 - comb(3, 1)*2^4 + comb(3, 2)*1^4 = 36
        if r < 0 or n < r: return ModInt(0)
        res = ModInt(0)
        coef = ModInt(1)
        for i in range(1, r+1):
            b = ModInt(r-i+1)
            base = b**n
            res += coef * base
            coef = coef * b // i * -1
        return res
    
    
    main()