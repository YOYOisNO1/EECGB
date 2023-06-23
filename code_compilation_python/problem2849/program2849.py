def program2849():
    n = int(input())
    
    fib = [0] * 55
    
    fib[0] = 0
    fib[1] = 2
    fib[2] = 3
    
    for x in xrange(3, len(fib)):
        fib[x] = fib[x-1] + fib[x-2]
    
    x = 0
    
    while fib[x] <= n:
        x += 1
    
    print x - 1