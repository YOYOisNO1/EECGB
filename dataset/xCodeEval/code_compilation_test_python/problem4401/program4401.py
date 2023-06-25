    import sys
    
    sys.setrecursionlimit(10 ** 6)
    int1 = lambda x: int(x) - 1
    p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
def bit(xx):return [format(x,"b") for x in xx]
    popcnt=lambda x:bin(x).count("1")
    
def ask(m):
        print("?",m,flush=True)
        return II()
    
    for _ in range(II()):
        n=II()
        l=0
        r=n+1
        while l+1<r:
            m=(l+r)//2
            if ask(m):r=m
            else:l=m
        print("=",r)