def program630():
    n = int(input())
    k = int(input())
    A = int(input())
    B = int(input())
    
    cost = 0
    if k == 1:
        cost = (n-1)*A
        n = 0
    while n > 0:
        steps = n-((n//k)*k)
        steps = min(steps, n-1)
        cost += steps * A
        n -= steps
        if n == 1:
            break
        steps = n-n//k
        if steps*A < B:
            cost += steps*A
        else:
            cost += B
        n -= steps
    
    print((cost))