def solve(k, p):
        c = {}
        for i in range(4):
            for j in range(4):
                x = p[i][j]
                if x == '.': continue
                if not x in c:
                    c[x] = 0
                c[x] += 1
        for v in c.values():
            if v > k*2: return False
        return True
    
    k = int(input())
    p = [[x for x in input()] for i in range(4)]
    print('YES') if solve(k, p) else 'NO'