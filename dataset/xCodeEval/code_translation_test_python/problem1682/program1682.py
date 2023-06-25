    import sys
    from array import array  # noqa: F401
    from itertools import product
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    n = int(input())
    cand = set()
    
    for i, (a, b, c) in enumerate(input().split() for _ in range(n)):
        a = list(map(int, a))
        b, c = int(b), int(c)
        s = set()
    
        for p in product(range(10), repeat=4):
            if len(set(p)) < 4:
                continue
            b_, c_ = 0, 0
            for j in range(4):
                if p[j] == a[j]:
                    b_ += 1
                elif p[j] in a:
                    c_ += 1
            if b == b_ and c == c_:
                s.add(''.join(map(str, p)))
    
        if i == 0:
            cand = s
        else:
            cand &= s
    
    if len(cand) == 1:
        print(cand.pop())
    elif len(cand) > 1:
        print('Need more data')
    elif not cand:
        print('Incorrect data')
    else:
        assert False