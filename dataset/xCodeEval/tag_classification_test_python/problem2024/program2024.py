    from sys import stdin, setrecursionlimit
    from collections import *
    
    mem, mod = defaultdict(int), 1000000007
    
    
def add(a, b):
        return (a % mod + b % mod) % mod
    
    
def dp(s, ma):
        if s == n:
            if ma:
                return 0
            else:
                return 1
        if s > n:
            return 0
    
        if mem[s, ma] != -1:
            return mem[s, ma]
    
        res = 0
        for j in range(1, k + 1):
            res += dp(s + j, min((j < d), ma)) % mod
    
        mem[s, ma] = res
    
        return mem[s, ma] % mod
    
    
    n, k, d = map(int, stdin.readline().split())
    # print(dp(0, True))
    mem[0, 0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j < 0:
                break
            if j < d:
                mem[i, 0] = add(mem[i, 0], mem[i - j, 0])
                mem[i, 1] = add(mem[i, 1], mem[i - j, 1])
            else:
                mem[i, 1] = add(mem[i, 1], mem[i - j, 0])
                mem[i, 1] = add(mem[i, 1], mem[i - j, 1])
    
    print(mem[n, 1])