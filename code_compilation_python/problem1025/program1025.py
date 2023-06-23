    import sys
    from math import *
    from collections import defaultdict
    from string import ascii_lowercase as lcs
    from string import ascii_uppercase as ucs
    from fractions import Fraction, gcd
    from decimal import Decimal, getcontext
    from itertools import product, permutations, combinations, count
    #getcontext().prec = 500
    #sys.setrecursionlimit(30000)
    
    mod = 10**9 + 7
    
    input = lambda: sys.stdin.readline().rstrip()
    die = lambda : exit(0)
    flush= lambda : sys.stdout.flush()
    
    r_s = lambda: input()                   #read str
    r_ss = lambda: input().split()          #read stringss
    r_i = lambda: int(input())              #read int
    r_is = lambda: map(int, input().split())#read ints
    r_f = lambda: float(input())            #read float
    r_fs = lambda: map(Decimal, input().split()) #read floats
    
    '''-------------------------------------------------------------------'''
    
def quad(x,y):
        if x*y>0:
            if x>0:
                return '1'
            else:
                return '3'
        else:
            if x<0:
                return '2'
            else:
                return '4'
    
    
    while True:
        x,y=r_is()
        r=sqrt(x**2+y**2)
        if x==0 or y==0 or r==int(r):
            print 'black'
        elif int(r)%2==0:
            if quad(x,y)=='1' or quad(x,y)=='3':
                print 'black'
            else:
                print 'white'
    
        else:
            if quad(x,y)=='1' or quad(x,y)=='3':
                print 'white'
            else:
                print 'black'
        #break
    