    #! /usr/bin/env python3
    
def phib_gen(n):
        p = [1, 1]
        for i in range(2, n):
            p.append(p[-1] + p[-2])
        return tuple(p)
    
    n, k = tuple(map(int, input().split()))
    
    phib = phib_gen(n + 1)
    
def gen_sequence(n, k):
        while n > 0:
            if k >= phib[n - 1]:
                k -= phib[n - 1]
                n -= 2
                yield 2
            else:
                n -= 1
                yield 1
    
def gen_perm(n, k):
        elem = 1
        for i in gen_sequence(n, k):
            if i == 2:
                yield elem + 1
                yield elem
                elem += 2
            else:
                yield elem
                elem += 1
    
    print(' '.join(map(str, gen_perm(n, k - 1))))