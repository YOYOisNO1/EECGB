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
    import Queue
    l=[0]*2
    l[0]=list(input())
    l[1]=list(input())
    s=0
    for i in range(0,len(l[0])-1):
        t=0
        if(l[0][i]=="X"):
            t+=1
        if(l[0][i+1]=="X"):
            t+=1
        if(l[1][i]=="X"):
            t+=1
        if(l[1][i+1]=="X"):
            t+=1
        if(t==1):
            l[0][i],l[0][i+1],l[1][i],l[1][i+1]="X","X","X","X"
            s+=1
        elif(t==0):
            l[0][i],l[1][i],l[1][i+1]="X","X","X"
            s+=1
    print(s)