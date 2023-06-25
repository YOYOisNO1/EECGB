def program6316():
    a,b = map(int, input().split())
    if a==b:
        ans = 1
    else:
        if b/10 > a/10:
            ans = 0
        else:
            ans = 1
            for i in range(a+1,b+1):
                ans = ans*i
    print(ans%10)