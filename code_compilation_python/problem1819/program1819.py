def program1819():
    n, x = [int(i) for i in input().split()]
    total = 0
    for i in xrange(1, int(x**.5)+1):
        f = x%i
        if x%i == 0 and i <=n and x/i <= n:
            total += 1
        if x/float(i) == i:
            total -= .5
    return int(2*total)