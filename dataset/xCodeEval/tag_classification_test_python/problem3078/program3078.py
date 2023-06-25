def program3078():
    from math import inf as inf
    from math import *
    from collections import *
    import sys
    input=sys.stdin.readline
    t=1
    while(t):
        t-=1
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        re=a[0]
        s=0
        for i in range(n):
            if(s*(a[i]+1)<=i):
                s+=1
        print(s)