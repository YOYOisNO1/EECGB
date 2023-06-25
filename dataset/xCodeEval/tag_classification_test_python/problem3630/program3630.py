def program3630():
    from collections import *
    from bisect import *
    #from math import *
    from heapq import *
    from fractions import *
    import sys
    input=sys.stdin.readline
    t=1
    while(t):
        t-=1
        n,tt=map(int,input().split())
        a=input().rstrip("\n")
        a=list(a)
        for i in range(tt):
            g,b=0,0
            j=0
            while(j<n-1):
                if(a[j]=='B' and a[j+1]=='G'):
                    a[j],a[j+1]=a[j+1],a[j]
                    j+=2
                else:
                    j+=1
        print(''.join(a))