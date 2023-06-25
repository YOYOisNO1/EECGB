    from math import factorial
    
def gp(n, i, wo):
        if n == 1:
            return [1]
        head = i // factorial(n - 1) + 1
        tail = gp(n - 1, i % factorial(n - 1), [head] + wo)
        for i in range(len(tail)):
            if tail[i] >= head:
                tail[i] += 1
        return [head] + tail
    
def perm(n, i):
        return gp(n, i - 1, [])
    
def p(per):
        s = 0
        for i in range(len(per)):
            for j in range(i, len(per)):
                s += min(per[i:j+1])
        return s
    
    n, m = [int(i) for i in input().split()]
    
    perms = [perm(n, i) for i in range(1, factorial(n) + 1)]
    maxval = max(map(p, perms))
    
    print(*list(filter(lambda x: p(x) == maxval, perms))[m - 1])