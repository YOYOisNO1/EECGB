    from random import randrange
    
    T = input()
    
def rwh_primes2(n):
        # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
        """ Input n>=6, Returns a list of primes, 2 <= p < n """
        correction = (n%6>1)
        n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
        sieve = [True] * (n/3)
        sieve[0] = False
        for i in xrange(int(n**0.5)/3+1):
          if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
        return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
    
    #pp = rwh_primes2(1000000)
    
def miller_rabin(n, k=10):
        if n == 2 or n== 3:
            return True
        if not n & 1:
            return False
    
    def check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                return True
            for i in xrange(s - 1):
                if x == n - 1:
                    return True
                x = pow(x, 2, n)
            return x == n - 1
    
        s = 0
        d = n - 1
    
        while d % 2 == 0:
            d >>= 1
            s += 1
    
        for i in xrange(k):
            a = randrange(2, n - 1)
            if not check(a, s, d, n):
                return False
        return True
    
    for t in xrange(T):
        a, b = map(int, input().split())
    
        if a-b == 1:
            if miller_rabin(a+b):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")