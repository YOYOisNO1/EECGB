    inp = input
    R, B = map(int, inp().split())
    from itertools import permutations
    
    ships = [[int(v) for v in inp().split()] for _ in range(R)]
    base = [[int(v) for v in inp().split()] for _ in range(B)]
    if B < R:
        print('No')
        exit(0)
    
    
    ok = False
    
def crz(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
def cross(p1, p2):
        a, b = p1
        c, d = p2
        return crz(a, c, d)*crz(b, c, d) < 0 and crz(c, a, b)*crz(d, a, b) < 0
    
    for perm in permutations([i for i in range(B)]):
        pairs = []
        for i, p in enumerate(perm):
            if i == R: break
            pairs.append((ships[i], base[p]))
        ok2 = True
        for i in range(R):
            for j in range(i+1, R):
                if cross(pairs[i], pairs[j]):
                    ok2 = False
                    break
            if not ok2: break
        if ok2:
            ok = True
            break
    
    if ok:
        print('Yes')
    else:
        print('No')