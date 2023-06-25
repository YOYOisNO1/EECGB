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
def ask(m):print("?",m,flush=True);return II()
    for _ in range(II()):
        n,l,r,pc,d,mx = II(),0,n,0,1,0
        while l+1<r:m=(l+r)//2;c=pc+m*d;mx=max(mx,c);l=m;pc=c;d*=-1
        pc=n-mx;ask(pc);l,r,d = 0,n,1
        while l+1<r:
            m=(l+r)//2;c=pc+m*d
            if ask(c):r=m
            else:l=m
            pc=c;d*=-1
        print("=",r,flush=True)