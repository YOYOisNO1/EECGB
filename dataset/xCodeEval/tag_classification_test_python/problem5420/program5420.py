    from collections import defaultdict, Counter,deque
    from math import sqrt, log10, log, floor, factorial,gcd
    from bisect import bisect_left, bisect_right
    from itertools import permutations,combinations
    import sys, io, os
    input = sys.stdin.readline
    # input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    # sys.setrecursionlimit(10000)
    inf = float('inf')
    mod = 10 ** 9 + 7
def get_list(): return [int(i) for i in input().split()]
def yn(a): print("YES" if a else "NO")
    ceil = lambda a, b: (a + b - 1) // b
    
    import __pypy__
    
    int_add = __pypy__.intop.int_add
    int_sub = __pypy__.intop.int_sub
    int_mul = __pypy__.intop.int_mul
    
    
def make_mod_mul(mod=10**9 + 7):
        fmod_inv = 1.0 / mod
    
    def mod_mul(a, b, c=0):
            res = int_sub(int_add(int_mul(a, b), c), int_mul(mod, int(fmod_inv * a * b + fmod_inv * c)))
            if res >= mod:
                return res - mod
            elif res < 0:
                return res + mod
            else:
                return res
    
        return mod_mul
    
    
    mod_mul = make_mod_mul()
    
    
def mod_pow(x, y):
        if y == 0:
            return 1
        res = 1
        while y > 1:
            if y & 1 == 1:
                res = mod_mul(res, x)
            x = mod_mul(x, x)
            y >>= 1
        return mod_mul(res, x)
def memodict(f):
        """ Memoization decorator for a function taking a single argument. """
        class memodict(dict):
        def __missing__(self, key):
                ret = self[key] = f(key)
                return ret
    
        return memodict().__getitem__
    
    
def memoize(f):
        """ Memoization decorator for a function taking one or more arguments. """
        class memodict(dict):
        def __getitem__(self, *key):
                return dict.__getitem__(self, key)
    
        def __missing__(self, key):
                ret = self[key] = f(*key)
                return ret
    
        return memodict().__getitem__
    @memoize
def fun(n,k):
        a = 1
        if n % 2 == 0:
            mul = mod_pow(2, n - 1)
            for i in range(1, k + 1):
                a = (a * (mul - 1)) % mod
                a = (a + mod_pow(2, ((i - 1) * n))) % mod
            # print(a)
            return a
        else:
            # print(mod_pow(mod_pow(2, n - 1) + 1, k))
            return mod_pow(mod_pow(2, n - 1) + 1, k)
    t=int(input())
    for i in range(t):
        n,k=[int(i) for i in input().split()]
        print(fun(n,k))
        # a=1
        # if n%2==0:
        #     mul=mod_pow(2,n-1)
        #     for i in range(1,k+1):
        #         a=(a*(mul-1))%mod
        #         a=(a+mod_pow(2,((i-1)*n)))%mod
        #     print(a)
        # else:
        #     print(mod_pow(mod_pow(2,n-1)+1,k))
    
    """
    3 1 case
    0 0 0 
    n=4,k=2 case
    0 0 0 0
    4c0+4c2+4c4=1 + 6 + 1 =8
    00
    00
    00
    00
    8+6*8+1*(2**4)
    =8+48+16
    =72
    000
    000
    000
    000
    72+72*6+1*(2**8)
    """