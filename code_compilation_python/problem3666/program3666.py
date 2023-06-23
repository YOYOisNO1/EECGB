def C(n, m):
        return 1 if n==m or m==0 else C(n-1, m-1)+C(n-1, m)
    
    n, m=map(int, input().split())
    ans=1
    
    if m>=2:
        ans+=C(n, 2)
    
    if m>=3:
        ans+=C(n, 3)*2
    
    if m>=4:
        ans+=C(n, 2)*C(n-2, 2)//2
        ans+=C(n, 4)*6
    
    print(ans)