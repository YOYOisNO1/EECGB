    import sys;sys.setrecursionlimit(999999)
def f(L):
        n=len(L)
        if n==0: return 0
        if n==1: return 1
        diff=min(L)-1
        s=e=-1
        for i in range(n):
            L[i]-=diff
            if s==-1 and L[i]==1:
                s=i
                e=i
            if i>0 and e==i-1 and L[i]==1:
                e=i
        if s==0 and e==n-1:
            return str(bin(n)).count('1')
        R=9999
        cnt=e-s+1
        c2=cnt//2
        for a in range(c2+1):
            b=c2-a
            r=f(L[:s]+[2]*a)+f([2]*b+L[e+1:])
            R=min(r,R)
        return R+(cnt%2)
    input();print(f(list(map(int,input().split()))))