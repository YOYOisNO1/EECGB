    import math
def isprime(n):
        if n == 2: return True
        if n % 2 == 0:  return False
        for x in range(3, int(math.sqrt(n)+1), 2):
            if n % x == 0:
                return False
        return True
    
def calc(n):
        if isprime(n):
            print 1
            print n
            return
        if isprime(n-2):
            print 2
            print 2, n-2
            return
        if isprime(n-3):
            print 2
            print 3, n-3
            return
        print 3
        for i in range(3, n/2, 2):
            if isprime(i) and isprime(n-i-3):
                print 3, i, n-i-3
                return
    
    n = int(input())
    calc(n)