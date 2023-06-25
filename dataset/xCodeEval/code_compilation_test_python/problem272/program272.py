    z,zz=input,lambda:list(map(int,z().split()))
    zzz=lambda:[int(i) for i in stdin.readline().split()]
    szz,graph,mod,szzz=lambda:sorted(zz()),{},10**9+7,lambda:sorted(zzz())
    from string import *
    from re import *
    from collections import *
    from queue import *
    from sys import *
    from collections import *
    from math import *
    from heapq import *
    from itertools import *
    from bisect import *
    from collections import Counter as cc
    from math import factorial as f
    from bisect import bisect as bs
    from bisect import bisect_left as bsl
    from itertools import accumulate as ac
def lcd(xnum1,xnum2):return (xnum1*xnum2//gcd(xnum1,xnum2))
def prime(x):
        p=ceil(x**.5)+1
        for i in range(2,p):
            if (x%i==0 and x!=2) or x==0:return 0
        return 1
def dfs(u,visit,graph):
        visit[u]=True
        for i in graph[u]:
            if not visit[i]:
                dfs(i,visit,graph)
    
    ###########################---Test-Case---#################################
    """
    
    
    
    """
    ###########################---START-CODING---##############################
    
    
    n,s=zz()
    
    
    
def big(n,s):
        arr=[9]*n
        ans=[-1]
        for i in range(1,n+1):
            arr[-i]=0
    
            if sum(arr)>s:
                continue
            c=1
            
            for j in range(0,10):
                arr[-i]=j
            
                if sum(arr)==s:
                    return arr
                    c=0
                  
            
        if c==1:return [-1]
    
def small(n,s):
        arr=[1]+[0]*(n-1)
        ans=[-1]
        for i in range(1,n+1):
            arr[-i]=9
    
            if sum(arr)<s:
                continue
            c=1
            
            for j in range(9,-1,-1):
                arr[-i]=j
            
                if sum(arr)==s:
                    return arr
                    c=0
    
        if c==1:return [-1]
    if s==0:
        if n==1:print(0,0)
        else:print(-1,-1)
        exit()
    print(''.join(str(i) for i in small(n,s)),''.join(str(i) for i in big(n,s)))
        
            
            
                
    
        
        
    
    
    
    
    
    
    
    
    
    
        
        
        
            
            
                
            
            
            
        
        
            
        
            
        
        
        
            
            
        
        
            
            
            
            
            
            
            
    
        
        
    
        
    
        
            
            
            
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        