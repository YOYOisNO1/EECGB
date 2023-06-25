    import math
    import sys
    import collections
    
    # imgur.com/Pkt7iIf.png
    
def getdict(n):
        d = {}
        if type(n) is list:
            for i in n:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        else:
            for i in range(n):
                t = ii()
                if t in d:
                    d[t] += 1
                else:
                    d[t] = 1
        return d
def cdiv(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a*b) // math.gcd(a, b)
    
    a, b = mi()
    a, b = min(a,b), max(a,b)
    ac = '0'
    bc = '1'
    if a%2 == 0:
        a, b, ac, bc = b, a, '1', '0'
    t = ''
    s = ac + bc
    for i in range(min(a, b)):
        t += s
        s = s[::-1]
    t += ac*(a - min(a,b)) + bc*(b - min(a,b))
    p = v = 0
    for i in range(a+b-1):
        if t[i] == t[i+1]:
            p += 1
        else:
            v += 1
    print(p, v)
    
    