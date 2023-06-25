    '''
        Auther: ghoshashis545 Ashis Ghosh
        College: jalpaiguri Govt Enggineering College
        Date:08/06/2020
    
    '''
    from os import path
    import sys
    from functools import cmp_to_key as ctk
    from collections import deque,defaultdict as dd 
    from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
    from itertools import permutations
    from datetime import datetime
    from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())
    abc='abcdefghijklmnopqrstuvwxyz'
    abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    mod=1000000007
    #mod=998244353
    inf = float("inf")
    vow=['a','e','i','o','u']
    dx,dy=[-1,1,0,0],[0,0,1,-1]
    
def func(a,x):
        ans=0
        n=len(a)
        for i in range(n,0,-1):
            x1=(1<<i)-1
            if(x>=x1):
                ans+=a[i-1]
                x-=x1
                if(x>0):
                    ans+=a[i]%(2*a[i-1])
                    x-=1
        return ans
        
            
        
        
        
        
        
def solve():
        
        
        # for _ in range(ii()):
        n,l,r=mi()
        
        a=[n]
        while(n>1):
            a.append(n//2)
            n//=2
        a.reverse()
        cnt1=[a[0]]
        for i in range(1,len(a)):
            cnt1.append(2*cnt1[i-1]+a[i]%2)
        tot=(1<<len(cnt1))-1
        if(r>tot):
            r-=tot
        if(l>tot):
            l-=tot
        x=func(cnt1,r)
        y=func(cnt1,l-1)
        print(x-y)
        
        
        
        
        
        
        
    if __name__ =="__main__":
        solve()