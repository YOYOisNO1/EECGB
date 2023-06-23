    input()
    x = sorted(map(int,input().split()))
def solve(x,rm,nx,ins):
        if nx == len(x):
            if rm == 2:
                return ins
            return float("inf")
        if nx == len(x)-1:
            if rm == 1:
                return ins
            return float("inf")
        return min(solve(x,rm+1,nx+1,ins),solve(x,rm,nx+2,ins+x[nx+1]-x[nx]))
    print solve(x,0,0,0)