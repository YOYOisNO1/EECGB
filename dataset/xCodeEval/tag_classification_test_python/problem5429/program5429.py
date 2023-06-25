    from math import inf
    from collections import *
    import math, os, sys, heapq, bisect, random
    from functools import lru_cache
    from itertools import *
def inp(): return sys.stdin.readline().rstrip("\r\n")
def out(var): sys.stdout.write(str(var))  # for fast output, always take string
def inpu(): return int(inp())
def lis(): return list(map(int, inp().split()))
def stringlis(): return list(map(str, inp().split()))
def sep(): return map(int, inp().split())
def strsep(): return map(str, inp().split())
def fsep(): return map(float, inp().split())
    M,M1=1000000007,998244353
    mod = M
    
    #-------------------not so clear-------------------
def main():
        how_much_noob_I_am = 1
        how_much_noob_I_am = inpu()
        for __ in range(how_much_noob_I_am):
            n,k= sep()
            Pn1 = pow(2, n-1, mod)
            Pn = pow(2, n, mod)
            if n % 2 == 1:
                print(pow(Pn1 + 1, k, mod))
            else:
                ANS = pow(Pn1 - 1, k, mod)
                for i in range(k):
                    ANS = (ANS + pow(Pn1 - 1, i, mod) * 1 * pow(Pn, k - i - 1, mod)) % mod
                print(ANS)
    
    if __name__ == '__main__':
        main()