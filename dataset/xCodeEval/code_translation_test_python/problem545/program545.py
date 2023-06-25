    z,zz=input,lambda:list(map(int,z().split()));
    szz,dgraphs,mod=lambda:sorted(zz()),{},10**9+7
    from string import *
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
            if x%i==0 and x!=2:return 0
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
    
    l1=list('qwertyuiop')
    l2=list('asdfghjkl;')
    l3=list('zxcvbnm,./')
    s=''
    
    
    
    d=z()
    if d=='R':
        p=-1
    if d=='L':
        p=1
        
    
        
    l=list(z())
    
    
    for i in l:
        try:
            t=l1.index(i)
            s+=l1[t+p]
        except:pass
        try:
            t=l2.index(i)
            s+=l2[t+p]
        except:pass
        try:
            t=l3.index(i)
            s+=l3[t+p]
        except:pass
     
    
    
    
    
    
    
    
    
    
    
    print(s)
    
    
            
            
            
    
    
    
    
    