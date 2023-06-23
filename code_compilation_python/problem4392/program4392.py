    inp = input
    n, m = map(int, inp().split())
    sabs = [int(v) - 1 for v in inp().split()]
    cols = [int(v) for v in inp().split()]
    t = sum(cols)
def ok():
        for i in range(m):
            if K[i] != cols[i]: return False
        return True
    K = [0]*len(cols)
    for i in range(t):
        K[sabs[i]] += 1
    
    for i in range(t, n):
        if ok():
            print('YES')
            exit(0)
        K[sabs[i]] += 1
        K[sabs[i - t]] -= 1
    
    if ok():
        print('YES')
    else:
        print('NO')
        