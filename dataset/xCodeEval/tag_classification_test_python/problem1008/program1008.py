    import sys
    
    sys.setrecursionlimit(10**5)
    int1 = lambda x: int(x)-1
    p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def MI(): return map(int, sys.stdin.buffer.readline().split())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline()[:-1]
def SI(): return sys.stdin.buffer.readline()[:-1].decode()
    
    n=II()
    aa=LI()
    bb=LI()
    mn=sum(max(aa[i]-bb[i]-bb[i-1],0) for i in range(3))
    mx=sum(min(aa[i-1],bb[i]) for i in range(3))
    print(mn,mx)