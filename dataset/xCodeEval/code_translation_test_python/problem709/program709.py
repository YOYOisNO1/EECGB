    #import resource
    #import sys
    #resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])
    #sys.setrecursionlimit(0x10000000)
    from sys import stdin, stdout
def GCD(x, y):
       while(y):
           x, y = y, x % y
       return x
def BS(arr, l, r, x):
        if r >= l:
            mid = l + (r - l)/2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return BS(arr, l, mid-1, x)
            else:
                return BS(arr, mid+1, r, x)
        else:
            return -1
    from bisect import bisect_left as bl
    from bisect import bisect_right as br
    import itertools
    import math
    a=input()
    b=input()
    e=[]
    for i in range(2,a):
        if(a%i==0):
            e.append(i)
    for i in range(len(e)):
        d=b[:e[i]]
        d=d[::-1]+b[e[i]:]
        b=d[:]
    print(b[::-1])