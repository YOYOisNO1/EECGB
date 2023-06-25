    n = int(input())
    crush = map(int, input().split())
    # print(n)
    # print(crush)
    
    crush = [c - 1 for c in crush]
    # print(crush)
    cycle = []
    for i in range(n):
        t = 1
        c = crush[i]
        while c != i and t <= n:
            c = crush[c]
            t += 1
        cycle.append(t)
    
def f(c):
        if c % 2 == 0:
            return c / 2
        else:
            return c
    
def gcd(a, b):
        if a % b == 0:
            return b
        return gcd(b, a % b)
    
def lcm(l):
        ln = len(l)
        if ln == 1:
            return l[0]
        if ln == 2:
            return l[0] * l[1] / gcd(l[0], l[1])
        
        return lcm( [lcm(l[:ln/2]), lcm(l[ln/2:])] )
    
    if n+1 in cycle:
        print(-1)
    else:
        cycle = list(set([f(c) for c in cycle]))
        print(lcm(cycle))