    #!/usr/bin/env python2
    # -*- coding: utf-8 -*-
    import sys
    input = sys.stdin
    output = sys.stdout
    
    from math import sqrt
    from itertools import repeat
    
def primes_eratosthene_leq_simple(N):
        primes = [True]*(N+1)
        primes[0] = False
        primes[1] = False
        SQRT_N = int(sqrt(N))
        for i in range(2,SQRT_N+1):
            if primes[i]:
                primes[i*i:N+1:i] = repeat(False, len(primes[i*i:N+1:i]))
        P = []
        for p,prime in enumerate(primes):
            if prime:
                P.append(p)
        return P
    
def solve(n):
        P = primes_eratosthene_leq_simple(n)
        N = 0
        m = len(P)
        for i in range(m):
            a = P[i]
            if 2*a > n:
                break
            for j in range(i+1,m):
                b = P[j]
                if 2*b > n:
                    break
                for ip in range(1,13):
                    aa = a**ip
                    if 2*aa > n:
                        break
                    for jp in range(1,13):
                        bb = b**jp
                        if 2*bb > n:
                            break
                        p = aa*bb
                        if p <= n:
                            N += 1
                            #print(p) 
        return N
    
    n = int(input.readline())
    
    a = solve(n)
    output.write('%s\n' % str(a))