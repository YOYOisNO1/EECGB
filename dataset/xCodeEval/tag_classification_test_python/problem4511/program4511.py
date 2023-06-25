def R(): return map(int, input().split())
def I(): return int(input())
def S(): return str(input())
    
    from collections import Counter 
    
    import math
    import sys
    
    
    f = open('test.txt', 'w')
    
    #f.write('haha')
    
    n,m=R()
    
    fact=[1]*(n+1)
    
    for i in range(1,n+1):
        fact[i]=fact[i-1]*i
        fact[i]%=m
    
    sum=0
    for i in range(1,n+1):
        sum=(sum+fact[n-i+1]*fact[i]*(n-i+1))%m
    
    print(sum%m)