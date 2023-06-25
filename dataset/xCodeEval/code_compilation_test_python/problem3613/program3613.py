    import sys
    import math
    
    p, q = map(int, sys.stdin.readline().split())
    
def is_palindrome(x):
        s = str(x)
        return all([s[i] == s[len(s)-1-i] for i in xrange(len(s)/2)])
        
def get_primes(x):
        arr = [0, 1] + [1, 0]*(x/2)
        for i in xrange(2, int(math.ceil(math.sqrt(n)))+1, 2):
            for j in xrange(i+2, x):
                if j % (i+1) == 0:
                    arr[j-1] = 0
        res = [0]*x
        for i in xrange(1, x):
            res[i] = res[i-1] + arr[i]
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
        n += 1
    
    pi = get_primes(n)
    
    while(q*pi[n-1] > p*rub[n-1]):
        n -= 1
    
    print >> sys.stdout, n