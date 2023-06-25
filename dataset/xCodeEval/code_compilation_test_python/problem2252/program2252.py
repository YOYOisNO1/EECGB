def program2252():
    n,m = map(int,input().split())
    l = [0]*(n+1)
    c=1
    for i in range(1,n+1):
        l[i] = i*c
        c = l[i]
    ans =0
    for i in range(n):
        ans += (n-i)*l[n-i]*l[i+1]
    print(ans%m)