    #import resource
    import sys
    #resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])
    #import threading
    #threading.Thread(target=main).start()
    #threading.stack_size(2**26)
    #sys.setrecursionlimit(10**6)
    mod=(10**9)+7
    fact=[1]
    for i in range(1,100001):
        fact.append((fact[-1]*i)%mod)
    ifact=[0]*100001
    ifact[100000]=pow(fact[100000],mod-2,mod)
    for i in range(100000,0,-1):
        ifact[i-1]=(i*ifact[i])%mod
    from sys import stdin, stdout
    from bisect import bisect_left as bl
    from bisect import bisect_right as br
    import itertools
    import math
    import heapq
    from random import randint as rn
    from Queue import Queue as Q
def find(x):
        if(x!=p[x]):
            p[x]=find(p[x])
        return p[x]
def union(x,y):
        m=find(x)
        n=find(y)
        if(m!=n):
            if(r[m]>r[n]):
                p[n]=m
            elif(r[m]<r[n]):
                p[m]=n
            else:
                p[n]=m
                r[m]+=1
def modinv(n,p):
        return pow(n,p-2,p)
def ncr(n,r,p):
        t=((fact[n])*((ifact[r]*ifact[n-r])%p))%p
        return t
def ain():
        return map(int,sin().split())
def sin():
        return stdin.readline().strip()
def GCD(x,y):
        while(y):
            x, y = y, x % y
        return x
def isprime(x):
        if(x==1):
            return False
        elif(x<4):
            return True
        for i in range(2,int(math.sqrt(x))+1):
            if(x%i==0):
                return False
        return True
    """**************************************************************************"""
    n,a,x,b,y=ain()
    s=0
    while(a!=x and b!=y):
        a+=1
        if(a==(n+1)):
            a=1
        b-=1
        if(b==0):
            b=n
        if(a==b):
            s=1
            break
    if(s==0):
        print"NO"
    else:
        print"YES"