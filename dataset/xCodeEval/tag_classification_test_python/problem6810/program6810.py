    import os,io
    from sys import stdout
    import collections
    # import random
    # import math
    # from operator import itemgetter
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
    from collections import Counter
    # import heapq
    # from functools import lru_cache
    
    # import sys
    # sys.setrecursionlimit(10**6)
    
    # from functools import lru_cache
    # @lru_cache(maxsize=None)
    
def primes(n):
        sieve = [True] * n
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        return [2] + [i for i in range(3,n,2) if sieve[i]]
    
def binomial_coefficient(n, k):
        if 0 <= k <= n:
            ntok = 1
            ktok = 1
            for t in range(1, min(k, n - k) + 1):
                ntok *= n
                ktok *= t
                n -= 1
            return ntok // ktok
        else:
            return 0
    
def powerOfK(k, max):
        if k == 1:
            return [1]
        if k == -1:
            return [-1, 1]
    
        result = []
        n = 1
        while n <= max:
            result.append(n)
            n *= k
        return result
    
def prefixSum(arr):
        for i in range(1, len(arr)):
            arr[i] = arr[i] + arr[i-1]
        return arr
    
def divisors(n):
        i = 1
        result = []
        while i*i <= n:
            if n%i == 0:
                if n/i == i:
                    result.append(i)
                else:
                    result.append(i)
                    result.append(n/i)
            i+=1
        return result
    
def kadane(a,size):
        max_so_far = 0
        max_ending_here = 0
    
        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
    
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
    
    # @lru_cache(maxsize=None)
def digitsSum(n):
        if n == 0:
            return 0
        r = 0
        while n > 0:
            r += n % 10
            n //= 10
        return r
    
    # INPUTS  --------------------------
    # s = input().decode('utf-8').strip()
    # n = int(input())
    # l = list(map(int, input().split()))
    # t = int(input())
    # for _ in range(t):
    
    options = 0
    k = int(input())
    require = k
    s = input().decode('utf-8').strip()
    s = list(s)
    for i in range(len(s)//2):
        a = s[i]
        b = s[-1-i]
        if a == '?' and b == '?':
            options += 1
        elif a == '?':
            if ord(b) - 96 > k:
                print("IMPOSSIBLE")
                exit()
            s[i] = s[-1-i]
        elif b == '?':
            if ord(a) - 96 > k:
                print("IMPOSSIBLE")
                exit()
            s[-1-i] = s[i]
        elif a != b:
            print("IMPOSSIBLE")
            exit()
        elif ord(a) - 96 > k:
            print("IMPOSSIBLE")
            exit()
    
    c = Counter(s)
    if options < k - len(c.items()):
        print('IMPOSSIBLE')
        exit()
    
    while chr(k+96) in c and k > 1:
        k -= 1
    
    if len(s) % 2 != 0 and s[(len(s)//2)] == '?':
        s[(len(s)//2)] = chr(k+96)
        c[chr(k+96)] = 2
        while chr(k+96) in c and k > 1:
            k -= 1
    
    for i in range(len(s)//2, -1, -1):
        a = s[i]
        b = s[-1-i]
        if a == '?' and b == '?':
            s[i] = chr(k+96)
            s[-1-i] = chr(k+96)
            c[chr(k+96)] = 2
            while chr(k+96) in c and k > 1:
                k -= 1
    
    for e in s:
        if ord(e) - 96 > require:
            print('IMPOSSIBLE')
            exit()
    
    del c['?']
    if require != len(c.items()):
        print('IMPOSSIBLE')
        exit()
    
    print("".join(s))