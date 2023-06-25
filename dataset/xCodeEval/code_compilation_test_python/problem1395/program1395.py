def program1395():
    import sys
    n=int(input())
    *a,=map(int,input().split())
    if a==sorted(a):
        print('YES')
        sys.exit()
    mx=a.index(max(a))
    
    if(mx!=n-1)a=a[:mx]+a[mx+1:]+a[mx]
    if a==sorted(a):
        print('YES')
        sys.exit()
    print('NO')