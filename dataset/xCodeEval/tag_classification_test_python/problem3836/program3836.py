    
def gcd(a, b):
       if(a == 0):
          return b
       return gcd(b % a, a)
    
    min, max = map(int, input().split())
    
    if min > max:
       max, min = min, max
       
    den, num = 6, 6 - max + 1
    _gcd = gcd(num, den)
    den, num = den / _gcd, num / _gcd
    
    print("%d/%d") % (num, den)