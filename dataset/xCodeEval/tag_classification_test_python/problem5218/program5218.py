    import sys
    import math
    
    p, q = map(int, sys.stdin.readline().split())
    
def is_palindrome(x):
        s = str(x)
        for i in xrange(len(s)/2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
        
def get_primes2(x):
        x, correction = x-x%6+6, 2-(x%6>1)
        sieve = [True] * (x/3)
        for i in xrange(1,int(x**0.5)/3+1):
          if sieve[i]:
            k=3*i+1|1
            sieve[      k*k/3      ::2*k] = [False] * ((x/6-k*k/6-1)/k+1)
            sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((x/6-k*(k-2*(i&1)+4)/6-1)/k+1)
        arr = [2,3] + [3*i+1|1 for i in xrange(1,x/3-correction) if sieve[i]] + [x]
        res = [0]*x
        ind = 0
        for i in xrange(1, x):
            if arr[ind] <= i+1:
                res[i] = res[i-1] + 1
                ind += 1
            else:
                res[i] = res[i-1]
        return res
    
    n = 2
    rub = [1]
    while(1):
        if is_palindrome(n):
            rub.append(rub[-1]+1)
        else:
            rub.append(rub[-1])
        if n >= 17 and p*rub[-1] < q * n / math.log(n):
            break
        if n >= 5393 and p*rub[-1] < q * n / (math.log(n) - 1):
            break
        n += 1
    
    pi = get_primes2(n)
    
    while(q*pi[n-1] > p*rub[n-1]):
        n -= 1
    
    print(>>) sys.stdout, n