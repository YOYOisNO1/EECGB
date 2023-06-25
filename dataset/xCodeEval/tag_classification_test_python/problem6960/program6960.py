    from math import factorial as fac
    
    tmp = 1
    fc = []
    for i in range(1001):
        fc.append(tmp)
        tmp *= (i+1)
    
def bio(n, m):
        if n < m:
            return 0
        return fc[n] // fc[m] // fc[n - m]
    
    
    inp = input('').split(' ')
    # inp = [1000, 1.00000]
    N, P = int(inp[0]), float(inp[1])
    
    for x in range(0, N):
        if (2 * bio(x, 3) + 2 *
            (N - x) * bio(x, 2) + x * bio(N - x, 2)) / (2 * bio(N, 3)) >= P:
            print(x)
            break