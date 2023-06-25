def readarray(f): return map(f, input().split())
def readint(): return int(input())
def printlist(l): print(' ').join(map(str, l))
    
    x, y, a, b = readarray(int)
    
    from fractions import gcd
    
    lcm = x*y/gcd(x, y)
    
    ma = (a/lcm)*lcm
    if ma < a:
      ma += lcm
    mb = (b/lcm)*lcm
    res = (mb-ma)/lcm+1
    
    print(res)