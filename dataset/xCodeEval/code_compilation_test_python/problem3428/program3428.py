    # -*- coding: utf-8 -*-
    
    """
    created by huash06 at 2015-05-18 15:10
    """
    __author__ = 'huash06'
    
    import sys
    import os
    import datetime
    import functools
    import itertools
    import collections
    
    
    
def findBeautifulStr(astr, index, pres, firsts, n):
        if index >= len(astr):
            if n == len(pres):
                return pres
            else:
                return []
        if len(astr) - index < n - len(pres):
            return []
    
        if astr[index] in firsts:
            return []
    
        if n == len(pres) + 1:
            return pres + [astr[index:]]
        for i in range(index+1, len(astr)-(n-len(pres))+1):
            res = findBeautifulStr(astr, i, pres + [astr[index:i]], firsts.union(astr[index]), n)
            if res:
                return res
        return []
    
    
    
    N = int(input())
    S = input()
    
    res = findBeautifulStr(S, 0, [], set(), N)
    if res:
        print('YES')
        for seg in res:
            print(seg)
    else:
        print('NO')