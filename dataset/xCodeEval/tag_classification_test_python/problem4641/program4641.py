def program4641():
    import math as mt 
    import sys,string
    input=sys.stdin.readline
    import random
    from collections import deque,defaultdict
    L=lambda : list(map(int,input().split()))
    Ls=lambda : list(input().split())
    M=lambda : map(int,input().split())
    I=lambda :int(input())
    n,k=M()
    s=input().strip()
    l=[0]*26
    v=[0]*26
    g=0
    for i in s:
        l[ord(i)-65]+=1
    for i in s:
        if(v[ord(i)-65]==0):
            v[ord(i)-65]=1
            if(g<k):
                g+=1
                l[ord(i)-65]-=1
                if(l[ord(i)-65]==0):
                    g-=1
            else:
                print("YES")
                exit()
        else:
            l[ord(i)-65]-=1
            if(l[ord(i)-65]==0):
                g-=1
    print("NO")
    