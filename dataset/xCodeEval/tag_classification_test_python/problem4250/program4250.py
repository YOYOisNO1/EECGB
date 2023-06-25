    A,B,C,D = map(int,input().split())
    X = B-A+1
    Y = C-B+1
    
def cnt(c):
        if A+B > c: return X*Y
        if B+C <= c: return 0
        m = B+C - c
        if X > Y:
            if m <= Y:
                return m*(m+1)//2
            elif m <= X:
                return (m+m-Y+1)*Y//2
            else:
                n = X+Y-1-m
                return X*Y - n*(n+1)//2
        else:
            if m <= X:
                return m*(m+1)//2
            elif m <= Y:
                return (m+m-X+1)*X//2
            else:
                n = X+Y-1-m
                return X*Y - n*(n+1)//2
    ans = 0
    for c in range(C,D+1):
        ans += cnt(c)
    print(ans)