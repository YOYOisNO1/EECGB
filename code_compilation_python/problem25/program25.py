    import sys
    
    # sys.setrecursionlimit(200005)
    int1 = lambda x: int(x)-1
    pDB = lambda *x: print(*x, end="\n", file=sys.stderr)
    p2D = lambda x: print(*x, sep="\n", end="\n\n", file=sys.stderr)
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline().rstrip()
    # inf = 18446744073709551615
    inf = 4294967295
    # md = 10**9+7
    md = 998244353
    
def ok(s, t):
        f = t.find(s)
        if f == -1: return False
        for i in range(f):
            if t[i] == "0": return False
        for i in range(f+len(s), len(t)):
            if t[i] == "0": return False
        return True
    
    x, y = LI()
    
    s1 = bin(x)[2:]+"1"
    while x & 1 == 0: x >>= 1
    s0 = bin(x)[2:]
    t = bin(y)[2:]
    # print(s0, s1)
    # print(t)
    
    if ok(s0, t):
        print("YES")
        exit()
    
    if ok(s1, t):
        print("YES")
        exit()
    
    if ok(s0[::-1], t):
        print("YES")
        exit()
    
    if ok(s1[::-1], t):
        print("YES")
        exit()
    
    print("NO")