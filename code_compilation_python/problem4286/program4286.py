    import sys, os.path
    from collections import*
    from copy import*
    import math
    mod=10**9+7
    if(os.path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")   
    
    N = 15
    is_prime = [0] * N
     
def primes():
        for i in range(2, N):
            if is_prime[i] == 1:
                continue
            for j in range(2*i, N, i):
                is_prime[j] = 1
     
    a, b, k = map(int, input().split())
    primes()
    cnt_primes = [0] * N
    for i in range(2, N):
        cnt_primes[i] = cnt_primes[i-1] + (1 - is_prime[i])
    
    
def valid(x):
        for i in range(a, b-x+2):
            if cnt_primes[i+x-1] - cnt_primes[i-1] < k:
                return False
        return True
     
def binary_search():
        f, e = 1, b-a+1
        best=-1
        while f<=e:
            m = f+(e-f)//2
            if valid(m):
                best=m
                e = m - 1            
            else:
                f = m + 1
        return best
     
    res = binary_search()
    print(res)
    
    
    
    
    
     