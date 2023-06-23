    '''
        Auther: ghoshashis545 Ashis Ghosh
        College: jalpaiguri Govt Enggineering College
    
    '''
    from os import path
    import sys
    from heapq import heappush,heappop
    from functools import cmp_to_key as ctk
    from collections import deque,Counter,defaultdict as dd 
    from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
    from itertools import permutations
    from datetime import datetime
    from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input().rstrip()
def mi():return map(int,input().split())
def li():return list(mi())
    abc='abcdefghijklmnopqrstuvwxyz'
    # mod=1000000007
    mod=998244353
    inf = float("inf")
    vow=['a','e','i','o','u']
    dx,dy=[-1,1,0,0],[0,0,1,-1]
    
def bo(i):
        return ord(i)-ord('0')
    
    file = 1
    
    
    
        
def solve():
    
    
    
    
        # for _ in range(ii()):
        n = ii()
        a = li()
        b = Counter(a)
        most_freq_elm,cnt = 0,1
        for i in b:
            if b[i] > b[most_freq_elm]:
                most_freq_elm = i
                cnt = 1
            elif b[i] == b[most_freq_elm]:
                cnt += 1
        if cnt > 1:
            print(n)
            return
    
        ans = 0
        for i in b:
            if i == most_freq_elm:
                continue
            prev_occur = [-2]*(2*n+1)
            prev_occur[n] = -1
            cnt = 0
            # print(prev_occur)
            for j in range(n):
                if a[j] == i:
                    cnt += 1
                elif a[j] == most_freq_elm:
                    cnt -= 1
                if prev_occur[cnt+n]==-2:
                    prev_occur[cnt+n] = j
                else:
                    ans = max(ans,j-prev_occur[cnt+n])
        print(ans)
    
    
    
    
    
    
        
            
                    
        
    
    
    
    
    
    
    
    
    
            
    if __name__ =="__main__":
    
        if(file):
    
            if path.exists('input.txt'):
                sys.stdin=open('input.txt', 'r')
                sys.stdout=open('output.txt','w')
            else:
                input=sys.stdin.readline
        solve()