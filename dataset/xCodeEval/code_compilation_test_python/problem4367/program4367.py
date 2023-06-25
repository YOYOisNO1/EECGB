    '''input
    5 1000
    38361 75847 14913 11499 8297
    '''
    
    import sys
    pow2 = pow              # for modular expo pow2(base, n, mod)
    from math import *
    from time import time
    from collections import defaultdict
    from bisect import bisect_right, bisect_left
    from string import ascii_lowercase as lcs
    from string import ascii_uppercase as ucs
    from fractions import Fraction, gcd
    from decimal import Decimal, getcontext
    from itertools import product, permutations, combinations
    #getcontext().prec = 500
    sys.setrecursionlimit(30000)
    
    # What doesn't challenge you, makes you weaker.
    
    mod = 10**9 + 7
    INF = sys.maxint
    
    input = lambda: sys.stdin.readline().rstrip()
    die = lambda : exit(0)
    flush= lambda : sys.stdout.flush()
    
    r_s = lambda: input().strip()                   #read str
    r_ss = lambda: input().split()          #read stringss
    r_i = lambda: int(input())              #read int
    r_is = lambda: map(int, input().split())#read ints
    r_f = lambda: float(input())            #read float
    r_fs = lambda: map(Decimal, input().split()) #read floats
    
    # For effieciently taking lots of queries with each query in a separate line
    # having integer values separated by space. A 2d list is made with each row
    # corresponding to line. Each row is a list with all the values.
    # Use this for fast I/O by taking all input in one go.
    r_qs = lambda: map(lambda s:map(int, s.split(' ')), sys.stdin.readlines())
    
    '''-------------------------------------------------------------------'''
    
    # Call it as dbg(varName=varName)
def dbg(**kwargs):
        print "Value of '" + kwargs.keys()[0] + "' is", kwargs[kwargs.keys()[0]]
    
    
def main():
    
    
    def solve(pos, end, sum1, ans=0):
            if pos==end:
                sum1.append(ans)
                sum1.append((ans+arr[pos])%m)
                return
            solve(pos+1, end, sum1, ans)
            solve(pos+1, end, sum1, (ans+arr[pos])%m)
    
        n, m =r_is()
        arr = r_is()
        sum1 = []
        sum2 = []
        solve(0, n/2-1, sum1)
        solve(n/2, n-1, sum2)
        # print sum1
        # print sum2
        res = max(sum2)
        sum2.sort()
    
        for elem in sum1:
            new = m-elem
            lower = bisect_left(sum2, new)
            # print elem, new, lower
            if lower!=0:
                res = max(res, elem+sum2[lower-1])
            else:
                res = max(res, elem)
        print res
    
    if __name__ == '__main__':
        # local = True
        local = True
        if local:
            try:
                sys.stdin = open('input.txt')
                print 'Running at local.'
                for i in range(r_i()):
                    main()
            except IOError:
                main()
        else:
            main()
    
    