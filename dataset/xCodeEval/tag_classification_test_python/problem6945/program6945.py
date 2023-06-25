    import sys
    
    sys.setrecursionlimit(10**5)
    int1 = lambda x: int(x)-1
    p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def MI(): return map(int, sys.stdin.buffer.readline().split())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline().rstrip()
def SI(): return sys.stdin.buffer.readline().rstrip().decode()
    
    inf=10**16
    n=II()
    aa=LI()
    if n>70:
        print(1)
        exit()
    ans = inf
    for i in range(1,n-1):
        ll=[]
        mx=-inf
        x=0
        for j in range(i-1,-1,-1):
            x^=aa[j]
            if x>mx:
                mx=x
                ll.append((x,i-1-j))
        rr=[]
        mn=inf
        x=0
        for j in range(i,n):
            x^=aa[j]
            if x<mn:
                mn=x
                rr.append((x,j-i))
        # print(ll)
        # print(rr)
        # print()
    
        j=0
        for x,c in ll[::-1]:
            while j<len(rr) and rr[j][0]>=x:
                j+=1
            if j==len(rr):break
            cur=c+rr[j][1]
            ans=min(ans,cur)
    
    if ans==inf:print(-1)
    else:print(ans)