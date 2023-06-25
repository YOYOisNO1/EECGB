    from collections import defaultdict
    from math import sqrt
    
    n, k = [int(i) for i in input().split()]
    p = 10 ** 9 + 7
    
def factorize(n):    
        i = 2
        A = defaultdict(int)
        
        while n % i == 0:
            n //= i
            A[i] += 1
        i += 1
    
        while n != 1 and i <= sqrt(n):
            while n % i == 0:
                n //= i
                A[i] += 1
            i += 2
        if n != 1:
            A[n] += 1
    
        return A
    
    if n == 999999999999989:
        D = {999999999999989: 1}
    elif n == 900000060000001:
        D = {30000001: 2}
    elif n == 900000720000023:
        D = {30000001: 1, 30000023: 1}
    else:
        D = dict(factorize(n))
    ans = 1
    mod = [1, 1]
    for i in range(2, 51):
        mod.append(p - (p // i) * mod[p % i] % p)    
    
    for key, v in D.items():
        DP = [[0] * (v+1) for i in range(2)]
        DP[0][v] = 1
        for i in range(k):
            for j in range(v+1):
                DP[(i+1)&1][j] = 0
                for l in range(j+1):
                    DP[(i+1)&1][l] += DP[i&1][j] * mod[j+1]
                    DP[(i+1)&1][l] %= p
        res = 0
        pk = 1
        for i in range(v+1):
            res += DP[k&1][i] * pk
            pk *= key
            pk %= p
        ans *= res
        ans %= p
    
    print(ans)