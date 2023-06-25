    import sys
    import math
    import itertools
    import collections
    
    
def divs(n, start=2):
        r = []
        for i in range(start, int(math.sqrt(n) + 1)):
            if (n % i == 0):
                if (n / i == i):
                    r.append(i)
                else:
                    r.extend([i, n // i])
        return r
def cdiv(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def wr(arr): return ' '.join(map(str, arr))
def revn(n): return str(n)[::-1]
def prime(n):
        if n == 2: return True
        if n % 2 == 0 or n <= 1: return False
        sqr = int(math.sqrt(n)) + 1
        for d in range(3, sqr, 2):
            if n % d == 0: return False
        return True
def convn(number, base=3):
        newnumber = ''
        while number > 0:
            newnumber = str(number % base) + newnumber
            number //= base
        return newnumber
    
    
def z(n):
        if n <10:
            return '0' + str(n)
        else:
            return str(n)
    
    hh, mm = map(int, input().split(':'))
    if mm + 1 == 60:
        if hh == 23:
            hh = 0
        else:
            hh += 1
        mm = 0
    else:
        mm += 1
    while z(hh) != revn(z(mm)):
        if mm + 1 == 60:
            if hh == 23:
                hh = 0
            else:
                hh += 1
            mm = 0
        else:
            mm += 1
    print(z(hh) + ":" + z(mm))