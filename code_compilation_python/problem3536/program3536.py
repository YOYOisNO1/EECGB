def program3536():
    from fractions import gcd
    import math
    
    lcm = lambda a, b: a//gcd(a,b)*b
    a, b = (map(int, input().split()))
    
    d = abs(b-a)
    divs = {d}
    for i in range(2, int(math.sqrt(d))):
        if not d%i: divs |= {i, d//i}
    
    sol = [(lcm(a, b), 0)]
    for d in divs:
        k = d-a%d if a%d else 0
        sol.append((lcm(a+k, b+k), k))
    
    print(min(sol)[1])