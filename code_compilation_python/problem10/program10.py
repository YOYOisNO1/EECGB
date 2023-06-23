    ﻿#!/usr/bin/python
    
    import sys, os
    sys.setrecursionlimit(10000)
    
def readrow():
    	return sys.stdin.readline().strip().split(' ')
    
def iscomfortable(a, b):
    	return (a - b) in [-3, -2, -1, 0, 1]
    (al, ar) = map(int, readrow())
    (bl, br) = map(int, readrow())
    
    if iscomfortable(al, br) or iscomfortable(ar, bl):
    	print('YES')
    else:
    	print('NO')