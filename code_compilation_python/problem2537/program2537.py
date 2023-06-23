def program2537():
    n,k = map(int,input().split())
    MOD = 1000000007
    cur = 1
    ans = 0
    for i in range(k+1):
        ans+=cur
        cur*= (n-i)*pow(i+1,MOD-2,MOD)
    print(ans%=MOD)