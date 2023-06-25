    import os
    import sys
    import math
    import heapq
    from decimal import *
    from io import BytesIO, IOBase
    from collections import defaultdict, deque
    
def r():
        return int(input())
def rm():
        return map(int,input().split())
def rl():
        return list(map(int,input().split()))
    
    a = rl()
    a.sort()
    tri=False
    seg=False
    imp=False
    for i in range(2):
        for j in range(i+1,3):
            for k in range(j+1,4):
                if a[i]+a[j]>a[k]:
                    tri=True
                elif a[i]+a[j]==a[k]:
                    seg=True
    if tri:
        print('TRIANGLE')
    elif seg:
        print('SEGMENT')
    else:
        print('IMPOSSIBLE')