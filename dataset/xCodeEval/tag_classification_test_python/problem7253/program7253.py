    #sum(c = 0 to n) (Binomial[m*(n-1), n - c] * Binomial[m, c] * (c/n)^2)/Binomial[m*n, n]
    from math import *
    n, m = map(int, input().split(" "))
    
    d = {}
def b(n, k):
        #print(n,) k
        #input("")
        if k > n or k < 0:
            return 0
        if (n, k) in d:
            return d[(n, k)]
        result = 0
        for i in range(1, k+1):
            result += log(n-i+1) - log(i)
        d[(n, k)] = result
        return result
    
    print(n*sum([exp(b((n-1)*(m),) n - c) + b(m, c) - b(m*n, n)) * (c/float(n))**2 for c in xrange(1, min(n, m) + 1)])