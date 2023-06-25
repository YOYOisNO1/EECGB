    import sys
    sys_in = sys.stdin
    
    X2 = int(sys.stdin.read())
    
    
    primes = range(X2+1)
    
    for i in range(2, (X2+1)/2+1):
        if primes[i] == i:
            for k in range(i, X2+1, i):
                primes[k] = i
    
    
def get_max_div(i):
        return primes[i]
    
    
    min_X0 = -1
    d_max = get_max_div(X2)
    for X1 in range(X2, X2-d_max, -1):
        p0 = get_max_div(X1)
        X0 = X1-p0+1
        if X0 == 1:
            X0 = X1
        # print("{} p0, {} X0, {} p1, {} X1").format(p0, X0, d, X1)
        if X0 < min_X0 or min_X0 == -1:
            min_X0 = X0
    
    sys.stdout.write(str(min_X0)+"\n")