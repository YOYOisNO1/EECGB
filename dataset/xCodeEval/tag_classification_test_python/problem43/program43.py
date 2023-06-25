def program43():
    n,m,k=list(map(int,input().split()))
    m=min(m,k)
    print("YES" if n<=m else "NO")