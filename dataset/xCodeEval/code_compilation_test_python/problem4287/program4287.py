    import sys
    from collections import deque
    from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
    from itertools import permutations
    from datetime import datetime
    from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())
    
def read():
        zz=0
        if zz:
            input=sys.stdin.readline
        else:   
            sys.stdin=open('input1.txt', 'r')
            sys.stdout=open('output1.txt','w')
    
    abc='abcdefghijklmnopqrstuvwxyz'
    abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    mod=1000000007
    #mod=998244353
    inf = float("inf")
    vow=['a','e','i','o','u']
    dx,dy=[-1,1,0,0],[0,0,1,-1]
    
    
    
        
def solve():
        
        
        
    
        n=1000005
        sieve=[1]*1000005
        sieve[0],sieve[1]=0,0
        for i in range(2,int(sqrt(n))):
            if(sieve[i]):
                for j in range(i*i,n,i):
                    sieve[j]=0
        for i in range(1,n):
            sieve[i]+=sieve[i-1]
            
          
    def check(m):
            for i in range(a,b-m+2):
                x=sieve[i+m-1]-sieve[i-1]
                if(x<k):
                    return 0
            return 1
            
            
                
    def bs(r):
            l=1
            ans=-1
            while(l<=r):
                m=l+(r-l)//2
                if(check(m)):
                    ans=m
                    r=m-1
                else:
                    l=m+1
            return ans
        
        
        # print(sieve)
        global a,b,k
        a,b,k=mi()
        ans=bs(b-a+1)
        print(ans)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
    if __name__== "__main__":
        read()
        solve()