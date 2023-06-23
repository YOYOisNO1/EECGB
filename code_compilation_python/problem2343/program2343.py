def program2343():
    ######################################################################
    # Write your code here
    import sys
    from math import *
    input = sys.stdin.readline
    #import resource
    #resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
    #sys.setrecursionlimit(0x100000)
    # Write your code here
    RI = lambda : [int(x) for x in sys.stdin.readline().strip().split()]
    rw = lambda : input().strip().split()
    ls = lambda : list(input().strip()) # for strings to list of char
    from collections import defaultdict as df
    import heapq 
    #heapq.heapify(li) heappush(li,4) heappop(li)
    #import random
    #random.shuffle(list)
    infinite = float('inf')
    #######################################################################
    
    n,k=RI()
    
    if(k>=3n):
        print(0)
    else:
        print(3n-k)