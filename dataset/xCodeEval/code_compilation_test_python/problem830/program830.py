def program830():
    import math
    n, m = list(map(int,input().split()))
    if n % m == 0:
        print(*m*(int(n/m),), sep=' ')
    
    else:
        print(*str(n//m) * (m-(n%m)), *str(math.ceil(n/m)) * (n%m), sep =' ')
        