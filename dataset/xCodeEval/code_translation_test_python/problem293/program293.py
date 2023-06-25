    n,m=map(long,input().split())
def f(n,i,m):
        if i==n:
            return str(i)
        r=2**(n-i-1)
        if m>r:
            return f(n,i+1,m-r)+' '+str(i)
        else: return str(i)+' '+f(n,i+1,m)
    op=f(n,1,m).split()
    print(' ').join(op)