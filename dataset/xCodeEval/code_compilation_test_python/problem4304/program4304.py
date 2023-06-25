    n = int(input()) - 1
    a = []
def inp(k):
        a.append(map(int, input().split()))
        k and inp(k - 1)
    inp(n)
def f(i,j,k,g):
        g(i,j,k)
        k and f(i,j,k-1,g)
        j and not k and f(i,j-1,n,g)
        i and not j and not k and f(i-1,n,n,g)
def upd(i,j,k):
        a[i][j] = min(a[i][j], a[i][k] + a[k][j])
    ans = 0
def sel(i,j,k):
        global ans
        ans = max(ans, a[i][j])
    f(n,n,n,upd)
    f(n,n,n,sel)
    print ans