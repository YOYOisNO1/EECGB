    import sys
     
    p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def MI(): return map(int, sys.stdin.buffer.readline().split())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline().rstrip()
def SI(): return sys.stdin.buffer.readline().rstrip().decode()
def li(): return [int(i) for i in input().split()]
def lli(rows): return [li() for _ in range(rows)]
def si(): return input()
def ii(): return int(input())
def ins(): return input().split()
    
    p=10**9+7
    
    
def solve():
        n,k=MI()
        if n%2!=0:
            return pow((pow(2,n-1,p)+1)%p,k,p)
        else:
            if k==0:
                return 1
            twon=pow(2,n,p)
            util=(pow(2,n-1,p)-1)%p
            ans=pow(util,k,p)
            f1,f2=1,pow(twon,k-1,p)
            for i in range(1,k+1):
                ans=(ans+(f1*f2)%p)%p
                f1=(f1*util)%p
                f2=(f2*pow(twon,p-2,p))%p
            return ans
                
            
    
    
    
    
    t=II()
    for _ in range(t):
        print(solve())